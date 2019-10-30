import os
from block import block
import pickledb
import utils
from proof_of_work import PoW

class block_chain():

    """Docstring for block_chain. """

    def __init__(self):
        """
        1. init the block list
        2. create a genesis block for this block chain
        """

        self.blocks = []
        self.db = None
        self.latest_block = None

        if ('block.db' not in os.listdir('.')):
            print("No existing blockchain found, create a new one...")
            utils.create_db('block')
            self.db = pickledb.load('block.db', True)
            genesis_block = block(prev_hash = None, data = 'Genesis Block', height = 0)
            genesis_block.pow_of_block()
            self.db.set(genesis_block.hash, utils.serialize(genesis_block))
            self.db.set('latest', genesis_block.hash)
        else:
            self.db = pickledb.load('block.db', True)

    def addBlock(self, data: str):
        """
        create a new block for this block chain

        Args:
            data (str): data for this new block

        Returns: TODO

        """
        latest = self.db.get('latest')
        height = utils.deserialize(self.db.get(latest)).height
        new_block = block(prev_hash = latest, data=data, height=height)
        new_block = new_block.pow_of_block()
        self.db.set('latest', new_block.hash)
        self.db.set(new_block.hash, utils.serialize(new_block))

    def printChain(self):
        latest = self.db.get('latest')
        current_block = utils.deserialize(self.db.get(latest))
        while True:
            current_block.printBlock()
            if current_block.prev_hash == None:
                break
            current_block = utils.deserialize(self.db.get(current_block.prev_hash))

    def printBlock(self, height):
        latest = self.db.get('latest')
        current_block = utils.deserialize(self.db.get(latest))
        while current_block.height != height:
            current_block = utils.deserialize(self.db.get(current_block.prev_hash))
        current_block.printBlock()
