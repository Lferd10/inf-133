from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def find_student(self, id):
        return next(
            (estudiante for estudiante in estudiantes if estudiante["id"] == id),
            None,
        )

    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path == "/estudiantes":
            if "apellido" in query_params:
                nombre = query_params["apellido"][0]
                estudiantes_filtrados = [
                    estudiante
                    for estudiante in estudiantes
                    if estudiante["apellido"] == nombre
                ]
                if estudiantes_filtrados != []:
                    self.response_handler(200, estudiantes_filtrados)
                else:
                    self.response_handler(204, [])
            else:
                self.response_handler(200, estudiantes)

        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id)
            if estudiante:
                self.response_handler(200, [estudiante])
            else:
                self.response_handler(204, [])

        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_POST(self):
        if self.path == "/estudiantes":
            data = self.read_data()
            data["id"] = len(estudiantes) + 1
            estudiantes.append(data)
            self.response_handler(201, estudiantes)

        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id)
            data = self.read_data()
            if estudiante:
                estudiante.update(data)
                self.response_handler(200, [estudiantes])
            else:
                self.response_handler(404, {"Error": "Estudiante no encontrado"})
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_DELETE(self):
        if self.path == "/estudiantes":
            estudiantes.clear()
            self.response_handler(200, estudiantes)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()





# from http.server import HTTPServer, BaseHTTPRequestHandler
# import json

# estudiantes = [
#     {
#         "id": 1,
#         "nombre": "Pedrito",
#         "apellido": "García",
#         "carrera": "Ingeniería de Sistemas",
#     },
# ]


# class RESTRequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == "/estudiantes":
#             self.send_response(200)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
#         elif self.path.startswith("/estudiantes/"):
#             id = int(self.path.split("/")[-1])
#             estudiante = next(
#                 (estudiante for estudiante in estudiantes if estudiante["id"] == id),
#                 None,
#             )
#             if estudiante:
#                 self.send_response(200)
#                 self.send_header("Content-type", "application/json")
#                 self.end_headers()
#                 self.wfile.write(json.dumps(estudiante).encode("utf-8"))

#         else:
#             self.send_response(404)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

#     def do_POST(self):
#         if self.path == "/estudiantes":
#             content_length = int(self.headers["Content-Length"])
#             post_data = self.rfile.read(content_length)
#             post_data = json.loads(post_data.decode("utf-8"))
#             post_data["id"] = len(estudiantes) + 1
#             estudiantes.append(post_data)
#             self.send_response(201)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps(estudiantes).encode("utf-8"))

#         else:
#             self.send_response(404)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

#     def do_PUT(self):
#         if self.path.startswith("/estudiantes"):
#             content_length = int(self.headers["Content-Length"])
#             data = self.rfile.read(content_length)
#             data = json.loads(data.decode("utf-8"))
#             id = data["id"]
#             estudiante = next(
#                 (estudiante for estudiante in estudiantes if estudiante["id"] == id),
#                 None,
#             )
#             if estudiante:
#                 estudiante.update(data)
#                 self.send_response(200)
#                 self.send_header("Content-type", "application/json")
#                 self.end_headers()
#                 self.wfile.write(json.dumps(estudiante).encode("utf-8"))
#         else:
#             self.send_response(404)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

#     def do_DELETE(self):
#         if self.path == "/estudiantes":
#             self.send_response(200)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()
#             estudiantes.clear()
#             self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
#         else:
#             self.send_response(404)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))


# def run_server(port=8000):
#     try:
#         server_address = ("", port)
#         httpd = HTTPServer(server_address, RESTRequestHandler)
#         print(f"Iniciando servidor web en http://localhost:{port}/")
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         print("Apagando servidor web")
#         httpd.socket.close()


# if __name__ == "__main__":
#     run_server()