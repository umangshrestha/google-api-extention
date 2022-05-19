import requests
from pprint import pprint

URL = "http://127.0.0.1:8000/api/data/"
data = requests.get(
    URL, 
    headers={"Content-Type": "application/json"}, 
    data='{"start": 1, "end": 3}').json()
pprint(data)

# output
{'auth': [{'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
           'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
           'client_email': 'zadon-644@mineral-trainer-304110.iam.gserviceaccount.com',
           'client_id': '113599432147475183656',
           'client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/zadon-644%40mineral-trainer-304110.iam.gserviceaccount.com',
           'id': 2,
           'private_key': '-----BEGIN PRIVATE KEY-----\n'
                          'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCQYMjxtqMWmEPk\n'
                          'nJ3Ir8IgF7CiRQRB0k1jM5i/o+YEOFwma3/i6lwsc5dhtG+TYJ5p88lX5IfJuOO6\n'
                          'q7GrYnXMaAM4mZyCVTVOVwxfBsV7XxX+Hmzojv/CyWD4OAqZcoScgdp3kPeLGgcu\n'
                          'y4r6fmRBvZFMYTd5QcDyOgHmQ6RK3YCYCGj6dc5bZ64qUzD5lxmo3s/Rc/01ronz\n'
                          'eHrGmBKSVP2aq463WVd09ocRJtvkShEORlYlLBmfg/tSPpmVFf4p0t4uFfzf7vm2\n'
                          '8i/TgFiFfFtSvdrTH3yNSWP5RevOs7cjc3arXC8qFRoBYJjmexyMG9UGUDFB9Wss\n'
                          'uBDCle61AgMBAAECggEAAhSrALTJn+s820AYlApYaV7+CDCncY1m2R2mv2hMydXI\n'
                          'GjOlaa9H+coGrf1MOFsFnXBKgA5GmLUl7wxHaLloCjSbi0bHdydkN8dQYdQ2p2ME\n'
                          '7Z8hoa5h6Dw/vgQMvw5j8995NwzrTGFpJhb/30FQD5R8UhX6lzBH6BXG7jseVIfc\n'
                          'Jg4Jsiu7HVpDfcRb3VCPsrgD7onEhCrFE0OkrZpndlwZadbquYqSbdYHmh/feRP4\n'
                          'mAe3TTUl8GvGPu5of88+HpXwwtlwG52SObv3DZX1h3x4WmbebLhpce//05izmo+g\n'
                          'yntn4bi3ArKqQMaZJmCkftjHx6eS5dw7d3vlMyMogQKBgQDE+WcaPT4IWiVvQMIE\n'
                          'cyp1BwR+IjczC9rmO/U/orpMFSmltkybFRRlGykzpENmaVNSwfh/RDvVurBnzXhC\n'
                          's281BO297547EqpC4anSoNQbEchoDYXZ1fCmSciHP9wzjQiAvPas94YhNdFHutX1\n'
                          'iJj0JhZAYB27jtBgytrCXqzEdQKBgQC7pIrg6QLXvE+0ZrGp1dwse/wF6d07eh0G\n'
                          'xhb3CqMTqiVObBLoIDlMxL1Z43n/LvOUa+6dCB4qzbrduoj3jQVDblTWTmfG7+nS\n'
                          'iEE9M3uOgjQydUTKNtLomZMWBhxIYVFm4x0ljS+08LGbZ8jc1Zrob277ZF+S/YK7\n'
                          'lfEtldI5QQKBgB6e1tRRaO9LdD5TRtYCQTtoF96z2vjoguL/tyRpW6SwNYU5Tbde\n'
                          'E4mUK1eH1aJ6BSX8WXEPXm3fU8UPP/6+fi8z0PGR6nssb6NuCURhFBgRL6JdV82B\n'
                          'YKO5HJ9J4iVxazz4IzDIWeWXxCzucox067IoqZTgXD7n+KTTZCaLKThxAoGBAKXF\n'
                          'ZdPwxswk1x1/JDHwd4TtO+dVhldHOGGFm0BAq3Vx+Wdg3wsnfLevj8Db0Cl7J0HW\n'
                          'YIVmaJBUFGRSqTJZ6W57CIQT3GbKCP4v1cLluqBZsxdoto8XBBjtpB3u5AmlwC5v\n'
                          'Mo68PotRoPa0J6XBKAt0ds2tDSpkwJxMiTdGhuSBAoGAA1vv8U88a96z+bcUY1P5\n'
                          '2Z2S3KtPN5NWO6+nggvFeY8pmefrlH+HE2SSlndczt9wlLdsrV291Yt9xgon0LyO\n'
                          '6SvburOyj2QPZ5x3SAH5jlM4vfErJEL4ZwZBa5gHtoIWDGz2rmA/rxehlxsIlNL3\n'
                          'gnF8E1L/fxiPpa3mrzJEiqg=\n'
                          '-----END PRIVATE KEY-----\n',
           'private_key_id': '2e404831c6342d0a3c186d753e26f680ffb80874',
           'project_id': 'mineral-trainer-304110',
           'status': None,
           'token_uri': 'https://oauth2.googleapis.com/token',
           'type': 'service_account'}],
 'url': ['https://okomaps.com/us/raleigh/oyster-supplier-in-raleigh/westlake-ace-hardware-3974',
         'https://okomaps.com/us/raleigh/oyster-supplier-in-raleigh/westlake-ace-hardware-3971']}