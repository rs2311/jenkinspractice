#file1 = open("pythoncreatedfile.yaml")
import sys
with open('pythoncreated.yaml', 'a') as the_file:
     the_file.write('"customers":  [ \n')
     the_file.write('    { \n')
     the_file.write('        "cust_id": "%s", \n'%sys.argv[2])
     the_file.write('        "cust_name": "%s", \n'%sys.argv[1])
     the_file.write('        "l3_vni": "%s", \n'%sys.argv[3])
     the_file.write('        "l3_loopback_ip": "%s", \n'%sys.argv[4])
     
