import os
import platform 
import sys

print(sys.gettrace())
print(os.getcwd() , os.get_blocking(1) , os.get_exec_path() , os.get_inheritable(1) )

print (os.get_terminal_size())
print ("The code is running from : "+os.getcwd())

print ("The credention " + str(os.geteuid())  )
print ("The os use groups are "+ str(os.getgroups()))
print ("The average system load information  " + str(os.getloadavg()))
print ("Get os login "+ os.getlogin() + " \n The p_id: " + str(os.getpgid(1)) + "\n the p_group: " + str(os.getpgrp()))
print ("\n os p_id :"+ str(os.getpid()) + "\n os_pp_id :" + str(os.getppid()))
print ("\nvgroup id"+ str(os.getresgid())+ "\nuser_id "+str(os.getresuid()))
print ("\n "+ str(os.getsid(1))+ "\n"+ str(os.getuid()))
print ("cpu count :"+ str(os.cpu_count()))


print ("\n\n\n \t\t<--- SYSTEM INFORMATION ---> \n\n\n")
print (""+ str(platform.uname()))
print("With processor "+ platform.processor() + "The machine "+  platform.machine() +" run in " + platform.node() + "node is connected in " + str( platform.mac_ver()) )
print (""+ str(platform.java_ver()))
print("python version " + str(platform.python_version_tuple()))
