import random
import string
import os
import pathlib

os.system('clear')
data = open('data.json', 'w+')
data.write('{')
def select(choices, numOptions, question, default=1):
	#Get inputed selection as a number
	print(choices)
	validSelection = False
	while(not validSelection):
		try:
				selectedOption = input(question)
				if(selectedOption == ''):
					selectedOption = default
				else:
					selectedOption = int(selectedOption)
				if(selectedOption >= 1 and selectedOption <= numOptions):
					validSelection = True
					return selectedOption
		except:
			print("Please select a valid option")
def setupStartup():
	#Add decapitator.py to rc.local so it runs on startup
	print('In order for this program to do what it needs to do, it needs to run on startup')
	approval = input('Would you like this to do that automatically? (y/n): ')
	while approval.lower() not in {'y', 'n', 'yes', 'no'}:
		approval = input('Would you like this to do that automatically? (y/n): ')
	if approval.lower()[0] =='y':
		rc = open('/etc/rc.local', 'a')
		check_rc = open('/etc/rc.local', 'r')
		shouldWrite = True
		for line in check_rc:
			if 'python3 decapitator.py ' in line:
				shouldWrite = False
				print('It looks like this program is already in your startup. It won\'t be added again')
		if (shouldWrite):
			print(pathlib.Path(__file__).parent.absolute())
			rc.write('cd ' + str(pathlib.Path(__file__).parent.absolute()) + '\n')
			rc.write('python3 decapitator.py \n')
			rc.write('cd \n')
			rc.flush()
			rc.close()






options = '''
Thank you for installing Decapitator, a simple tool that allows you not to worry about changing non-static IP addresses. Please select a method of notification (currently I have only set up one, more will hopefully come in the future):

1. Dweet - A simple, free, IoT messaging system.

'''
selectedOption = select(options, 1, "Choose a meathod (1): ")

#dweet
if selectedOption == 1:
	meathod = "Dweet"
	options = '''
	You have chosen Dweet. There are some Dweet customizations to choose from.
	This code only supports publicly accessible dweets. This means that if anyone has
	your access code, they can get your IP. This means that having a random access code
	makes it less likely for someone to accidentally find your information. This information 
	is not a security risk for most people, as there isn't anything to link you to the IP.
	Additionally, due to the open and public nature of dweets, anyone can dweet to any dweet.
	Therefore having a random access code has a significantly lower chance of two systems 
	causing conflicts. Due to the possibility of conflicts, I heavily recommend using a
	random access code.
	
	1. Random
	2. Custom
	'''
	rand_or_custom = select(options, 2, "Would you like a random or custom access code (1): ")
	data.write('"rand_or_custom":' + str(rand_or_custom) + ',')
	access_code = (''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(15))).lower()
	if(rand_or_custom == 2):
		access_code = input("Make a unique access code: ")
	data.write('"access_code":"'+access_code+'",')
	setupStartup()
	print('\n')
	print("That's it! Thank you for using decapitator, the best headless solution. You can now access your pi's ip at the following link. This will update every time the pi reboots: ")
	print("https://dweet.io/get/latest/dweet/for/"+access_code)
data.write('"meathod":"' + meathod+'"')
data.write('}')
data.flush()
data.close()
os.system("python3 decapitator.py")





