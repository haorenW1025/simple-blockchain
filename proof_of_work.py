import sys

import utils

class PoW():

    """Performs proof-of-work"""

    max_nonce = sys.maxsize
    target_bit = 15
    def __init__(self, b):
        """
        Args:
            block (block object)
        """
        self._block = b
        self.target = 1 << (256 - PoW.target_bit)

    def prepare_data(self, nonce):
        """
        concatenate block, target_bit and nonce for run process of pow
        Args:
            nonce (big integer)
        Returns:
            data: for running process of pow
        """

        data = [self._block.prev_hash ,self._block.data ,
                self._block.timestamp ,str(self.target_bit) ,str(nonce)]
        if self._block.prev_hash == None:
            data.remove(self._block.prev_hash)
        return ''.join(data)

    def run(self) -> (int, str):
        """
        for every nonce, calculate its hash until it is bigger than target
        Returns:
            nonce: a legal nonce
            hash: the corresponding hash
        """
        nonce = 0
        print("Mining block with data = {data}".format(data=self._block.data))
        while nonce < PoW.max_nonce:
            print('trying nonce: {n}'.format(n=nonce) , end='\r')
            data = self.prepare_data(nonce)
            hash_hex = utils.gen_sha_value(data)
            hash_int = int(hash_hex, 16)

            if hash_int < self.target:
                break
            else:
                nonce+=1
        print('\n')
        print("Success!")
        print("Nonce = {n}\n".format(n=nonce))
        return nonce, hash_hex

    def validate(self) -> bool:
        """
        check if this nonce is validate or not
        Returns:
            bool: validate or not
        """
        data = self.prepare_data(self._block.nonce)
        hash_int = int(utils.gen_sha_value(data), 16)

        return hash_int < self.target
