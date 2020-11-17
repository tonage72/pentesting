#!/usr/bin/env python3

import socket
import os
import sys
from optparse import OptionParser

options = OptionParser(usage='%prog pyCat <MODE> <OPTIONS>', description='Choose pyCat client or server mode and connectivity options (IP PORT)')
options.add_option('-c', '--client', help='ex: pyCat -c 10.0.0.10 9999')
options.add_option('-s', '--server', help='ex: pyCat -s 0.0.0.0 9999')


def serv():
    HOST = sys.argv[2]
    PORT = int(sys.argv[3])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('~pyCat Server~ is RUNNING ')
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(65536).decode()
                if data == 'quit 2>&1':
                    exit()
                out1 = os.popen(data).read().encode()
                conn.sendall(out1)


def sender():
    RHOST = sys.argv[2]             # The server's hostname or IP address
    RPORT = int(sys.argv[3])        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((RHOST, RPORT))
        while True:
            stderr = (' 2>&1')
            userin = input('~pyCat Client~$ ')
            cmds = (userin + stderr).encode()
            s.sendall(cmds)
            data = s.recv(65536)
            print (data.decode())
            callback()

def callback():
    sender()


def main():
    opts, args = options.parse_args()
    if len(args) < 1:
        options.print_help()
        return
    else:
         if sys.argv[1] == '-c' or sys.argv[1] == '--client':
             callback()
         elif sys.argv[1] == '-s' or sys.argv[1] == '--server':
             serv()
         else:
             print('There was an error')
             exit()

main()
