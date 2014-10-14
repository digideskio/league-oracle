from flask import Flask, request

from oracle.commands import (
    RankingsCommand,
    DougCommand,
)

app = Flask(__name__)

commands = [
    RankingsCommand(),
    DougCommand(),
]


class Message(object):
    def __init__(self, json):
        self.__dict__.update(json)
        self.text = self.text.split(' ')


def respond(message):
    print "Responding to message {}".format(message.text)
    for command in commands:
        if command.should_execute(message.text):
            command.execute(message.text)


@app.route('/message', methods=['POST'])
def incoming_message():
    try:
        message = request.json
        respond(Message(message))
    except Exception as e:
        print 'Failed to respond to message: {}'.format(request.json)
        print 'Exception: {}'.format(e)

    return ''

if __name__ == '__main__':
    app.run()
