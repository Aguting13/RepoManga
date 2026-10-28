from http.server import SimpleHTTPRequestHandler, HTTPServer
import webbrowser

HOST = "localhost"
PUERTO = 8000


def iniciar_servidor():
    servidor = HTTPServer((HOST, PUERTO), SimpleHTTPRequestHandler)
    direccion = f"http://{HOST}:{PUERTO}/index.html"

    print("Café Cult está funcionando")
    print("Abrí en tu navegador:", direccion)
    print("Presioná Ctrl + C para detener el servidor")

    webbrowser.open(direccion)
    servidor.serve_forever()


if __name__ == "__main__":
    iniciar_servidor()
