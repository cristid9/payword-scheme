class Payment():

    def __init__(self, id, amount, hash_index):
        self.id = id
        self.amount = amount
        #self.hash_index = hash_index

    def __str__(self):
        return self.id + " -- " + str(self.amount)
