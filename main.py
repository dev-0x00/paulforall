#local imports
from voter.helpers import get_proxy_queue, get_useragent_queue
from voter.voter import Voter

from queue import Queue
from threading import Thread

def worker(proxy_queue: Queue, user_agent_queue: Queue):
    while not proxy_queue.empty():
        proxy = proxy_queue.get()
        agent = user_agent_queue.get()
        proxy = f"http://{proxy['address']}:{proxy['port']}"
        voter = Voter(proxy, agent)
        state = voter.voting_steps()

        if state != True:
            proxy_queue.put(state)
        
        user_agent_queue.put(agent)

def main():
    proxy_queue = get_proxy_queue()
    user_agent_queue = get_useragent_queue()
    
    #set number of threads to open concurently
    number_of_threads = 2
    threads = []

    for _ in range(number_of_threads):
        try:
            t = Thread(target=worker, args=(proxy_queue, user_agent_queue))
            t.start()
            threads.append(t)
        
        except:
            pass

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    main()