import codecs
import json
from mimetypes import init
from turtle import mode
f = codecs.open('マトリクス.json', 'r', "utf8")
json_dict = json.load(f)

class Case:
    case_count = 0
    def __init__(self, factor, result):
        print("CASE" + str(case_id) + ":" + str(factor) + " Was Apennded. -> " + result)
        pass

all_cases = []

factors = dict()

output_mode = 0
def case_parse(id, case_path, result):# 経緯と結果
    all_cases.append(Case(case_path, result))
    if output_mode == 0:
        for case in case_path:
            if "[" in case and "]" in case:
                factor_name = case.split("]")[0][1:]
                factor_value = case.split("]")[1]
                if type(factors.get(factor_name)) is list:
                    factors[factor_name].append(factor_value)
                else:
                    factors[factor_name] = [factor_value]

    else:
        print(str(case_path) + " → CASE" + str(id) + ": " + str(result))
    return

case_id = 0
def object_parse(object, path):
    global case_id
    for key, value in object.items():
        current_path = path.copy()
        current_path.append(key)
        if type(value) is str:
            case_id += 1
            case_parse(case_id, current_path, value)
        elif type(value) is dict:
            object_parse(value, current_path)
object_parse(json_dict, [])

# CSV
print("FACTOR, VALUE")
for factor, values in factors.items():
    for value in values:
        print(factor, ",", value)

