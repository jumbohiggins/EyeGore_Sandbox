import requests
import json
import os
import Helpers as hlp
import urllib3
from bs4 import BeautifulSoup


class CharScrape(object):

    def __init__(self):
        self.name = "CharDat"

    def CharScrape(self, url):

        #print(1)
        #print("Fatty")
        #print(url)
        data = requests.get(url).json()
        #print(3)
        binary = json.dumps(data)
        #print(4)
        output = json.loads(binary)
        #print(5)
        return(output)


    def SaveCharScrape(self, ScrapeObj):

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        mexxy = (json.dumps([ScrapeObj], sort_keys=True, indent=4, separators=(',', ': ')))
        output_path = os.path.join(__location__, ScrapeObj['name'] + '__CharData.CDF')

        with open(output_path, 'w') as f:
            f.write(mexxy)

    def BasicScrape(self, urlid):
        hp = hlp.Helpers()
        http = urllib3.PoolManager()
        url = "https://www.dndbeyond.com/character/%s/json" % urlid
        response = http.request('Get', url)
        soup = BeautifulSoup(response.data, "html.parser")
        site_json = json.loads(soup.text)
        current_hp = int(site_json['baseHitPoints']) + hp.get_mod(int(site_json["stats"][2]["value"])) * hp.get_player_level(int(site_json['currentXp'])) - int(site_json['removedHitPoints'])
        print(current_hp)


numslist = 4741434, 15473396, 10428007, 15636899, 10648918
cs = CharScrape()
for each in numslist:
    cs.BasicScrape(each)


#ven = cs.CharScrape("https://www.dndbeyond.com/profile/Venificus/characters/2113653/json")
