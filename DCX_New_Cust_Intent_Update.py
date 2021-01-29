import sys
import json

fname = "DCX_Intent.json"

with open(fname) as f:
    newdct = json.load(f)

custid_found = False

for entry in newdct['Devices'][sys.argv[1]]['customers']:
    if entry['cust_id'] == sys.argv[2]:
        print 'entry_found'
        entry.update({'cust_id': '%s'%sys.argv[2], 'cust_name': '%s'%sys.argv[3], 'l3_loopback_subnet': '%s'%sys.argv[4], 'l3_vni': '%s'%sys.argv[5], 'type5_routes':[{'type5_vlan_id': '%s'%sys.argv[6], 'type5_vlan_name': '%s'%sys.argv[7], 'type5_vlan_subnet': '%s'%sys.argv[8], }], 'type2_routes':[{'type2_vlan_id': '%s'%sys.argv[6], 'type2_vlan_name': '%s'%sys.argv[7], 'type2_vlan_subnet': '%s'%sys.argv[8], }],})
        custid_found = True
        break


if custid_found == False:
         print 'entry_notfound'
         newdct['Devices'][sys.argv[1]]['customers'].append({'cust_id': '%s'%sys.argv[2], 'cust_name': '%s'%sys.argv[3], 'l3_loopback_subnet': '%s'%sys.argv[4], 'l3_vni': '%s'%sys.argv[5], 'type5_routes':[{'type5_vlan_id': '%s'%sys.argv[6], 'type5_vlan_name': '%s'%sys.argv[7], 'type5_vlan_subnet': '%s'%sys.argv[8], }], 'type2_routes':[{'type2_vlan_id': '%s'%sys.argv[6], 'type2_vlan_name': '%s'%sys.argv[7], 'type2_vlan_subnet': '%s'%sys.argv[8], }],})

with open(fname, "w") as f:
     json.dump(newdct, f)

        
        
        
