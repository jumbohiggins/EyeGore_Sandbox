import requests
import json
import os


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


#cs = CharScrape()
#ven = cs.CharScrape("https://www.dndbeyond.com/profile/Venificus/characters/2113653/json")
