import json
def grt_coct():
    with open("coctail.json", 'r') as f:
        coctails = json.load(f)
    return coctails

print(grt_coct())