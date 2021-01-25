import sys
import json
import groovy.json.*

fname = "./DCX_Intent.json"

with open(fname) as f:
    newdct = json.loads(f)

print newdct['Devices']['CL31']['customers']

#newdct['Devices']['CL31']['customers'].append({'cust_name': '%s'%sys.argv[1], 'cust_id': '%s'%sys.argv[2], })

#print newdct['Devices']['CL31']['customers']

#with open(fname, "w") as f:
#     json.dump(newdct, f)
