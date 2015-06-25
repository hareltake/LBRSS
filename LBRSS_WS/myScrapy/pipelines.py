# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from tables import News, Position
import json
import codecs


class NewsPipeline(object):

    def __init__(self):
        self.file = codecs.open('items.txt', 'w+', 'utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        Person.create()
        return item
