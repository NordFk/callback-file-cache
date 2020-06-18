import json
import os
import pickle as pickle
import hashlib


class File:
    def __init__(self, directory=None):
        self.directory = 'cache' if directory is None else directory
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)

    def get_cache_file_name(self, key: str):
        result = hashlib.md5(key.encode())
        return self.directory + "/" + result.hexdigest() +'.pickle'

    def get(self, key: str):
        filename = self.get_cache_file_name(key)
        if os.path.isfile(filename):
            return pickle.load(open(filename, 'rb'))

    def set(self, key: str, data):
        filename = self.get_cache_file_name(key)
        pickle.dump(data, open(filename, 'wb'))

    def clear(self, key: str):
        filename = self.get_cache_file_name(key)
        if os.path.isfile(filename):
            os.remove(filename)

    def get_with_callback(self, **kwargs):
        callback = kwargs.pop("callback")
        key = json.dumps(kwargs, default=str, sort_keys=True)
        value = self.get(key)
        if value is None:
            value = callback(**kwargs)
            if value is not None:
                self.set(key, value)
        return value
