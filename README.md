<a href="https://aispawn.com/support" target="_blank"><img src="https://aispawn.com/support/readme-image.png" alt="Support Me!" height="41" width="174"></a>

# Decapitator

## What is Decapitator?
On boot, Decapitator will find your IP and send it to you. Currently this is done through a system called [Dweets](https://dweet.io), however I am working to provide additional functionality in the future. Also Decapitator only sends your **local** IP, however this too will be updated in a future release to provide more options.

### Background
I've recently been working on a steam trading bot which I am hosting on a Raspberry Pi. I would run everything in headless mode, and interface with it via SSH and SFTP. However, a tropical storm had caused the power to go down. Once power came back, I realized that I was unable to SSH into my pi. So I went to the Pi, moved it over to the monitor, restarted it, and found it's IP Address. Although this really isn't a lot of work, it is still a pointless task and I thought that there had to be a better way. 

Decapitator is a tool to help you run Raspberry Pi's (and other Linux based machines) headless. Get it, it's a pun. Headless... decapitator... I like my jokes a bit too much.  




## Installation
First start by cloning the repository

>cd
>git clone https://github.com/AI-Spawn/Decapitator


Then run init.py
>cd Decapitator 
>python3 init.py

Select details about your Decapitation, this should be pretty straightforward as there are only really one or two choices.

At the end, the program will say that you can access your IP at `https://dweet.io/get/latest/dweet/for/XXXXXXXXXXXXXX`. Make sure you copy down this link. 



That's It! Thank you for using Decapitator, you can now reboot to test. 


## Bugs
If you find a problem with Decapitator, please [open an issue for it]([https://github.com/AI-Spawn/Decapitator/issues/new](https://github.com/AI-Spawn/Decapitator/issues/new)), but first please just check to see if it has already been reported. 
