import os
import pytest

from app import my_app
from app.connect_to_db import connect_to_db, setup_database


DATABASE = os.environ["DB_NAME"]

input_data = [('000068', True),
              ('000069', True),
              ('000070', True)]

expected = [('000068', True),
            ('000069', True),
            ('000070', False)]


@pytest.fixture(scope="module")
def db():
    con, cur = connect_to_db(DATABASE)
    setup_database(cur)
    yield con, cur
    con.close()


def clean_and_populate_table(con, cur):
    cur.execute("SELECT TRUE FROM trains.gtfs LIMIT 1")
    try:
        cur.fetchone()[0]
        cur.execute("TRUNCATE trains.gtfs")
        cur.execute("ALTER SEQUENCE trains.gtfs_id_seq RESTART WITH 1")
        con.commit()
    except TypeError:
        pass
    for d in input_data:
        cur.execute("""
            INSERT INTO trains.gtfs
            (route,active) VALUES ('{route}',{active})
            """.format(route=d[0], active=d[1]))
    con.commit()


def select_and_fetch_query(cur):
    query = '''SELECT route,active FROM trains.gtfs ORDER BY route ASC'''
    cur.execute(query)
    return cur.fetchall()


def test_update_db(db):
    con, cur = db
    clean_and_populate_table(con, cur)
    my_app.using_database(con, cur)
    result = select_and_fetch_query(cur)
    assert result == expected
