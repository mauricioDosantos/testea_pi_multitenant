begin;
create database if not exists validacao;
\c validacao
create table if not exists token_for_the_base(code uuid not null, base varchar(255));
insert into token_for_the_base(code, base) values('da153535-737c-4eb2-ba58-70eb325f1cdd', 'my_animal');

create database if not exists my_animal;
\c my_animal
create table if not exists animal_animal(name varchar(255));
insert into animal_animal(name) values('cachorro');
commit;
