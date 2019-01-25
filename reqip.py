#conding=utf-8
from flask import Flask, render_template, request
from flask import make_response
# Initialize the Flask application
app = Flask(__name__)
# Default route, print user's IP
@app.route('/ip')
def indexx():
    # response = make_response(render_template('index.html', foo=42))
    # response.set_cookie('name','davidszhou')
    # return response

    ip = request.remote_addr
    name = request.cookies.get('name')  # 获取cookie
    print(request.cookies)
    ua=request.headers.get('User-Agent')
    response=str(ip)+"\n"+str(ua)+str(name)
    if name==None:

        response = make_response(response)
        response.set_cookie('name', 'davidszhou')
    # r.set_cookie('name', '', expires=0)#删除

    return response
@app.route('/')
def index():
    ip = request.remote_addr
    ua=request.headers.get('User-Agent')
    # r=str(ip)+str(ua)
    a="aaa"
    return a
if __name__ == '__main__':
    app.run(   host="0.0.0.0", port=81,debug=True )