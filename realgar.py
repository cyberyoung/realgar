from wsgiref.simple_server import make_server

def app(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return ['Hello Wrold']

if __name__ == '__main__':
    #from paste import httpserver
    #httpserver.serve(app, host='127.0.0.1', port='8080')
    httpd = make_server('localhost', 8888, app)
    httpd.handle_request()
