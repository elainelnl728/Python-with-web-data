import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    # url = 'http://py4e-data.dr-chuck.net/comments_91328.xml'
    print('Retrieving ', address)
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read().decode()
    print('Retrieved ', len(data), 'characters')
    print(data)
    info = json.loads(data)
    print('Count ', len(info['comments']))
    # print(json.dumps(info, indent=2))
    sum = 0
    for user in info['comments']:
        sum = sum + user['count']
    print('Sum: ', sum)
