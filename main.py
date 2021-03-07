from flask import Flask
from db_session import *
from models import *

app = Flask(__name__)
app.config['abc'] = 'abc'


def main():
    global_init('database.db')
    app.run(port=8080, host='127.0.0.1', debug=True)
    session = create_session()
    try:
        captain = User()
        captain.name = 'Scott'
    finally:
        session.close()


if __name__ == "__main__":
    main()
