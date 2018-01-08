#!/usr/bin/env python
# coding: utf-8
from wxbot import *
import random
import time


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:  # group message
            group_id = msg['user']['id']
            group_name = self.check_user_name(msg['user']['name'])
            content = msg['content']['data']
            print content
        elif msg['msg_type_id'] == 4 and msg['content']['type'] == 0:  # contact messageos
            content = msg['content']['data']
            print content

    def check_user_name(self, name):
        result = ""
        i = 0
        while i < len(name):
            if name[i] == "<":
                while name[i] != '>':
                    i += 1
            else:
                result += name[i]
            i += 1
        return result

    def send_message(self, content):
        for group in self.group_list:
            '''group_name = self.check_user_name(group['NickName'].encode('utf-8'))
            print group_name + "--" + str(group['NickName'].encode('utf-8').startswith('Where is cheese'))'''
            self.send_msg_by_uid(content, group['UserName'])
            time.sleep(1)

    def send_message_test(self, content):
        print content

    def group_reply(self, content):
        results = {
            'cheese': ['aa', 'bb']
        }[content]
        num = random.random() * len(results)
        return results[int(num)]
