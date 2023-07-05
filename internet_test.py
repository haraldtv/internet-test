import datetime
import os
import subprocess
import time
import re

with open("log_verbose.txt",'w') as file:
    pass

with open("log_rawdata.txt",'w') as file:
    pass


#iPerf server address
IP_ADDR = '62.210.18.40'

#In seconds
TEST_TIME = str(2)

#In minutes 
TEST_INTERVAL = 2 

#In minutes
MAX_RUNTIME = 60*4

iterator = 0

while (iterator*TEST_INTERVAL != MAX_RUNTIME):
    
    iterator += 1
    print("Run #: " + str(iterator))

    now = datetime.datetime.now()
    output = subprocess.check_output(['iperf', '-c', IP_ADDR, '-t', TEST_TIME])

    print(str(now) + "\n")
    print(output)
    print("----------\n\n")

    speed = re.search('MBytes(.*)Mbits', str(output))
    speed = str(speed.group(1)).strip()
    size = re.search('sec(.*)MBytes', str(output))
    size = str(size.group(1)).strip()
    length = re.search('0.00-(.* )sec', str(output))
    length = str(length.group(1)).strip()
    #print(speed.group(1))

    print("Formated output: " + length + " sec - " + size + " MBytes - " + speed + " Mbit/s") 
    with open("log_verbose.txt", "a") as myfile:
        myfile.write(str(now))

        myfile.write('\n')

        myfile.write(length + " sec - " + size + " MBytes - " + speed + " Mbit/s")

        myfile.write("\n")

        myfile.write("----------")

        myfile.write('\n')
        myfile.write('\n')


    with open("log_rawdata.txt", "a") as fp:
        fp.write(speed)
        fp.write("\n")


    time.sleep(60*TEST_INTERVAL)
