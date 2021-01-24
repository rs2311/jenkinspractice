#file1 = open("pythoncreatedfile.yaml")
import sys
with open('pythoncreated.yaml', 'a') as the_file:
     the_file.write('%s\n'%sys.argv[1])
    
    
