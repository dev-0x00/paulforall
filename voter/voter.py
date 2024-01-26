#local imports 
from browser.browser import create_browser

#external imports
from colorama import Fore
import time, random
from anticaptchaofficial.recaptchav2proxyless import *

#selenium imports 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By

class Voter:

    def __init__(self, proxy, user_agent) -> None:
        self.browser = create_browser(proxy=proxy, user_agent=user_agent)
        self.proxy = proxy
        print(Fore.GREEN + "[INFO]: Using proxy: " + proxy)
        self.wait = WebDriverWait(self.browser, 10)

    def voting_steps(self):
        #get the voting url
        url = "https://pollforall.com/pk789z6m"
        self.browser.get(url)
        time.sleep(random.randint(2, 5))
       
        try:
            self.accept_cookies()
            iframe = self.wait.until(Ec.frame_to_be_available_and_switch_to_it((By.ID, "iframe")))
            self.browser.switch_to.frame(iframe)
        
        except:
            pass

        try:
            yes_button = self.wait.until(Ec.presence_of_element_located((
                By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div[4]"
            )))
        
        except Exception as Error:
            yes_button = self.wait.until(Ec.presence_of_element_located((
                By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div[3]/div[1]"
            )))
            
        yes_button.click()
        time.sleep(random.randint(2, 5))

        try:
            submit_button = self.wait.until(Ec.presence_of_element_located((
                By.XPATH, "//div[@aria-label='submit vote']"
            )))
            self.browser.execute_script("arguments[0].click();", submit_button)
            time.sleep(random.randint(2, 5))

            agree_button = self.wait.until(Ec.presence_of_element_located((
                By.XPATH, "//button[contains(., 'I agree') and @type='button']"
            )))
            self.browser.execute_script("arguments[0].click();", agree_button)
            solve_captha = Captcha()
            is_solve = solve_captha.solve_captcha(self.browser)
            
            if is_solve:
                yes_votes, no_votes = self.get_current_votes()
                print(Fore.YELLOW + "[INFO]: Upvotes At: " + yes_votes)
                print(Fore.YELLOW + "[INFO]: Downvotes At: " + no_votes)
                return True

            else:
                return self.proxy
            
        
        except Exception as Error:
            print(Fore.RED + "[ERROR]: Failed to vote: " + self.proxy)
            print(Fore.RED + "[ERROR]: " + Error)
            self.browser.quit()
            return self.proxy
    
    def get_current_votes(self):
        time.sleep(random.randint(3, 5))
        yes_votes_element = self.wait.until(Ec.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div"
        )))

        no_votes_element = self.wait.until(Ec.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[4]/div[2]/div[1]/div[2]/div"
        )))
        yes_votes = yes_votes_element.get_attribute("innerHTML")
        no_votes = no_votes_element.get_attribute("innerHTML")

        return yes_votes, no_votes

    def accept_cookies(self):
        cookie_button = self.wait.until(Ec.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]"
        )))

        self.browser.execute_script("arguments[0].click();", cookie_button)
        time.sleep(random.randint(1, 3))

class Captcha:
    def __init__(self) -> None:
        self.solver = recaptchaV2Proxyless()
        self.solver.set_verbose(1)
        self.solver.set_website_key = "6LfEY_MiAAAAAH9z6OJAmlOgo9psagdAQh4kyVdS"
        self.solver.set_website_url = "https://pollforall.com/pk789z6m"
        self.solver.set_key = "token"

    def get_tokens(self) -> str:
        print(Fore.GREEN + "[INFO]:  Solving captcha ...")
        g_response = self.solver.solve_and_return_solution()
        if g_response != 0:
            return g_response
        else:
            print(Fore.RED + "[ERROR]: " + self.solver.error_code)
            return ""
            
    def solve_captcha(self, driver) -> bool:
        try:
            code = self.get_tokens()
            driver.execute_script(f'document.getElementsByName("g-recaptcha-response")[0].value = "{code}";')
            driver.execute_script(f'___grecaptcha_cfg.clients[0].T.T.callback("{code}");')
            return True
        
        except:
            return False

        