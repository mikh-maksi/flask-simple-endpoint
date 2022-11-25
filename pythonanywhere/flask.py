from flask import Flask
import json
from flask import request, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!!'



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

if __name__ == '__main__':
    app.run()