# [20/Oct/2021 09:13:30] "POST /sendmessage HTTP/1.1" 400 63890

from flask import Flask, render_template, request
from flask_cors import CORS


app = Flask(__name__)
# CORS(app,  resources={r"/*": {"origins": "*"}})   # 允许所有域名跨域
CORS(app, supports_credenrials = True)


@app.route('/')
def student():
    return "Holeele"

@app.route('/sendmessage',methods = ['POST', 'GET'])
def sendmessage():
    if request.method == 'POST':
        result = request.form
        return "sendmessage 123"



if __name__ == '__main__':
    app.run(debug = True)






