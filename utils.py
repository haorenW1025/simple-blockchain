import json
import pickle
import hashlib


def encode(str, code='utf-8'):
    """ perform utf-8 encode """
    return str.encode(code)

def gen_sha_value(data : str):
    """ return sha256 value of given string

    Args:
        data (string)

    Returns: sha256 value of data

    """
    s = hashlib.sha256()
    s.update(encode(data))
    return s.hexdigest()

def create_db(name : str):
    empty_dict = {}
    with open ( name + '.db', 'w') as outfile:
        json.dump(empty_dict, outfile)

def serialize(data):
    return pickle.dumps(data).decode('latin1')

def deserialize(data):
    return pickle.loads(data.encode('latin1'))
