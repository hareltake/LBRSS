# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
import codecs
import sqlite3 as lite
from tables import News, Position


class NewsPipeline(object):
      

    def process_item(self, item, spider):
        news_id = item['id']
        title = item['title']
        link = item['link']
        desc = item['desc']

        position = Position.select().where(Position.id == news_id)
        News.create(pos=position, title=title, link=link, desc=desc)
        print news_id
        return item
