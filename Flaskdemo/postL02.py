from flask import Flask, render_template, request

app = Flask(__name__)
# api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  #或者，跨域。
  #response.headers['Access-Control-Allow-Origin']= '*'
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


@app.route('/')
def index():
    # data=request.file
    # file=data['file']
    # filename=file.filename
    # file.save(path)
    return 'Hello World'

if __name__ == '__main__':
    app.run(port=8089)