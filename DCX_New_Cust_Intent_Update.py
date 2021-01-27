import sys
import json

fname = "DCX_Intent.json"

with open(fname) as f:
    newdct = json.load(f)

print newdct['Devices'][sys.argv[1]]['customers']

newdct['Devices'][sys.argv[1]]['customers'].append({'cust_name': '%s'%sys.argv[3], 'cust_id': '%s'%sys.argv[2], 'l3_loopback_ip': '%s'%sys.argv[5], 'l3_vni': '%s'%sys.argv[6], })

print newdct['Devices'][sys.argv[1]]['customers']

with open(fname, "w") as f:
     json.dump(newdct, f)

print newdct['Devices'][sys.argv[1]]['customers']
        
        
        
        
