from datetime import datetime
import time, os, requests

url = 'https://www.google.com/'
timeout = 2
sleep_time = 10
op = None


now = datetime.now()
try:
        op = requests.get(url, timeout=timeout).status_code
        if op == 200:
            p="Connected"
        else:
            print("Status Code is not 200")
            print("status Code", op)
except:
        p="Not Connected"
        # print("status Code", op)
        # sleep_time = 5
print(p)

if p=="Connected":
    print('ra')
elif p=="Not Connected":
    print('plund')