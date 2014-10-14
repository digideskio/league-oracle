import os
import json
import requests
import random


class Command(object):
    def should_execute(self, message):
        pass

    def execute(self, message):
        pass

    def send_message(self, content):
        post_data = {
            'bot_id': 'e1b9d18e10fb81bc90e4e968c6',
            'text': content
        }
        print 'Sending message: {}'.format(content)
        resp = requests.post(
            'https://api.groupme.com/v3/bots/post?token=ce19a9503568013263911e0cd8959d11',
            data=json.dumps(post_data), headers={'Content-Type': 'application/json'}
        )
        print 'GroupMe responded with status {}'.format(resp.status_code)
        print 'GroupMe responded with content {}'.format(resp.content)


class OracleCommand(Command):
    def should_execute(self, message_parts):
        if len(message_parts) < 2:
            return False
        return message_parts[0:2] == ['!oracle', self.name]


class RankingsCommand(OracleCommand):
    name = 'rankings'

    def should_execute(self, message_parts):
        if not super(RankingsCommand, self).should_execute(message_parts):
            return False
        if message_parts[-1].isdigit():
            return True
        return False

    def execute(self, message_parts):
        week = message_parts[-1]
        location = os.path.realpath(
            os.path.join(
                os.getcwd(), os.path.dirname(__file__)
            )
        )
        with open(os.path.join(location, 'rankings/week{}.txt'.format(week))) as f:
            rankings_text = f.read()

        self.send_message(rankings_text)


class DougCommand(OracleCommand):
    name = 'doug'

    def execute(self, message_parts):
        messages = [
            'Doug for president.',
            'Doug is the best.',
            'I love you Doug.',
        ]
        self.send_message(random.choice(messages))
