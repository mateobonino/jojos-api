import json

class Jojo():
    name = ""
    season = ""
    abilities = []
    age = 0
    birthday = ""
    height = ""
    weight = ""
    nationality = ""

    def __init__(self, name, **kwargs):
        self.name = name
        self.season = kwargs['season']
        self.abilities = kwargs['abilities']
        self.age = kwargs['age']
        self.birthday = kwargs['birthday']
        self.height = kwargs['height']
        self.weight = kwargs['weight']
        self.nationality = kwargs['nationality']

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
