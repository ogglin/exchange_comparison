import psycopg2

from exchange_comparison.env import *


def _query(q):
    # print(q)
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
        if 'no results' not in err:
            print("Error: ", err)
    else:
        return data
    finally:
        con.commit()


def _query_cols(q):
    # print(q)
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
        colnames = list([desc[0] for desc in cur.description])
    except psycopg2.DatabaseError as err:
        print("Error: ", err)
    else:
        return data, colnames
    finally:
        con.commit()
