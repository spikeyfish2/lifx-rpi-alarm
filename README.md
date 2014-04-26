This is only a very *basic* solution to the problem, done in a few minutes. As far as I know, this will only work with a single bulb, and it fades from off through dark orange to light orange. 

#Usage
Put the script in a folder somewhere accessible by your RPi user (Home folder is recommended). Type
	`crontab -e`

Then append a line that looks like this to the cron file:
	`0 8 * * * python /root/lifx.py`

Change the path of the lifx.py file to wherever you saved it, and use the numbers on the left to set the time. The '0' is the minutes, and '8' is the hour, so if set as above, the lights would come on at 08:00am. 

#Troubleshooting
**Why does my bulb come on at the wrong time?**

Make sure your time settings are correct on the RPi.

*Why doesn't my bulb come on at all?*

Make sure your RPi is on the same network as the Lifx bulb.


#License
[Lazylights](https://github.com/mpapi/lazylights) runs under the MIT license, I've included it here purely for ease-of-use. You can install it yourself if you prefer, then just use the lifx.py file.
