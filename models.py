from flask_bcrypt import generate_password_hash, check_password_hash
import mongoengine as me


class Records(me.Document):
    email = me.StringField(required=True, unique=True)
    password = me.StringField(required=True)

    def hashing(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check(self, password):
        return check_password_hash(self.password, password)
