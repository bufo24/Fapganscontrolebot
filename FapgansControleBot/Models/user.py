from sqlalchemy import Integer, Column, String

from FapgansControleBot.Repository.database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_username = Column(String(256))

    def __init__(self, user_id: int, user_username: str):
        self.user_id = user_id
        self.user_username = user_username

    def set_username(self, username: str):
        self.user_username = username
