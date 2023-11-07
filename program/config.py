#################
#  FACTURATION  #
#  config.py    #
#  Gardier S.   #
#################

import json

class Config():
    def __init__(self):
        self.language = "en"
        self.treatment = 0
        self.debug = False
        self.load_config()

    def get_language(self):
        return self.language

    def change_language(self):
        if (self.language == "en"):
            self.language = "fr"
        else:
            self.language = "en"
        self.new_config()

    def get_debug(self):
        return self.debug

    def get_treatment(self):
        return self.treatment

    def load_config(self):
        try:
            with open('config.json', 'r') as cfg:
                cfg = json.load(cfg)
                self.language = cfg["language"]
                self.treatment = cfg["number_of_treatment"]
                self.debug = cfg["debug"]
        except:
            print("Error - Load config\nNew config generated")
            self.new_config()

    def new_config(self):
        new_cfg = {
            "language": self.language,
            "number_of_treatment": self.treatment,
            "debug": self.debug
        }

        json_object = json.dumps(new_cfg, indent=3)

        with open("config.json", "w") as outfile:
            outfile.write(json_object)
        
