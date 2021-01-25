import json
fname = "DCX_Intent.json"

with open(fname) as f:
    newdct = json.load(f)

newdct['Devices'][SW]['customers'].append({'cust_name': "%s", \n'%sys.argv[1], 'cust_id': "%s", \n'%sys.argv[2] })

with open(fname, "w") as f:
     json.dump(newdct, f)
