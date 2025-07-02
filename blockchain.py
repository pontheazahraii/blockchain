class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        """Creates a new Block and adds it to the chain"""
        ...

    def new_transaction(self):
        """Adds a new transaction to the list of transactions"""
        ...

    @staticmethod
    def hash(block):
        """Hashes a Block

        :param block: the block to hash
        :type block: Blockchain
        """
        ...

    @property
    def last_block(self):
        """Returns the last Block in the chain"""
        ...
