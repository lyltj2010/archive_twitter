import config
import twitter
import re
import MySQLdb
import time

api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_KEY,
                  access_token_secret=config.ACCESS_SECRET)

def connect_db():
    """Connect database and return db and cursor"""
    db = MySQLdb.connect(host="localhost",user='root',
                          passwd=config.PASSWORD ,db="twitter")
    cursor = db.cursor()
    return db, cursor

def insert_twitter_db(record):     
    db, cursor = connect_db()
    sql = """INSERT INTO twitter(id, hashtag, content, time)
           VALUES ('%d',  '%s', '%s', '%s')"""
    tp = (record["id"],record["hashtag"],record["content"],record["time"])
    try:
        cursor.execute(sql % tp)
        db.commit()
    except:
        db.rollback()
        print("Roll back due to error!")
    db.close()

def get_ids():
    """Make sure no duplicates"""
    db, cursor = connect_db()
    sql = """SELECT id FROM twitter"""
    try:
        cursor.execute(sql)
        ids = {x[0] for x in cursor.fetchall()}
        return ids
    except:
        print("Error in fetching ids!")
    db.close()

def insert_records(timeline):
    for t in timeline:
        if t.id in get_ids():
            print("Duplicated record! %s") % t.id
            continue
        record = {}
        if len(t.hashtags) == 0:
            hashtag = "notag"
            text = t.text
        else:
            hashtag = t.hashtags[0].text
            text = re.sub(u"^#[\u4e00-\u9fa5_a-zA-Z]+\s+","", t.text)
        record["id"] = t.id 
        record["hashtag"] = hashtag
        record["content"] = text
        tm = time.strptime(t.created_at, "%a %b %d %H:%M:%S +0000 %Y")
        record["time"] = time.strftime("%Y-%m-%d %H:%M:%S", tm)
        insert_twitter_db(record)
        print("Record inserted sucessfully! %d") % t.id

if __name__ == '__main__':
    timeline = api.GetHomeTimeline()
    insert_records(timeline)
