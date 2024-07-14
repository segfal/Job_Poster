import json

IS_PROD = False # Change this to True when deploying to production

def is_prod():
    return IS_PROD


def get_channels():
    if is_prod():
        with open('prod.json', 'r') as f:
            data = json.load(f)
            return data
    else:
        with open('dev.json', 'r') as f:
            data = json.load(f)
            return data
    




