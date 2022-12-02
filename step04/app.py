from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!!'


@app.route("/quiz",methods=['GET'])
def quiz():
    if request.method == "GET":
        if request.args.get('n') == None:
            n = 0
        else:
            n = int(request.args.get('n'))
    answer=''
    answer_arr = ['null','one','two','three']
    quiz_arr=[]
    quiz_arr.append({"question_arr":["\u0412 \u043a\u0430\u043a\u043e\u043c \u0433\u043e\u0434\u0443 \u043e\u0441\u043d\u043e\u0432\u0430\u043d \u0425\u0430\u0440\u044c\u043a\u043e\u0432\u0441\u043a\u0438\u0439 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442?"],"title_arr":["\u0413\u043e\u0434 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u0425\u0430\u0440\u044c\u043a\u043e\u0432\u0441\u043a\u043e\u0433\u043e \u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0430!"],"a1_arr":["1804"],"a2_arr":["1805"],"a3_arr":["1933"],"a4_arr":["1993"],"answer_arr":["1804"],"n_right_answer_arr":["1"],"total_n":"4"})
    quiz_arr.append({"question_arr":["\u041a\u043e\u0433\u0434\u0430 \u0434\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0412.\u041d. \u041a\u0430\u0440\u0430\u0437\u0438\u043d\u0430?"],"title_arr":["\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f"],"a1_arr":["09.02"],"a2_arr":["10.02"],"a3_arr":["12.09"],"a4_arr":["09.10"],"answer_arr":["10.02"],"n_right_answer_arr":["2"],"total_n":"4"})
    quiz_arr.append({"question_arr":["\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0432\u0430\u0440\u0438\u0430\u043d\u0442 \u0430"],"title_arr":["\u041f\u0440\u043e\u0441\u0442\u043e \u0432\u043e\u043f\u0440\u043e\u0441"],"a1_arr":["\u0430"],"a2_arr":["\u0431"],"a3_arr":["\u0432"],"a4_arr":["\u0433"],"answer_arr":["\u0430"],"n_right_answer_arr":["1"],"total_n":"4"})
    quiz_arr.append({"question_arr":["\u041f\u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043e\u0442\u0432\u0435\u0442 \u0432"],"title_arr":["\u041a\u0430\u043a\u043e\u0439-\u0442\u043e \u0432\u043e\u043f\u0440\u043e\u0441"],"a1_arr":["\u0430"],"a2_arr":["\u0431"],"a3_arr":["\u0432"],"a4_arr":["\u0433"],"answer_arr":["\u0432"],"n_right_answer_arr":["3"],"total_n":"4"})
    
    if n<len(quiz_arr):
        answer = quiz_arr[n]
    else:
        answer="Over"

    return answer



if __name__ == '__main__':
    app.run()