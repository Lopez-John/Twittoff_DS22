from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model): # User Table
    '''Twitter Users corresponding to Tweets'''
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column
    name = DB.Column(DB.STring, nullable=False)  # name column

    def __repr__(self):
        return'User: {}>'.format(self.name)


class Tweet(DB.Model):
    '''Tweets corresponding to Users'''
    id = DB.Column(DB.BigInteger, primary_key=True) # id column
    test = DB.Column(DB.Unicode(300))  # tweet text column - allows for emojis
    user_id = DB.Column(DB.BigInteger, DB.ForiegnKey(
        'user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet: {}>.format(self.text)