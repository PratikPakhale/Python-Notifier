import requests
from bs4 import BeautifulSoup
import time
from pushbullet import PushBullet

url = "https://josaa.nic.in/WebInfo/Page/Page?PageId=1&LangId=P"
access_token = "o.s41tTc9xuYWUBuDD2Ic2dDcISovBSPhY"
keyword = "Round 5"
sleep_time = 60

pb = PushBullet(access_token)
count = 1

while True:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    button = soup.find('a', attrs={'class': 'btn'})
    text = button.text
    file = open('data.txt', 'w')
    if keyword in text:
        push = pb.push_note(keyword, 'Gotcha!')
        break
    else:
        file.write('Current Count: '+str(count))
    time.sleep(sleep_time)
    count += 1


# file = open('data.txt', 'w')
# file.write(text)
# file.close()

# push = pb.push_note('Round 6 ', 'Result out')
