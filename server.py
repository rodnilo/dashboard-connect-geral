from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 1234)
    httpd = server_class(server_address, handler_class)
    print("Servidor rodando em http://localhost:1234")
    webbrowser.open('http://localhost:1234')
    httpd.serve_forever()

if __name__ == '__main__':
    run() 