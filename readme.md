## Twitter Database

Get all your twitter timeline, retrive information and save to database. Once saved to database, you can organize base on hashtag and time.

## Usage

First get your twitter api. Details can be found [here](https://python-twitter.readthedocs.io/en/latest/getting_started.html)  

Then create a mysql database named twitter`(id, hashtag, content, time)`.  

Fill in the `config.py` with your twitter api information and database password.  

```python
# Twitter API
CONSUMER_KEY = "xxxxxxxxx"
CONSUMER_SECRET = "xxxxxxxxx"
ACCESS_KEY = "xxxxx-xxxxxx"
ACCESS_SECRET = "xxxxxx"
# Database
PASSWORD = "xxxxxx"
```

Then `python new_table.py` and a table named twitter should be created.  

Then `python mytwitter.py` and you twitter data should be in your database now.  


## Python Twitter

`pip install python-twitter` to get started. This twitter wrapper documents can be found [here](https://python-twitter.readthedocs.io/en/latest/index.html).

## Pyhthon MySQL 

A quick [guide](http://www.jianshu.com/p/9a0318da1399).
