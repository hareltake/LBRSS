from peewee import *

db = SqliteDatabase('LBRSS_WS/news.sqlite', check_same_thread=False)


class BaseModel(Model):

    class Meta:
        database = db

class Position(BaseModel):
	country = CharField()
	city = CharField()

class News(BaseModel):
	pos = ForeignKeyField(Position, related_name='news')
	title = CharField()
	link = CharField()
	desc = CharField()