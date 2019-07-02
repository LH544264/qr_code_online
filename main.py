import io
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
    
@app.route("/qr")
def qr():
    data = flask.request.args.get("data")

    img = qrcode.make(data)
    bi = io.BytesIO() # 创建一个BytesIO对象，用于在内存中存储二维码图像数据
    img.save(bi, "png") # 调用img对象的save方法将二维码图像数据以PNG编码格式写入bi对象管理的内存空间

    # img.save(r"C:\Users\Administrator\Desktop\Python\qrcode_tool_online\static\qr.jpg")
    # return '<img src="/static/qr.jpg"/>'
    bi.seek(0)  # 将bi对象内部指针移动到图像数据的起始位置

    # 返回二维码图像数据
    return flask.send_file(bi, "image/png")

if __name__ == '__main__':
    app.run(debug=True)