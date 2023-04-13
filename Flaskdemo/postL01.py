from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    print("收到请求 ")
    if request.method == 'POST':
        result = request.form
        print(result)
        return 'Hello World'
    return 'Hello World'

if __name__ == '__main__':
    app.run(port=8089,debug = True)


