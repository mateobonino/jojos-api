import json

class Stand():

    def __init__(self, name, **kwargs):
        self.name = name
        self.user = kwargs['user']
        self.attack = kwargs['attack']
        self.defense = kwargs['defense']
        self.type = kwargs['type']
        self.speed = kwargs['speed']

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
