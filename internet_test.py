import datetime
import os
import subprocess
import time
import re

with open("internet_log.txt",'w') as file:
    pass

#iPerf server address
IP_ADDR = '62.210.18.40'

#In seconds
TEST_TIME = str(2)

#In minutes 
TEST_INTERVAL = 15

iterator = 0

while (iterator != 50):
    
    iterator += 1
    print("Run #: " + str(iterator))

    now = datetime.datetime.now()
    output = subprocess.check_output(['iperf', '-c', IP_ADDR, '-t', TEST_TIME])

    print(str(now) + "\n")
    print(output)
    print("----------\n\n")

    speed = re.search('MBytes(.*)Mbits', str(output))
    speed = speed.strip()
    #print(speed.group(1))

    print("Formated output:" + str(speed.group(1))) 
    with open("internet_log.txt", "a") as myfile:
        myfile.write(str(now))

        myfile.write('\n')

        myfile.write(str(speed.group(1)))

        myfile.write('\n')

        myfile.write("----------")

        myfile.write('\n')
        myfile.write('\n')



    time.sleep(60*TEST_INTERVAL)
