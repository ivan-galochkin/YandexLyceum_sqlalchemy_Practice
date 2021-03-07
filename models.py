import sqlalchemy as sa
import datetime as dt
from db_session import Base


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String, nullable=True)
    name = sa.Column(sa.String, nullable=True)
    age = sa.Column(sa.Integer, nullable=True)
    position = sa.Column(sa.String, nullable=True)
    speciality = sa.Column(sa.String, nullable=True)
    address = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True)
    hashed_password = sa.Column(sa.String)

    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String,
                      index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)
    modified_date = sa.Column(sa.DATETIME, default=dt.datetime.now)
