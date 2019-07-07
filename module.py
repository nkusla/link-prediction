import datetime
import json
import os

(dirname, prom) = os.path.split(os.path.dirname(__file__))
json_path = os.path.join(dirname, "Link Prediction\\Results\\results.json")

def create_dic_result(graph_num, pos_size, neg_size, num_of_feat, func_name):
    result = {}
    now = datetime.datetime.now()
    result["time"] = "{} {}:{}".format(now.date(), now.hour, now.minute)
    result["graph"] = graph_num
    result["accuracy"] = 0

    result["test_size"] = float(input("Test size: "))
    result["positive_size"] = pos_size
    result["negative_size"] = neg_size
    result["num_of_feat"] = num_of_feat
    result["ML_algorithm"] = func_name
    result["desc"] = input("Desc: ")

    return result

def document_result(result, json_path):
    with open(json_path, "r") as f:
        json_file = json.load(f)
        json_file["results"].append(result)
    
    with open(json_path, "w") as f:
        json_file = json.dumps(json_file, indent = 4)
        f.write(json_file)