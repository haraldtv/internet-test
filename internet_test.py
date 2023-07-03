import datetime
import os
import subprocess
import time

with open("internet_log.txt",'w') as file:
    pass

IP_ADDR = '62.210.18.40'

iterator = 0

while (iterator != 50):
    
    iterator += 1
    print("Run #: " + str(iterator))

    now = datetime.datetime.now()
    output = subprocess.check_output(['iperf', '-c', IP_ADDR, '-t', '10'])

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


    time.sleep(60*15)
