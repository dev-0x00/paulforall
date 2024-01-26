import requests
import time
from requests.auth import HTTPProxyAuth
from colorama import Fore

#internal imports
from voter.helpers import get_proxy_queue, get_useragent_queue



def main():
    proxy_queue = get_proxy_queue()
    while not proxy_queue.empty():
        proxy = proxy_queue.get()
        proxy_details =  {
            "address": proxy["address"], 
            "port": int(proxy["port"]), 
            "username": proxy["username"], 
            "password": proxy["password"]
        }
        
        # Setup proxy
        proxies = {
            "http": f"http://{proxy_details['address']}:{proxy_details['port']}",
            "https": f"http://{proxy_details['address']}:{proxy_details['port']}",
        }
        auth = HTTPProxyAuth(proxy_details['username'], proxy_details['password'])

        # Headers
        user_agent_queue = get_useragent_queue()
        user_agent = user_agent_queue.get()
        user_agent_queue.put(user_agent)
        
        headers = {
            "Content-Type": "application/json",
            "User-Agent": user_agent
        }

        # Session
        session = requests.Session()
        try:
            print(Fore.GREEN + "[INFO]: Using proxy: " + proxy_details['address'] + ":" + str(proxy_details['port']))
            url = "https://api.pollforall.com/api/v2/aggregate/poll"
            payload = {
                "pollId": "pk789z6m",
                "requesterDetails" : {}
            }

            response = session.post(url, headers=headers, proxies=proxies, auth=auth, data=payload)
            if response.status_code == 200:
                print(response)

            else:
                print(f"Failed to send request: {response.text}")
            time.sleep(5) 

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
