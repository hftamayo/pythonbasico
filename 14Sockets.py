#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(HOST, PORT)

# para probar la conexion, en una terminal abro
#nc -nvlp 7777
#y desde otra: python3 socket.py
