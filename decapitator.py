import socket
import requests
import json

with open('data.json', 'r') as openfile:
    # Reading from json file 
    data = json.load(openfile)


# def connected():
#     if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
#         return False
#     else:
#         return True
def wait_for_internet_connection():
    while True:
        try:
            response = requests.get('http://google.com/',timeout=5)
            return
        except (requests.ConnectionError, requests.Timeout) as exception:
            pass


def send_data(key, info):
    if data['method'] == 'Dweet':
        r = requests.post(f'https://dweet.io/dweet/for/{data["access_code"]}?{key}={info}')
        print(r)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


wait_for_internet_connection()

# read the output of 'hostname -I'
ip = get_ip()

send_data('local_network', ip)
