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

        for key, value in kwargs.items():
            if key == 'season':
                self.season = value
            if key == 'abilities':
                self.abilities = value
            if key == 'age':
                self.age = value
            if key == 'birthday':
                self.birthday = value
            if key == 'height':
                self.height = value
            if key == 'weight':
                self.weight = value
            if key == 'nationality':
                self.nationality = value

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
