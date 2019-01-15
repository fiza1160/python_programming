import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        res = func(*args, **kwargs)
        return json.dumps(res, )
    return wrapped
