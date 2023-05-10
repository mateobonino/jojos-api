import json
from classes.jojo import Jojo
from classes.stand import Stand

class Serializer():
    _stand_data = ""
    _jojo_data = ""
    def load_data(self):
        raw_data = open('characters.json')
        raw_stand_data = open('stands.json')
        self._jojo_data = json.load(raw_data)
        self._stand_data = json.load(raw_stand_data)

    def search_character(self, name):
        if not name in list(self._jojo_data.keys()):
            return None
        jojo_args = self._jojo_data[name]
        myJojo = Jojo(name, **jojo_args)
        return myJojo

    def search_stand(self, name):
        if not name in list(self._stand_data.keys()):
            return None
        stand_args = self._stand_data[name]
        myStand = Stand(name, **stand_args)
        return myStand

