from wsgiref import simple_server
from wsgiref.simple_server import make_server

def demo_app(environ,start_response):
    path = environ['PATH_INFO']
    #状态码
    # 2xx 请求成功
    # 3xx 重定向
    # 4xx  客户端错误
    # 5xx 服务器内部错误
    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = '欢迎来到test页面'
    elif path == '/demo':
        response = '欢迎来到demo页面'
    else:
        status_code = '404 Not Found'
        response = '页面丢了'


    start_response(status_code, [('Content-Type','text/plain; charset=utf-8'),])
    return [response.encode('utf8')]  #浏览器显示的内容


if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户请求
    with make_server('', 8080, demo_app) as httpd:
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        import webbrowser

        # 作用是打开电脑的浏览器，并在浏览器输入http://localhost:8000/xyz?abc
        webbrowser.open('http://localhost:8080/xyz?abc')

        # 处理一次请求
        # httpd.handle_request()  # serve one request, then exit
        httpd.serve_forever() #在后台一直运行