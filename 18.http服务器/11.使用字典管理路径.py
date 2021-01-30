from wsgiref import simple_server
from wsgiref.simple_server import make_server
import json


def load_file(file_name, **kwargs):
    try:
        with open('./pages/' + file_name,encoding='utf8') as file:
            content = file.read()
            if kwargs:
                content = content.format(**kwargs)
            return content
    except FileNotFoundError:
        print('文件没有找到')


def show_test():
    return json.dumps({'name': 'zhangsan', 'age': 18})

def show_demo():
    return  load_file('xxx.txt')
def index():
    return '欢迎来到我的首页'
def show_info():
    return  load_file('info.html').format(username='张三')
def show_foo():
    return  '我是foo'


url = {
    '/':index,
    '/test':show_test,
    '/demo':show_demo,
    '/info':show_info,
    '/foo': show_foo #新添加的
}

def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    status_code = '200 OK'
    method = url.get(path)
    if method:
        response = method()
    else:
        status_code = '404 Not Found'
        response = '页面丢了'

    start_response(status_code, [('Content-Type', 'text/plain; charset=utf-8'), ])
    return [response.encode('utf8')]  # 浏览器显示的内容


if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户请求
    with make_server('', 9999, demo_app) as httpd:
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        import webbrowser

        # 作用是打开电脑的浏览器，并在浏览器输入http://localhost:8000/xyz?abc
        webbrowser.open('http://localhost:9999/xyz?abc')

        # 处理一次请求
        # httpd.handle_request()  # serve one request, then exit
        httpd.serve_forever()  # 在后台一直运行
