import flask 
import qrcode
from flask import render_template

app = flask.Flask(__name__)

@app.route("/")
def test():
    # # 第一步：获取要生成二维码的数据
    # data = flask.request.args.get("data")

    # # 第二步：生成二维码图像
    # img = qrcode.make(data)
    # img.save(r"C:\Users\Administrator\Desktop\Python\qrcode_tool_online\static\qr.jpg")

    # # 第三步：在页面上显示
    # return '<img src="/static/qr.jpg"/>' 
    return flask.render_template('hello.html')
    
@app.route("/qr", methods=["POST"])
def qr():
    data = flask.request.form.get("data")
    img = qrcode.make(data)
    img.save(r"C:\Users\Administrator\Desktop\Python\qrcode_tool_online\static\qr.jpg")
    return '<img src="/static/qr.jpg"/>'

if __name__ == '__main__':
    app.run(debug=True)