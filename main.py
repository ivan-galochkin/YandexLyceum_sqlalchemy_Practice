from flask import Flask
from db_session import *
from models import *

app = Flask(__name__)
app.config['abc'] = 'abc'


def add_user():
    session = create_session()
    dictionary = [['Scott', 21, 'captain', 'researcher engineer', 'module_1', 'scott_chief@mars.org'],
                  ['Elon Mask', 120, 'captain', 'genius', 'module_2', 'elonmask@mail.ru'],
                  ['Berlin hospital patient', 30, 'prisoner', 'rebel', 'module_3', 'navalny@gosdep.us'],
                  ['Yaroslav Filippov', 17, 'student', 'pygamer', 'module_1', 'yaroslav_asu@yandex.ru']]
    try:
        for data in dictionary:
            user = User()
            user.name = data[0]
            user.age = data[1]
            user.position = data[2]
            user.speciality = data[3]
            user.address = data[4]
            user.email = data[5]
            session.add(user)
        session.commit()
    finally:
        session.close()


def main():
    global_init('newdb.sqlite')
    try:
        add_user()
    finally:
        app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == "__main__":
    main()
