from socket import *
from threading import *
from random import randint
import json

def switch_case(data):
    method = data.get("method", "").lower()
    num1 = data.get("Tal1")
    num2 = data.get("Tal2")

    if method == "random":
        if num1 is None or num2 is None:
            return {"error": "Invalid input. Missing required fields."}
        try:
            random_num = randint(num1, num2)
            return {"result": random_num}
        except ValueError:
            return {"error": "Invalid input. Please enter two valid numbers."}
    elif method == "add":
        if num1 is None or num2 is None:
            return {"error": "Invalid input. Missing required fields."}
        try:
            add_num = num1 + num2
            return {"result": add_num}
        except ValueError:
            return {"error": "Invalid input. Please enter two valid numbers."}
    elif method == "subtract":
        if num1 is None or num2 is None:
            return {"error": "Invalid input. Missing required fields."}
        try:
            sub_num = num1 - num2
            return {"result": sub_num}
        except ValueError:
            return {"error": "Invalid input. Please enter two valid numbers."}
    else:
        return {"error": "Unknown method."}

def handleClient(connectionSocket, address):
    while True:
        try:
            data = connectionSocket.recv(1024).decode()
            data = json.loads(data)
            response = switch_case(data)
            connectionSocket.send(json.dumps(response).encode())
        except json.JSONDecodeError:
            connectionSocket.send(json.dumps({"error": "Invalid JSON format."}).encode())
        except Exception as e:
            connectionSocket.send(json.dumps({"error": str(e)}).encode())
            break
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    Thread(target=handleClient, args=(connectionSocket, addr)).start()