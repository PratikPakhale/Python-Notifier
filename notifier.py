import base64
import requests
from pushbullet import PushBullet

access_token = "o.s41tTc9xuYWUBuDD2Ic2dDcISovBSPhY"

pb = PushBullet(access_token)

push = pb.push_note('Round 6 ', 'Result out')
