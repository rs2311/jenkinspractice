import sys
import json

fname = "DCX_Intent.json"

with open(fname) as f:
    newdct = json.load(f)

print newdct['Devices']['%s'%sys.argv[0]]['customers']

newdct['Devices']['%s'%sys.argv[3]]['customers'].append({'cust_name': '%s'%sys.argv[3], 'cust_id': '%s'%sys.argv[2], })

print newdct['Devices']['%s'%sys.argv[3]]['customers']

with open(fname, "w") as f:
     json.dump(newdct, f)

print newdct['Devices']['%s'%sys.argv[3]]['customers']
        
        
        
        
