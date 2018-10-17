import requests
import json
import os


class CharScrape(object):

    def __init__(self):
        self.name = "CharDat"

    def CharScrape(self, url):

        req = requests.get(url)

        data = req.json()
        binary = json.dumps(data)
        output = json.loads(binary)

        return(output)


    def SaveCharScrape(self, ScrapeObj):

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        mexxy = (json.dumps([ScrapeObj], sort_keys=True, indent=4, separators=(',', ': ')))
        output_path = os.path.join(__location__, ScrapeObj['name'] + '__CharData.CDF')

        with open(output_path, 'w') as f:
            f.write(mexxy)


