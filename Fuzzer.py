#!/usr/bin/env python3

import socket

rhost=""
rport=

msg=b"\x41"*100
while True:
    print ("send"+str(len(msg)))
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rhost,rport))
    s.send(msg+b"\n")
    data=s.recv(1024)
    msg+=b"\x41"*100
