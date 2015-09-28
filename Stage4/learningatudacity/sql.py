import sqlite3

db = sqlite3.connect(':memory:')
db.execute("CREATE TABLE LINKS (id integer, title text, " +
           "submitter_id text, submitted_time integer, comments text, votes integer)")