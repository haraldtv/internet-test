import datetime
import os
import subprocess
import time
import re

with open("log_internet.txt",'w') as file:
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
    #print(speed.group(1))

    print("Formated output:" + speed) 
    with open("internet_log.txt", "a") as myfile:
        myfile.write(str(now))

        myfile.write('\n')

        myfile.write(speed)

        myfile.write('\n')

        myfile.write("----------")

        myfile.write('\n')
        myfile.write('\n')



    time.sleep(60*TEST_INTERVAL)
