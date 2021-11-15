import base64
import requests
from pushbullet import PushBullet

user = "PratikPakhale"
repo_name = "Python-Notifier"
path_to_file = "config.json"
url = 'https://api.github.com/repos/'+user + \
    '/'+repo_name+'/contents/'+path_to_file

access_token = "o.s41tTc9xuYWUBuDD2Ic2dDcISovBSPhY"

pb = PushBullet(access_token)

# print(url)
req = requests.get(url)
if req.status_code == requests.codes.ok:
    req = req.json()

    print(base64.b64decode(req['content']).decode('utf-8'))
else:
    print('Content was not found.')

# push = pb.push_note('Round 6 ', 'Result out')
