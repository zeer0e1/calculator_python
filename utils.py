import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string):
    return bool(NUM_OR_DOT_REGEX.search(string))


def isEmpty(string):
    return len(string) == 0
