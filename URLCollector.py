import CharScrapper as CharScrapper
import os
import Helpers as helpers
import json



class UrlCollect(object):

    def __init__(self):
        self.name = "UrlCollect"
        self.helo = helpers.Helpers()

    def CheckCurrentUrls(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        urls_file = os.path.join(__location__,self.helo.get_campain(__location__) + '__URLS.UFS')
        path_val = self.helo.check_path_valid(urls_file)

        if path_val:
            pysonob = self.helo.Openfile_return_pysonobj(urls_file)

        else:
            self.createUrlFile(urls_file)

    def createUrlFile(self, path):
        with open(path, "w+") as data_file:
            data = {'URLS': [{'Char_name': 'Temp', 'Char_URL': 'Temp'}]}
            json.dump(data, data_file)




UC = UrlCollect()
UC.CheckCurrentUrls()

#cs = CharScrapper.CharScrape()
#charob = cs.CharScrape("https://www.dndbeyond.com/character/4741434/json")
#cs.SaveCharScrape(charob)