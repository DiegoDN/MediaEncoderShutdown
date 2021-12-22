import os
import psutil
import signal
import subprocess
import sys
from pprint import pprint as pp
from time import sleep
from time import gmtime, strftime

try:
    #0) Get PID & CPU QTY used by MediaEncoder
    def mediaEncoderCpu():    
        for id in psutil.pids():
            p = psutil.Process(id)
            if ( p.name() == 'Adobe Media Encoder.exe'):
                cpuInt = int(p.cpu_percent(interval=1))
                print("PID:", p.pid)
                print("CPU: ", cpuInt)
                return cpuInt
            
    def mediaEncoderPID():
        for id in psutil.pids():
            p = psutil.Process(id)
            if ( p.name() == 'Adobe Media Encoder.exe'):
                 return p.pid


    #1) Control Ammount of X CPU percentage that are allowed;
    cpuQty = 50


    #2) Check if during 5 minutes the ps still allocated cpu (eliminated case of low ram allocation during audio encoding)
    counter = 0
    while (counter < 3):
        cpuQtyInUse = mediaEncoderCpu()
        if(cpuQtyInUse <= cpuQty): 
            print("Current CPU Usage: ", cpuQtyInUse)
            counter = counter + 1
            print("Preparing to shutdown, Step #", counter, "of 3. Time: ", strftime("%Y-%m-%d %H:%M:%S"))
            sleep(120) #wait 2min
        else:
            counter = 0;
            print("Current CPU Usage: ", cpuQtyInUse)
            print("Encoding...", "Time: ", strftime("%Y-%m-%d %H:%M:%S"))
            sleep(120) #wait 2min
            

    #3) process released ram, has finished, lets kill it.
    os.system("taskkill /im \"Adobe Media Encoder.exe\"")


    #4) Wait for a minute than shutdown computer.
    subprocess.call(["shutdown.exe", "/s", "/f", "/t", "60"])


except:
    print ("Media Encoder not running. Try Again.")
    os.system("pause") 






