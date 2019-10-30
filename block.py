import time
import json
import pickle
import hashlib

import utils
from proof_of_work import PoW


class block(object):

    """Docstring for block. """

    def __init__(self, prev_hash : str, data : str, height : int):
        """TODO: to be defined. """
        self.data = data
        self.timestamp = str(int(time.time()))
        self.prev_hash = prev_hash
        self.height = height
        self.nouce = None
        self._hash = None


    @property
    def hash(self):
        return self._hash

    def pow_of_block(self):
        """
        Returns: block
        """
        pow_block = PoW(self)
        nonce, hash_hex = pow_block.run()
        self.nonce, self._hash = nonce, hash_hex
        return self

    def printBlock(self):
        """
        Print data of Block
        """
        print("Prev hash: ")
        print(self.prev_hash)
        print("Data: ", self.data)
        print("Hash: ")
        print(self.hash)
        print("Height: ", self.height)
        print("PoW: ", PoW(self).validate(), '\n')

