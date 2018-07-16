import requests
from bs4 import BeautifulSoup
import time
import smtplib

class Course_alert():
    '''
      Check for the Dal QA course seats. If there are seats available then trigger an email alert.
    '''

    def __init__(self,url):
        self.url = url

    def send_email(self,no_of_seats):
        message = 'Subject: Hey QA has' + no_of_seats + ' seats available'
        fromaddress = 'mariavinoth619@yahoo.com'
        toaddress = 'vinoth@dal.ca'
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        # server.set_debuglevel(0)
        server.starttls()
        server.login("mariavinoth619@yahoo.com", "")
        server.sendmail(fromaddress, toaddress, message)
        server.quit()
        print("Alert email sent!")

    def check_seats(self):
        uClient = requests.get(self.url)
        soup = BeautifulSoup(uClient.content, 'lxml')
        containers = soup.find_all('td')
        for i in range(len(containers)):
            if (containers[i].find(text='32009')):
                if (self.check_avalability(containers[i + 14].text)):
                    # self.send_email(containers[i + 14].text)
                    print((containers[i + 14].text) + ' Seats available')
                    break;

    def check_avalability(self,no_of_seats):
        if int(no_of_seats) > 0:
            print("seats available")
            return True
        else:
            time.sleep(120)
            self.check_seats()


if __name__ == '__main__':
    url = "https://dalonline.dal.ca/PROD/fysktime.P_DisplaySchedule?s_term=201830&s_crn=&s_subj=CSCI&s_numb=&n=1&s_district=100"
    ca = Course_alert(url)
    ca.check_seats()

