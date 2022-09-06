import codecs
import json
from mimetypes import init
f = codecs.open('マトリクス.json', 'r', "utf8")
json_dict = json.load(f)

case_id = 0
def object_parse(object, path):
    global case_id
    for key, value in object.items():
        current_path = path.copy()
        current_path.append(key)
        if type(value) is str:
            case_id += 1
            print(str(current_path) + " → CASE" + str(case_id) + ": " + str(value))
        elif type(value) is dict:
            object_parse(value, current_path)
object_parse(json_dict, [])