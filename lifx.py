from lazylights import Lifx
import time

lifx = Lifx(num_bulbs=1)

@lifx.on_connected
def _connected():
	print 'Connected!'

with lifx.run():
	# lifx.set_power_state(True)
	time.sleep(1)
	lifx.set_power_state(True)
	lifx.set_light_state(30,0.6,0.1,10,timeout=1)
	time.sleep(1)
	lifx.set_light_state(30,0.6,0.1,10,timeout=1)
        time.sleep(1)
	i = 0.1;
	print "About to start loop"
	while (i < 1.0): # 17 minute loop
		lifx.set_light_state(30+(i*20),0.6,i,10,timeout=1)
        	time.sleep(1*60) # 1 minute
		print "I is " + str(i)
		i += 0.05
	lifx.set_light_state(30,0.1,1.0,10,timeout=1)
	lifx.stop()
