#import random
from colorama import Fore
from queue import Queue

PROXIES_LIST = [
        "185.199.228.220:7300",
        "185.199.231.45:8382",
        "188.74.210.207:6286",
        "188.74.183.10:8279",
        "188.74.210.21:6100",
        "45.155.68.129:8133",
        "154.95.36.199:6893",
        "45.94.47.66:8110"
    ]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 OPR/45.0.2552.898",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36",
]

def get_proxy_queue() -> Queue:
    proxies_queue = Queue()

    for proxy in PROXIES_LIST:
        address, port= proxy.split(":")
        proxy_details =  {
            "address": address, 
            "port": int(port), 
        }
        proxies_queue.put(proxy_details)
    return proxies_queue

def get_useragent_queue() -> Queue:
    agents_queue = Queue()

    for agent in USER_AGENTS:
       agents_queue.put(agent)
    return agents_queue