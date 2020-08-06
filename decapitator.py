import subprocess
import requests 
import json

with open('data.json', 'r') as openfile: 
    # Reading from json file 
    data = json.load(openfile) 
def sendData(eth0):
	if (data['meathod'] == 'Dweet'):
		r = requests.post('https://dweet.io/dweet/for/' + data['access_code'] + '?eth0=' + str(eth0))
		print(r)
		
		
#read data file
#write the output of 'ifconfig' to variable
ifconfig = str(subprocess.check_output('ifconfig'))
#look at each line in the output and find the ip addresses
ifconfig = ifconfig.split('\\n')
lineNumber = 0
eth0_ip = False
for line in ifconfig:
	#ethernet
	if(line.split(': ')[0] == 'b\'eth0' and line != ifconfig[-1]):
		
		row = ifconfig[lineNumber + 1]
		#remove spaces from start of line
		#this probably isn't required, however between different os's and systems,
		#or by sheer bad luck the number of spaces before the line may be different,
		#so I don't want to simply take the ninth element of the array.
		eth0_ip = row.split('inet ')[1].split(' ')[0]
	lineNumber += 1
	
if(eth0_ip != False):	
	sendData(eth0_ip)
	print(":)")
else:
	print(":(")
