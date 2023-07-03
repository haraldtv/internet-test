import datetime
import os
import subprocess
import time

with open("internet_log.txt",'w') as file:
    pass

#iPerf server address
IP_ADDR = '62.210.18.40'

#In seconds
TEST_TIME = str(10)

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

    with open("internet_log.txt", "a") as myfile:
        myfile.write(str(now))

        myfile.write('\n')

        myfile.write(str(output))

        myfile.write('\n')

        myfile.write("----------")

        myfile.write('\n')
        myfile.write('\n')


    time.sleep(60*TIME_INTERVAL)
