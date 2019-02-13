
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = 'http://py4e-data.dr-chuck.net/comments_91328.xml'
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    
    tree = ET.fromstring(data)
    sum = 0
    counts = tree.findall('.//count')
    print('Count:',len(counts))
    for i in counts:
        sum = sum + int(i.text)
    print('sum:', sum)
