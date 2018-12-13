import CharScrapper as CharScrapper
import os
import Helpers as helpers
import json
import CharClass as cc
import pickle as pickle

class UrlCollect(object):

    def __init__(self):
        self.name = "UrlCollect"
        self.helo = helpers.Helpers()

    def get_urls_file_loc(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.urls_file = os.path.join(__location__, self.helo.get_campain(__location__) + '__URLS.UFS')

    def CheckCurrentUrls(self):
        helo = helpers.Helpers()
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.urls_file = os.path.join(__location__,self.helo.get_campain(__location__) + '__URLS.UFS')
        path = self.helo.get_campain(__location__) + '__URLS.UFS'
        pysonob = helo.load_picklefile(path)
        return pysonob

    def createUrlFile(self, path, data):
        with open(path, "wb") as data_file:
            pickle.dump(data, data_file)

    def addUrls(self, urllist):
        #pysonob = self.CheckCurrentUrls()
        helo = helpers.Helpers()
        self.get_urls_file_loc()
        char_list = []
        for url in urllist:
            cs = CharScrapper.CharScrape()
            charob = cs.CharScrape(url)
            CharC = cc.CharClass()
            CharData = CharC.CreateCharData(charob, url)
            #CharData = helo.race_modify(CharData)
            char_list.append(CharData)

        for each in char_list:
            print(each.name, each.url)
        self.createUrlFile(self.urls_file, char_list)

    def getUrls(self):
        pysonob = self.CheckCurrentUrls()
        for each in pysonob:
            print(each.name)


UC = UrlCollect()
UC.addUrls(["https://www.dndbeyond.com/character/2113653/json", "https://www.dndbeyond.com/character/4741434/json"])
#UC.getUrls()

#cs = CharScrapper.CharScrape()
#charob = cs.CharScrape("https://www.dndbeyond.com/character/2113653/json")
#print(charob['name'])
#cs.SaveCharScrape(charob)