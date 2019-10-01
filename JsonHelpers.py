import CharScrapper as CharScrapper
import os
import Helpers as helpers
import json
import CharClass as cc
import pickle as pickle


class JsonSearch():

    def __init__(self):
        self.name = "JsonSearch"
        self.helo = helpers.Helpers()

class Json_Note():

    def __init__(self):
        self.name = "Json_Note"
        self.title = ""
        self.tags = ""
        self.body = ""


class JsonAdd():

    def __init__(self):
        self.name = "JsonSearch"
        self.helo = helpers.Helpers()

    def add_Json_Note(self, note):
        self.helo.save_out_picklefile(note, "Note")


class JsonHelpers():

    def __init__(self):
        self.name = "JsonHelpers"

    def get_JsonNotes_file_loc(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.notes = os.path.join(__location__, self.helo.get_campain(__location__) + '.Note')
        print(self.notes)


