CREATE SCHEMA trains;

create sequence trains.gtfs_id_seq
    maxvalue 99999999999999999
;

create table trains.gtfs
(
    id integer default nextval('trains.gtfs_id_seq'::regclass) not null
        constraint gtfs_pkey primary key
    ,route char(6) not null
    ,active boolean default true not null
);

create index gtfs_id_idx
    on trains.gtfs (id)
;
