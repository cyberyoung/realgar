from wsgiref.simple_server import make_server

def app(environ, start_response):
    response_body = ['%s: %s' %(k,v) for k,v in environ.items()]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [('content-type', 'text/plain'), 
                        ('content-length', str(len(response_body)))]
    
    start_response(status, response_headers)
    return [response_body]

if __name__ == '__main__':
    #from paste import httpserver
    #httpserver.serve(app, host='127.0.0.1', port='8080')
    httpd = make_server('localhost', 8888, app)
    httpd.serve_forever()
    #httpd.handle_request()
