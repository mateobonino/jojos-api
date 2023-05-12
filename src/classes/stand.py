import json

class Stand():

    def __init__(self, name, **kwargs):
        self.name = name
        self.user = kwargs['user']
        self.power = kwargs['power']
        self.type = kwargs['type']
        self.potential = kwargs['potential']
        self.durability = kwargs['durability']
        self.range = kwargs['range']
        self.speed = kwargs['speed']
        self.precision = kwargs['precision']

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
