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
    if n<len(answer_arr):
        answer = answer_arr[n]
    else:
        answer="Over"

    return answer



if __name__ == '__main__':
    app.run()