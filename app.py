from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    try:
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        print("iniciando servidor web en http://localhost:8000/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('apagando servidor web')
        httpd.socket.close()


if __name__ == "_main_":
    run()