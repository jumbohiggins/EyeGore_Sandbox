import requests
import json
import os
import Helpers as hlp

class CharClass(object):

    def init(self):
        self.name = "Char_Class"
        helo = hlp.Helpers()

    def CreateCharData(self, charjson, url=None):
        helo = hlp.Helpers()
        self.name = charjson["name"]
        self.strength = charjson["stats"][0]["value"]
        self.dexterity = charjson["stats"][1]["value"]
        self.dex_mod = helo.get_mod(self.dexterity)
        self.constitution = charjson["stats"][2]["value"]
        self.intelligence = charjson["stats"][3]["value"]
        self.wisdom = charjson["stats"][4]["value"]
        self.charisma = charjson["stats"][5]["value"]
        self.proficency = helo.get_proficency_level(charjson["classes"][0]["level"])
        self.basehitpoints = charjson["baseHitPoints"]
        self.overridehitpoints = charjson["overrideHitPoints"]
        self.charxp = charjson["currentXp"]
        self.removedhp = charjson["removedHitPoints"]
        self.race = charjson["race"]["fullName"]
        self.gp = charjson["currencies"]["gp"]
        self.sp = charjson["currencies"]["sp"]
        self.cp = charjson["currencies"]["cp"]
        self.pp = charjson["currencies"]["pp"]
        self.race = charjson["race"]["fullName"]


        helo.race_modify(self)

        self.url = url
        try:
            self.AC = charjson["inventory"][0]["definition"]["armorClass"] + self.dex_mod
        except:
            self.AC = 10 + self.dex_mod

        return self