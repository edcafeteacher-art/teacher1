-- Олимпиада Business English: хранилище ответов в Supabase.
-- Выполните весь файл в Supabase → SQL Editor → New query → Run.
-- ПЕРЕД ЗАПУСКОМ замените 'CHANGE-ME-PIN' на свой PIN преподавателя.
--
-- Схема доступа: прямого доступа к таблицам у анонимного ключа нет (RLS без политик).
-- Студент только отправляет работу через submit_result(); баллы считает сервер по ключу.
-- Преподаватель читает результаты через get_results(pin).

create extension if not exists pgcrypto;

create table if not exists public.settings (
  id int primary key default 1 check (id = 1),
  teacher_pin text not null,
  answer_key jsonb not null,
  points jsonb not null
);

create table if not exists public.results (
  id uuid primary key default gen_random_uuid(),
  surname text not null,
  name text not null,
  grp text not null,
  code text,
  answers jsonb not null,
  scores jsonb,
  auto_score int,
  open_score int,
  leaves int default 0,
  auto_submitted boolean default false,
  started_at timestamptz,
  submitted_at timestamptz default now()
);
create unique index if not exists results_person_uq
  on public.results (lower(trim(surname)), lower(trim(name)), lower(trim(grp)));

alter table public.settings enable row level security;
alter table public.results  enable row level security;
revoke all on public.settings, public.results from anon, authenticated;

-- Ключ. Строка означает один правильный ответ, массив означает несколько допустимых.
-- Сравнение без учёта регистра, лишних пробелов и типа апострофа.
insert into public.settings (id, teacher_pin, answer_key, points) values (1, 'CHANGE-ME-PIN',
 $key${
   "T": ["received","was","is preparing",["will be finished","is going to be finished","will have been finished","should be finished"],["have grown","have been growing"],"signed","are produced","visited","were loading","have",["will send","am going to send"],"hearing"],
   "R": ["a","an","the","-","the","an","the","-","the","an"],
   "C": ["for","with","to",["with","about"],"for","than","on","which",["but","although","though","yet"],"to"],
   "M": ["dreamed","set","make","high","take","invested","willing","employed","pays","over"],
   "W": ["successful","management","unrealistic","decision","dramatically","growth","unemployment",["adviser","advisor"],"reliable","development"],
   "P": ["C","A","E","B","E","B","A","D","D","A"],
   "A": ["To show that the choice of the place is a puzzle.","There are far fewer visitors per day outside the summer.","about 500 years older.","They found remains of huts at Durrington Walls.","The bluestones travelled about ten times farther than the sarsen stones.","They could organise a large number of workers.","The monument is aligned with the summer and winter solstices.","New technology shows the site is more complex than people thought."]
 }$key$::jsonb,
 '{"T":1,"R":1,"C":1,"M":1,"W":1,"P":1,"A":2}'::jsonb)
on conflict (id) do update set answer_key = excluded.answer_key, points = excluded.points;

create or replace function public.norm(t text) returns text
language sql immutable as $$
  select regexp_replace(replace(replace(lower(trim(coalesce(t,''))), '’', ''''), '‘', ''''), '\s+', ' ', 'g')
$$;

-- Подсчёт баллов по ключу
create or replace function public.score_answers(a jsonb) returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare k jsonb; pts jsonb; sec text; i int; c int; p int; e jsonb; ans text; s jsonb := '{}'; tot int := 0;
begin
  select answer_key, points into k, pts from settings where id = 1;
  for sec in select jsonb_object_keys(k) loop
    c := 0;
    for i in 0 .. jsonb_array_length(k -> sec) - 1 loop
      e := k -> sec -> i;
      ans := norm(a -> sec ->> i);
      if ans <> '' and (
           (jsonb_typeof(e) = 'array' and exists (select 1 from jsonb_array_elements_text(e) x where norm(x) = ans))
        or (jsonb_typeof(e) = 'string' and norm(e #>> '{}') = ans)) then
        c := c + 1;
      end if;
    end loop;
    p := coalesce((pts ->> sec)::int, 1);
    s := s || jsonb_build_object(sec, c * p);
    tot := tot + c * p;
  end loop;
  return s || jsonb_build_object('auto', tot);
end $$;

-- Отправка работы студентом (один раз на фамилию+имя+группу)
create or replace function public.submit_result(p jsonb) returns jsonb
language plpgsql volatile security definer set search_path = public as $$
declare sc jsonb;
begin
  if coalesce(trim(p->>'surname'),'') = '' or coalesce(trim(p->>'name'),'') = '' or coalesce(trim(p->>'grp'),'') = '' then
    raise exception 'surname, name and group are required';
  end if;
  if length(p::text) > 20000 then raise exception 'payload too large'; end if;
  sc := score_answers(p->'answers');
  insert into results (surname, name, grp, code, answers, scores, auto_score, leaves, auto_submitted, started_at)
  values (left(trim(p->>'surname'),80), left(trim(p->>'name'),80), left(trim(p->>'grp'),40), left(trim(coalesce(p->>'code','')),40),
          p->'answers', sc, (sc->>'auto')::int, coalesce((p->>'leaves')::int,0), coalesce((p->>'auto_submitted')::boolean,false),
          nullif(p->>'started_at','')::timestamptz);
  return jsonb_build_object('ok', true);
exception when unique_violation then
  return jsonb_build_object('ok', false, 'reason', 'duplicate');
end $$;

-- Чтение результатов преподавателем
create or replace function public.get_results(pin text) returns setof public.results
language plpgsql stable security definer set search_path = public as $$
begin
  if not exists (select 1 from settings where id = 1 and teacher_pin = pin) then raise exception 'wrong PIN'; end if;
  return query select * from results order by submitted_at;
end $$;

-- Балл за открытый ответ (0–4)
create or replace function public.set_open_score(pin text, rid uuid, s int) returns void
language plpgsql volatile security definer set search_path = public as $$
begin
  if not exists (select 1 from settings where id = 1 and teacher_pin = pin) then raise exception 'wrong PIN'; end if;
  update results set open_score = case when s is null then null else greatest(0, least(4, s)) end where id = rid;
end $$;

-- Пересчёт всех работ после правки ключа
create or replace function public.rescore_all(pin text) returns int
language plpgsql volatile security definer set search_path = public as $$
declare n int;
begin
  if not exists (select 1 from settings where id = 1 and teacher_pin = pin) then raise exception 'wrong PIN'; end if;
  update results set scores = score_answers(answers), auto_score = (score_answers(answers)->>'auto')::int;
  get diagnostics n = row_count; return n;
end $$;

revoke all on function public.score_answers(jsonb) from public, anon, authenticated;
grant execute on function public.submit_result(jsonb) to anon;
grant execute on function public.get_results(text) to anon;
grant execute on function public.set_open_score(text, uuid, int) to anon;
grant execute on function public.rescore_all(text) to anon;
