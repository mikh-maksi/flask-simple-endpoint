from flask import Flask, render_template
import json
from numbers import Real
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from celery import Celery
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask import request, jsonify
import time
from datetime import datetime


# db = create_engine('postgresql+psycopg2://jjjvxftvljouqa:a41a7e3069600c2daa7ed7e917e26216fbd28f517719f517c4529b994bb8e430@ec2-34-248-169-69.eu-west-1.compute.amazonaws.com:5432/dfmbp1l6kre1rn')
# db = create_engine('postgresql+psycopg2://fuvnjouopjkqjz:457d26bac4530137e6f5fe1cf70d0b89ce4a9659c00fc076186ba123329495db@ec2-99-81-137-11.eu-west-1.compute.amazonaws.com:5432/dffjdini6butuh')
# create the app
app = Flask(__name__)

CORS(app, supports_credentials=True, allow_headers=True)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# base = declarative_base()

# Session = sessionmaker(db)
# session = Session()


# ma = Marshmallow(app)

# @app.cli.command('db_create')
# def db_create():
#     base.metadata.create_all(db)
#     print('Database created')
#     return 'Database created'

# @app.route("/db_create")
# def db_create_all():
#     base.metadata.create_all(db)
#     return 'Database created'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/jsn")
def jsn():
    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann","Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
        }
    return json.dumps(x)

@app.route("/quiz")
def quiz():
    x = {"question_arr":["\u0412 \u043a\u0430\u043a\u043e\u043c \u0433\u043e\u0434\u0443 \u043e\u0441\u043d\u043e\u0432\u0430\u043d \u0425\u0430\u0440\u044c\u043a\u043e\u0432\u0441\u043a\u0438\u0439 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442?","\u041a\u043e\u0433\u0434\u0430 \u0434\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0412.\u041d. \u041a\u0430\u0440\u0430\u0437\u0438\u043d\u0430?","\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0432\u0430\u0440\u0438\u0430\u043d\u0442 \u0430","\u041f\u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043e\u0442\u0432\u0435\u0442 \u0432"],"a1_arr":["1804","09.02","\u0430","\u0430"],"a2_arr":["1805","10.02","\u0431","\u0431"],"a3_arr":["1933","12.09","\u0432","\u0432"],"a4_arr":["1993","09.10","\u0433","\u0433"],"answer_arr":["1804","10.02","\u0430","\u0432"],"n_right_answer_arr":["1","2","1","3"]}
    return  jsonify(data=x), 202


@app.route("/tmpl")
def tmpl_out():
    return_message = "Send fetch"
    # return return_message
    return render_template('tmpl.html',text = return_message)