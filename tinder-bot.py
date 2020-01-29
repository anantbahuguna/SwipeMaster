from selenium import webdriver
from time import sleep

from secrets import username,password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com")

        sleep(5)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        #save the base window
        base_window = self.driver.window_handles[0]

        #switch to popup window
        popup = self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        
        #switch back to base window after popup window closes
        self.driver.switch_to_window(base_window)

        sleep(3)

        location_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        location_popup.click()
        sleep(1)
        notify_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notify_popup.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()



    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while(True):
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()


    #close the "add tinder to home screen" popup
    def close_popup(self):
        home_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[1]')
        home_popup.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('')
        match_popup.click()



bot = TinderBot()
bot.login()