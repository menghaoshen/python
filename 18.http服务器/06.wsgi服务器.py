from wsgiref import simple_server
from wsgiref.simple_server import make_server

#demo_app 需要两个参数
#0个是参数，表示环境（电脑的环境，请求路径相关的环境）
# 第一个参数，是一个函数，用来返回响应头
# 这个函数需要一个返回值，返回值是一个列表，列表里只有一个元素，是个二进制，表示返回给浏览器的内容
# environ 是一个字典，报错了很多数据
# 其中重要的是PATH_INFO 能够获取到用户的访问路径
def demo_app(environ,start_response):
    path = environ['PATH_INFO']
    print('path={}'.format(path))
    start_response("200 OK", [('Content-Type','text/plain; charset=utf-8'),('sss','dddd')]) #自己定义的头信息
    return ['hello'.encode('utf8')]  #浏览器显示的内容


if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户请求
    with make_server('', 8000, demo_app) as httpd:
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        import webbrowser

        # 作用是打开电脑的浏览器，并在浏览器输入http://localhost:8000/xyz?abc
        webbrowser.open('http://localhost:8000/xyz?abc')

        # 处理一次请求
        # httpd.handle_request()  # serve one request, then exit
        httpd.serve_forever() #在后台一直运行