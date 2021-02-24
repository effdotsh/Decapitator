import random
import string
import os
import pathlib
from crontab import CronTab
import getpass

os.system('clear')
data = open('data.json', 'w+')
data.write('{')


def select(choices, num_options, question, default=1):
    # Get inputed selection as a number
    print(choices)
    valid_selection = False
    while not valid_selection:
        try:
            selected_option = input(question)
            if selected_option == '':
                selected_option = default
            else:
                selected_option = int(selected_option)
            if 1 <= selected_option <= num_options:
                valid_selection = True
                return selected_option
        except:
            print("Please select a valid option")


options = '''Thank you for installing Decapitator, a simple tool that allows you not to worry about changing 
non-static IP addresses. Please select a method of notification (currently I have only set up one, more will 
hopefully come in the future): 

1. Dweet - A simple, free, IoT messaging system.

'''
selectedOption = select(options, 1, "Choose a method (1): ")

# dweet
if selectedOption == 1:
    meathod = "Dweet"
    options = '''
	You have chosen Dweet. There are some Dweet customizations to choose from.
	This code only supports publicly accessible dweets. This means that if anyone has
	your access code, they can get your IP. This means that having a random access code
	makes it less likely for someone to accidentally find your information. This information 
	is not a security risk for most people, as this is just the local IP.
	However, due to the open and public nature of dweets, anyone can dweet to any dweet.
	Therefore having a random access code has a significantly lower chance of two systems 
	causing conflicts. Due to the possibility of conflicts, I heavily recommend using a
	random access code.
	
	1. Random
	2. Custom
	'''
    rand_or_custom = select(options, 2, "Would you like a random or custom access code (1): ")
    data.write(f'"rand_or_custom": {str(rand_or_custom)},')
    access_code = (
        ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(15))).lower()
    if rand_or_custom == 2:
        access_code = input("Make a unique access code: ")
    data.write('"access_code":"' + access_code + '",')
    print('\n')
    print(
        "That's it! Thank you for using decapitator, the best headless solution. You can now access your pi's ip at "
        "the following link. This will update every time the pi reboots: ")
    print(f'https://dweet.io/get/latest/dweet/for/{access_code}')
data.write(f'"method": "{meathod}"')
data.write('}')
data.flush()
data.close()


crontab_auth = input("Automatically run crontab [Y/n]: ")
if crontab_auth.lower() != 'n':
    path = pathlib.Path(__file__).parent.absolute()
    cron = CronTab(user=getpass.getuser())
    job = cron.new(command=f'cd {path} && python3 decapitator.py')
    job.every_reboot()
    cron.write()


os.system("python3 decapitator.py")

print('done')
