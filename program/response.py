#################
#  FACTURATION  #
#  response.py  #
#  Gardier S.   #
#################

class Response:

    def __init__(self):
        self.state = False
        self.message = "Response message"
        self.data = None

    ## Getter

    def get_state(self):
        return self.state

    def get_message(self):
        return self.message

    def get_data(self):
        return self.data

    ## Setter

    def set_state(self, s):
        self.state = s

    def set_message(self, m):
        self.message = m

    def set_data(self, d):
        self.data = d


    def set_response(self, s, m, d):
        self.state = s
        self.message = m
        self.data = d
