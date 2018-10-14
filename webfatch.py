import webbrowser
import urllib.request as urllib
from urllib.parse import urlparse
import webbrowser
import dependency.nmap.nmap as nmap


url = "http://technoindiauniversity.ac.in"

#unicode responce of the url 
responce = urllib.urlopen(url)
print (responce)

#print the http status code as 200 , 401 or etc
code = str(responce.getcode())
print (code)

#return the webpage html code 
data = responce.read()

# print (data)

#return the path of website where it is seted 
websitepath = urllib.url2pathname(url)
print (websitepath)

#unwrape the url
unwrap = urllib.unwrap(url)
print (unwrap)

#get return the local ip address
address_of_local_host = urllib.thishost() 
print ("The local IP address of this host is "+ str(address_of_local_host))

#get host name of site

hostname = urlparse(url).hostname
print (hostname)

#getting the host and corrosponding port

host_port = urllib.splitport(hostname)
print (host_port)

print (urllib.splitpasswd("admin"))



#working with web browser

print (webbrowser.__all__)

webbrowser.Chrome("http://google.com")
print(webbrowser.Chrome("http://google.com"))
# webbrowser.open_new_tab("http://google.com")
print(webbrowser.open_new_tab.__call__)

#nmap features

nm = nmap.PortScanner()
print (nm.nmap_version())
scaninfo = nm.scan(hosts=url,arguments='-sV -A')
print(scaninfo)