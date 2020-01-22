import json
import datetime

contributors = []
with open("data/contributors.csv", encoding="utf-8") as contrib_f:
    data = [line.split(",", maxsplit=2) for line in contrib_f.readlines()]
    for dt, name, comment in data:
        if len(dt) < 4:
            continue
        dt = datetime.datetime.strptime(dt, "%m/%d/%Y %H:%M:%S") # 1/19/2020 20:56:04
        comment = comment.strip("\"\n   ")
        user = {"name": name, "time":dt.isoformat(), "comment":comment}
        contributors.append(user)

with open("data/contributors.json", "w+") as contrib_json_f:
    json.dump(contributors, contrib_json_f)