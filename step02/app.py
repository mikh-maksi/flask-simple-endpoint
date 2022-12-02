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
            n = request.args.get('n')
    return str(n)



if __name__ == '__main__':
    app.run()