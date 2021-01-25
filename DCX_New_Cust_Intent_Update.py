import json
fname = "DCX_Intent.json"

with open(fname) as f:
    newdct = json.load(f)

newdct['Devices'][SW]['customers'].append({'cust_id': cust_id, 'cust_name': cust_name })

with open(fname, "w") as f:
     json.dump(newdct, f)
