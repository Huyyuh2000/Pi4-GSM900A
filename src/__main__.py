import argparse

from src.sim900a.sim900a import Sim900a

parser = argparse.ArgumentParser(description='Sim900A module interface')
parser.add_argument('action', help='action to be executed')
parser.add_argument('target',  help='target phone number')
parser.add_argument('content',  help='message content')

if __name__ == '__main__':
    args = parser.parse_args()

    # Init Sim900a
    s = Sim900a()

    if (args.action == 'send'):
        s.send_message(args.target, args.content)