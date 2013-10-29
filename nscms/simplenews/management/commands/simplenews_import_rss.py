#!/usr/bin/env python
#-*- coding:utf-8 -*-


from django.core.management.base import BaseCommand

from dateutil.parser import parse
import feedparser

from nscms.simplenews.models import SimpleNews


class Command(BaseCommand):
    help = u"Import news from RSS."

    def handle(self, *args, **options):
        for url in args:
            data = feedparser.parse(url)
            for entry in data['entries']:
                sn = SimpleNews()
                sn.published = True
                sn.title = entry['title']
                sn.publish_date = parse(entry['published'])
                sn.content = entry['summary']
                sn.save()
                print 'entry', sn
                for tag in entry['tags']:
                    print 'tag', tag['term']
                    sn.tags.add(tag['term'])
