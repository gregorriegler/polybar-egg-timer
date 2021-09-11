#!/usr/bin/env python3
import argparse
import socket

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['toggle_play', 'reset', 'toggle_loop', 'longer', 'shorter', 'quit'])
    parser.add_argument("-host", default='127.0.0.1', help="Host where the control sends commands to. Default: '127.0.0.1'")
    parser.add_argument("-p", "--port", type=int, default=65441, help="Port on which the control sends commands (int). Default: 65441")
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.host, args.port))
        s.sendall(bytearray(args.command, 'utf-8'))





