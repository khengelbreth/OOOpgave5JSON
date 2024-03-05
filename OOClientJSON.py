from socket import *
import json

def main():
    method = input("Enter method ('random', 'add' or 'subtract'): ").lower()
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    data = {"method": method, "Tal1": num1, "Tal2": num2}
    try:
        serverName = "localhost"
        serverPort = 12000
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(json.dumps(data).encode())
        response = clientSocket.recv(1024).decode()
        print('From server:', response)
        clientSocket.close()
    except Exception as e:
        print("Error:", e)


main()