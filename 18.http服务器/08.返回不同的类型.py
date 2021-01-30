from wsgiref import simple_server
from wsgiref.simple_server import make_server
import  json

def demo_app(environ,start_response):
    path = environ['PATH_INFO']
    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name':'zhangsan','age':18})
    elif path == '/demo':

        with open('pages/xxx.txt', 'r', encoding='utf8') as file:
            response = file.read()
    elif path == '/info':
        # 查询数据库获取到用户名
        name = 'jack'
        with open('pages/info.html', 'r', encoding='utf8') as file:
            response = file.read().format(username=name)
    else:
        status_code = '404 Not Found'
        response = '页面丢了'

    start_response(status_code, [('Content-Type','text/plain; charset=utf-8'),])
    return [response.encode('utf8')]  #浏览器显示的内容


if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户请求
    with make_server('', 8089, demo_app) as httpd:
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        import webbrowser

        # 作用是打开电脑的浏览器，并在浏览器输入http://localhost:8000/xyz?abc
        webbrowser.open('http://localhost:8089/xyz?abc')

        # 处理一次请求
        # httpd.handle_request()  # serve one request, then exit
        httpd.serve_forever() #在后台一直运行