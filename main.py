from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>我的GAE实验</title>
    </head>
    <body>
        <h1>我的第一个GAE应用</h1>
        <p><strong>项目ID：</strong>massive-cider-475900-h9</p>
        <p><strong>技术栈：</strong>Python + Flask + GAE</p>
        <p>云计算与分布式系统 - 实验2</p>
        <p>部署状态：成功</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)