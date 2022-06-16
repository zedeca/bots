import requests
def proxychecker():
  proxyfile = input('input proxies')
  f = open(proxyfile,'r')
  proxylist = f.readlines()
  print(proxylist)
  for proxy in proxylist:
    proxy = proxy.replace('\n', '')
    print(proxy)
    proxycheck = requests.get('https://whatismyipaddress.com/proxy-check')
    print(proxycheck)

proxychecker()