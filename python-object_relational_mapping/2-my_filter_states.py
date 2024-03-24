#!/usr/bin/python3
"""
A script that takes an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC").format(state_name_searched)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state_name_searched:
            print(row)
    cur.close()
    conn.close()
