#!/usr/bin/env python3

import asyncio
import socket
import sys
from pathlib import Path

# class LiquidsoapSocket:
#     path: Path
#     sock: socket.socket

#     def __init__(self, path: Path):
#         self.path = path
#         self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

#     def connect(self):
#         self.sock.connect(str(self.path))

#     def send(self, msg: str):
#         self.sock.sendall(msg.encode(encoding="utf-8"))

#     def read(self):
#         chunks = []
#         while True:
#             chunk = self.sock.recv(1024)
#             print(chunk)
#             if len(chunk) == 0:
#                 break
#             chunks.append(chunk)
#         return b"".join(chunks)


# def run():
#     sock = LiquidsoapSocket(path=Path("./liquidsoap.sock"))
#     try:
#         sock.connect()
#         sock.send("help\n")
#         print(sock.read())
#         sock.send("exit\n")

#     except socket.error as msg:
#         print(msg)
#         sys.exit(1)


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_unix_connection("./liquidsoap.sock")

    writer.write(message.encode())
    await writer.drain()

    data = await reader.readuntil(b"END")
    print(data.decode(encoding="utf-8"))

    writer.write(b"exit\n")
    await writer.drain()
    await reader.read()

    writer.close()
    await writer.wait_closed()


asyncio.run(tcp_echo_client("help\n"))
asyncio.run(tcp_echo_client("var.set use_queue1 = true\n"))
asyncio.run(tcp_echo_client("var.get use_queue2\n"))
asyncio.run(tcp_echo_client("var.set use_queue2 = false\n"))
asyncio.run(tcp_echo_client("var.get use_queue2\n"))
asyncio.run(tcp_echo_client("var.set use_queue2 = 'hello'\n"))
asyncio.run(tcp_echo_client("var.get use_queue2\n"))
asyncio.run(tcp_echo_client("var.set use_queue2 = true\n"))
asyncio.run(tcp_echo_client("var.get use_queue2\n"))
