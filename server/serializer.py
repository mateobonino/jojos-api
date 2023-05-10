import json
from classes.jojo import Jojo

class Serializer():
    _data = ""

    def load_data(self):
        raw_data = open('characters.json')
        self._data = json.load(raw_data)

    def search_character(self, name):
        if not name in list(self._data.keys()):
            return None
        else:
            jojo_args = self._data[name]
            myJojo = Jojo(name, **jojo_args)
            return myJojo

