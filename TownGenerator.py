import os
import json
import random as rand
import Helpers as hlp
import re
import GeneratorHelpers as GenHelp

class GenerateTown(object):

    def __init__(self):
        print("startup the town")


    def randomtownie(self):
        print("townie")
        GH = GenHelp.GeneratorHelpers()
        max = GH.quick_char()
        print("---------------------")
        print(max.lastnames)
        print(max.firstnames)
        print(max.nouns)
        print(max.charTraits)
        print(max.mannerisms)


class Town_blank(object):

    def __init__(self):
        self.TownName = ""
        self.PopulationSize = ""
        self.HowManyNpcsToGenerate = ''
        self.GenerateMerchants = False
        self.Npc_obj = []

