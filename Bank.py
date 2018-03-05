import nacl.signing
import sqlite3

class Bank():
    DB_NAME = 'example.db'

    def __init__(self, id):
        self.id = id
        self.signing_key = nacl.signing.SigningKey.generate()
        self.verify_key = self.signing_key.verify_key


    def genererate_digital_signature(self, user, password, signing_key):
        user_data = self.query_user(user, password)
        data_for_signing = (self.id, user, self.signing_key, signing_key, 312312123123, str(user_data))
        print(str(data_for_signing))
        signed_data  = self.signing_key.sign(str(data_for_signing).encode('ascii'))

        return signed_data.signature

    @staticmethod
    def create_db():
        conn = sqlite3.connect(Bank.DB_NAME)
        c = conn.cursor()
        c.execute('''CREATE TABLE user(user_id, password, credit_card, data_expirare, limita_creditare)''')
        conn.commit()
        conn.close()


    def query_user(self, id, password):
        conn = sqlite3.connect(Bank.DB_NAME)
        c = conn.cursor()
        c.execute("SELECT credit_card, data_expirare, limita_creditare FROM user WHERE user_id=(?) and password=(?)",
                  (id, password,))
        data = c.fetchone()
        conn.close()

        if data == None or len(data) == 0:
            return -1
        else:
            return data


if __name__ == "__main__":
    # Call when there's no database
    # Bank.create_db()
    print(Bank('uid001', 'uid').query_user())

