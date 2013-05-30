realgar
=======

A Simple Web Framework to learn python


WSGI API
========
* implemented as a callable object: a function, a method, a class or a instance with a __call__ method
* paramaters:
    * dict containing CGI like variables
    * a callback function will be used by the application to send HTTP status code/message and HTTP headers to the server
* return response body to the server as strings wrapped in an iterable.
* GET:	escape( parse_qs( environ['QUERY_STRING'] ) )
* POST:	escape( parse_qs( environ['wsgi.input'].read( int(environ.get('CONTENT_LENGTH', 0)) ) ) )
References
========
* http://wsgi.readthedocs.org/en/latest/learn.html
    * http://webpython.codepoint.net/wsgi_application_interface
* http://anandology.com/blog/how-to-write-a-web-framework-in-python/
