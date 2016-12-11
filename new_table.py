import config
import MySQLdb

def connect_db():
    """Connect database and return db and cursor"""
    db = MySQLdb.connect(host="localhost",user='root',
                          passwd=config.PASSWORD ,db="twitter")
    cursor = db.cursor()
    return db, cursor

def table_exists(table_name):
    """Check table existence base on table name"""
    db, cursor = connect_db()
    cursor.execute("SELECT * FROM information_schema.tables \
                   WHERE table_name = '%s'" % table_name)
    nrows = int(cursor.rowcount); db.close()
    return False if nrows == 0 else True

def create_twitter_table():
     # Connect database
    db, cursor = connect_db()
    # (key, id, hashtag, content, time)
    sql = """CREATE TABLE twitter(
             id BIGINT UNIQUE,
             hashtag CHAR(25) NOT NULL,
             content TEXT,
             time DATETIME)
             CHARACTER SET = utf8""" # support Chinese
    if not table_exists('twitter'):
        cursor.execute(sql)
        print("Table twitter created sucessfully!")
    else:
        print("Table twitter already exists!")
    db.close()

def drop_twitter_table(table_name = "twitter"):
    db, cursor = connect_db()
    if table_exists(table_name):
        sql = """DROP TABLE %s""" % table_name
        print("Table twitter droped!")
        cursor.execute(sql)
    else:
        print("Table twitter does not exist!")
    db.close()

if __name__ == '__main__':
    drop_twitter_table()
    create_twitter_table()
    