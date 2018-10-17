import requests
import json
import os
import glob
import fnmatch

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


    def get_location(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        return __location__






