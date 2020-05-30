import os
import json


def translateIdsToModulesNames(c_databases, p):
    with open(p+'/data/modulesMap.json', "r", encoding='utf8') as read_file:
        config = json.load(read_file)

    schema = {}

    for i in c_databases:
        schema[i] = {}
        if config[i]['local'] == "No":
            schema[i]['url'] = config[i]['execution_model']
            schema[i]['type'] = 'external'
        else:
            schema[i]['url'] = config[i]['url']
            schema[i]['type'] = 'local'
    return(schema)
