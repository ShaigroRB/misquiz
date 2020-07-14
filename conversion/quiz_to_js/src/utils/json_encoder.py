import json

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        """ Default method to encode an object in JSON """
        if (hasattr(obj, 'to_json')):
            return obj.to_json()
        else:
            return json.JSONEncoder.default(self, obj)