import psycopg2

from exchange_comparison.env import *


def _query(q):
    con = psycopg2.connect(
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )
    cur = con.cursor()
    try:
        cur.execute(q)
        data = cur.fetchall()
    except psycopg2.DatabaseError as err:
        print("Error: ", err)
    else:
        return data
    finally:
        con.commit()
