import socket       # Used for raw TCP communication
import re           # Used for regular expression matching(extract numbers from text)

HOST = "b3520df57bbdc554.247ctf.com"
PORT = 50118

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Creating a TCP socket, AF_INET indicates IPv4, SOCK_STREAM indicates TCP
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)         # Disable Nagle's algorithm for lower latency. Nagle's algorithm delays small packets to bundle them together for efficiency.
s.connect((HOST, PORT))                                

buffer = ""

while True:
    data = s.recv(4096)
    if not data:
        break

    buffer += data.decode(errors="ignore")

    # Solve immediately if question appears
    match = re.search(r"(\d+)\s*\+\s*(\d+)", buffer)
    if match:
        a, b = map(int, match.groups())
        answer = a + b
        s.sendall(f"{answer}\r\n".encode())
        buffer = ""

    # Print AFTER sending
    print(data.decode(errors="ignore"), end="", flush=True)

    if "flag" in buffer.lower():
        break

s.close()
