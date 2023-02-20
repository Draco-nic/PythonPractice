pcs = {
    "Dan":{
        "GPU": "3080ti",
        "CPU": "5950x",
        "Ram": 32
    },
    "Jack": {
        "GPU": "3080",
        "CPU": "5800x",
        "Ram": 16
    },
    "Connor":{
        "GPU": "2070 super",
        "CPU": "2700x",
        "Ram": 16
    }
}
for x in pcs:
    print(pcs[x].values())