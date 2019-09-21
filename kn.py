#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from django.conf.urls import url
from app01.views import index


class StarkSite(object):
    def __init__(self):
        self._registry = []

    def get_urls(self):
        patterns = []

        '''
        patterns = [
                    url(r'^index/', index.index),
                    url(r'^home/', index.home),
                ]
        '''

        for app in self._registry:
            # patterns.append(url(r'^index/',index.index))
            patterns.append(url(r'^%s/' % app,index.index))
        return patterns

    @property
    def urls(self):
        return (self.get_urls(), None, None)


site = StarkSite()
