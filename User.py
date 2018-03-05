import nacl.signing
from Payment import Payment

class User():

    def __init__(self, id, password):
        self.password = password
        self.id = id
        self.signing_key = nacl.signing.SigningKey.generate()
        self.verify_key = self.signing_key.verify_key
        # self.hash_index = self.verify_key.encode(encoder=nacl.encoding.HexEncoder)

    # def generatePayment(self, amount):
    #     payment = Payment(id, amount)
    #     return self.signing_key.sign(str(payment))

if __name__ == "__main__":
    u = User("a")
    print("a")
