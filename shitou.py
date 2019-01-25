from flask import Flask ,redirect,render_template
import json
app=Flask(__name__,static_folder="template_folder='../templates",)

@app.route('/')
@app.route('/index')
def index():
    s=['张三','年龄','姓名']
    t={}
    t['data']=s
    # return json.dumps(t,ensure_ascii=False)
    # return "abc!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    return render_template('b.html')

if __name__ == "__main__":
    app.run(port=82,debug=True)