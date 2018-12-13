import requests
import json
import os
import glob
import fnmatch
import pickle
import io

class Helpers(object):

    def __init__(self):
        self.name = "Helpers"


    def get_campain(self, __location__):

        path = os.path.join(__location__, "Campaigns.CMPS")

        if not os.path.exists(path):
            with open(path, "w+") as data_file:
                data = {'Campains':[{'name': 'TheGreatAdventure', 'CurrentCampaign': 'True'}]}
                json.dump(data, data_file)

        else:
            with open(path) as data_file:
                input = data_file.read()
                data = json.loads(input)
                for campaign in data['Campains']:

                    if campaign['CurrentCampaign'] == "True":
                        print("Walnut")
                        return campaign['name']

    def Openfile_return_pysonobj(self, __location__):
        print('000')
        with open(__location__) as data_file:
            input = data_file.read()
            data = json.loads(input)
            return data


    def joinpath(self, path):
        path_loc = os.path.join(path)
        return(path_loc)


    def check_path_valid(self, path):

        if not os.path.exists(path):
            return False
        else:
            return True

    def race_modify(self, charob):
        print(charob.race)

        if charob.race == "Human":
            charob.strength = charob.strength + 1
            charob.dexterity = charob.dexterity + 1
            charob.constitution = charob.constitution + 1
            charob.intelligence = charob.intelligence + 1
            charob.wisdom = charob.wisdom + 1
            charob.charisma = charob.charisma + 1

        if charob.race == "Dragonborn":
            charob.strength = charob.strength + 2
            charob.charisma = charob.charisma + 1

        if charob.race == "Dwarf":
            charob.constitution = charob.constitution + 2

        if charob.race == "Elf":
            charob.dexterity = charob.dexterity + 2

        if charob.race == "Gnome":
            charob.intelligence = charob.intelligence + 2

        if charob.race == "Halfling":
            charob.dexterity = charob.dexterity + 2

        if charob.race == "Half-Orc":
            charob.strength = charob.strength + 2
            charob.constitution = charob.constitution + 1

        if charob.race == "Half-Elf":
            charob.charisma = charob.charisma + 2

        if charob.race == "Tiefling":
            charob.charisma = charob.charisma + 2
            charob.intelligence = charob.intelligence + 1

        return charob

    def get_location(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        return __location__

    def save_out_jsonfile(self, data_to_write, extention):
        __location__ = self.get_location()
        jdump = (json.dumps(data_to_write.__dict__, sort_keys=True, indent=4, separators=(',', ': ')))
        output_path = os.path.join(__location__, data_to_write['name'] + extention)
        with open(output_path, 'w') as f:
            f.write(jdump)


    def save_out_picklefile(self, data_to_write, extention):

        __location__ = self.get_location()
        loc = os.path.join(__location__, extention)
        file_pi = open(loc, 'wb')
        pickle.dump(data_to_write, file_pi)


    def load_picklefile(self, path):
        __location__ = self.get_location()
        loc = os.path.join(__location__, path)

        with open(loc, 'rb') as input_file:
            loadob = pickle.load(input_file)
        input_file.close()

        return loadob


    def get_player_count(self):
        return 6

    def get_proficency_level(self, playerlevel):
        if playerlevel < 5:
            return 2
        if playerlevel >= 5 and playerlevel < 9:
            return 3
        if playerlevel >= 9 and playerlevel < 13:
            return 4
        if playerlevel >= 13 and playerlevel < 17:
            return 5
        if playerlevel >= 17:
            return 6

    def get_mod(self, baseint):
        if baseint < 2:
            return -5
        if baseint < 4:
            return -4
        if baseint < 6:
            return -3
        if baseint < 8:
            return -2
        if baseint < 10:
            return -1
        if baseint < 12:
            return 0
        if baseint < 14:
            return 1
        if baseint < 16:
            return 2
        if baseint < 18:
            return 3
        if baseint < 20:
            return 4
        if baseint < 22:
            return 5