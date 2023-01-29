import argparse
from http.server import HTTPServer
from src.calculator.Calculator import Calculator
from src.user_interface.UserInterface import UserInterface
from src.user_interface.ServerInterface import ServerInterface
from tkinter import *

import sys

if(len(sys.argv) < 2):
    ui = UserInterface(True)
elif(sys.argv[1] == "web"):
    server_class=HTTPServer
    handler_class=ServerInterface
    addr="localhost"
    port=8000
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()
else:
    calculator = Calculator()
    print(calculator.calculate(sys.argv[1]))