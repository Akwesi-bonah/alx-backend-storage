#!/usr/bin/env python3
""" Define class Cache"""

from redis import Redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> callable:
    """count_calls method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> callable:
    """call_history method"""
    key = method.__qualname__
    input_list_key = key + ":inputs"
    output_list_key = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""
        self._redis.rpush(input_list_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, output)
        return output
    return wrapper


def replay(fn: Callable):
    """replay method"""
    key = fn.__qualname__
    redis = Redis()
    count = redis.get(key)
    input_list_key = key + ":inputs"
    output_list_key = key + ":outputs"

    print("{} was called {} times:".format(key, count))
    inputs = redis.lrange(input_list_key, 0, -1)
    outputs = redis.lrange(output_list_key, 0, -1)

    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """declear ridis class"""

    def __init__(self) -> None:
        """init method"""
        self._redis = Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''convert the data back to the desired format'''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """get_str method"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """get_int method"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
