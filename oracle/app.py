from flask import Flask, request
import json
import requests
import os

app = Flask(__name__)


class Message(object):
    def __init__(self, json):
        self.__dict__.update(json)


def send_message(content):
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


def print_rankings(week):
    location = os.path.realpath(
        os.path.join(
            os.getcwd(), os.path.dirname(__file__)
        )
    )
    with open(os.path.join(location, 'rankings/week{}.txt'.format(week))) as f:
        rankings_text = f.read()

    send_message(rankings_text)


def respond(message):
    print "Responding to message {}".format(message)
    if message.text.startswith('!oracle '):
        command = message.text.replace('!oracle ', '')
        if command:
            oracle_command(command)


def oracle_command(command):
    parts = command.split(' ')
    print '!oracle command: {}'.format(parts)
    if not parts:
        return
    if parts[0] == 'rankings' and len(parts) > 1 and parts[1].isdigit():
        print_rankings(parts[1])


@app.route('/message', methods=['POST'])
def incoming_message():
    try:
        message = request.json
        respond(Message(message))
    except Exception:
        print 'Failed to respond to message: {}'.format(request.json)
    return ''

if __name__ == '__main__':
    app.run()
