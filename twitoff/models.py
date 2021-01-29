"""SQLAlchemy models and utility functions for Twitoff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):  # User Table

    """Twitter Users corresponding to Tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column
    name = DB.Column(DB.String, nullable=False)  # name column
    newest_tweet_id = DB.Column(DB.BigInteger) # keeps track of newest tweet of user


    def __repr__(self):
        return "<User: {}>".format(self.name)


class Tweet(DB.Model):
    """Tweets corresponding to Users"""
    id = DB.Column(DB.BigInteger, primary_key=True)  # id column
    text = DB.Column(DB.Unicode(300))  # tweet text column - allows for emojis
    vect = DB.Column(DB.PickleType, nullable=False) # vectorize twets
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False)  # user_id column (corresponding user)
    user = DB.relationship("User", backref=DB.backref("tweets", lazy=True))  # creates user link between tweets

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)
