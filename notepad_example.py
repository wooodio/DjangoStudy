import urllib.request

print(urllib.request.urlopen('http://www.google.com').read().decode('utf-8'))
