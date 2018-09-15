import psycopg2
from app.config import db_login_dict


def connect_to_db(db_type):
    db = db_login_dict[db_type]
    con = psycopg2.connect(database=db.database, user=db.user, password=db.password, host=db.host)
    cur = con.cursor()
    return con, cur
