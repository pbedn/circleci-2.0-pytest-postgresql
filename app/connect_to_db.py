import psycopg2
from app.config import db_login_dict

SQL_QUERY = """
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
"""

def setup_database(cur):
    cur.execute(psycopg2.sql.SQL(SQL_QUERY))

def connect_to_db(db_type):
    db = db_login_dict[db_type]
    con = psycopg2.connect(database=db.database, user=db.user, password=db.password, host=db.host)
    cur = con.cursor()
    return con, cur
