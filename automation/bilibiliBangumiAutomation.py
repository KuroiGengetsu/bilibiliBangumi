#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests


class Parse:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}

    def __init__(self, serial):
        self.serial = serial
        self.url = 'http://bangumi.bilibili.com/jsonp/seasoninfo/' + serial + '.ver?callback=seasonListCallback&jsonp=jsonp'
        self.json = eval(requests.get(self.url, headers=self.headers).text[19: -2])

    def dump_json(self):
        if not os.path.exists(r'json'):
            os.makedirs(r'json')
        f = open('json/' + str(self.serial) + '.json', 'w+b')
        f.write(str(self.json).encode('utf8'))
        f.close()

    def dump_episodes(self):
        if not os.path.exists(r'json'):
            os.makedirs(r'json')
        f = open('json/' + str(self.serial) + '_episodes.json', 'w+b')
        f.write(str(self.episodes()).encode('utf8'))
        f.close()

    def episodes(self):
        episodes_list = self.json['result']['episodes']
        return episodes_list

    def count(self):
        episodes = self.episodes()
        return len(episodes)

    def key_url(self):
        episodes = self.episodes()
        episode = []
        count = self.count()
        for index in range(count):
            episode.append(episodes[index]['webplay_url'])
        return episode
