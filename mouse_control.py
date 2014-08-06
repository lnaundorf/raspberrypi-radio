from evdev import InputDevice, categorize, ecodes, KeyEvent, list_devices
from select import select
import subprocess
from time import sleep

LIVESTREAM_URL="http://fritz.de/livemp3"
ls = None
playing = False
RIGHT_BTN_PRESS_TIMESTAMP = None



def wait_for_usb_mouse():
	usb_mouse_dev = None
	while True:
		devices = map(InputDevice, list_devices())
		for dev in devices:
			if "mouse" in dev.name.lower() and "usb" in dev.phys.lower():
				usb_mouse_dev = dev
				break

		if usb_mouse_dev is None:
			print "No USB mouse found. sleeping."
			sleep(5)
		else:
			print "Found USB mouse: %s" % str(usb_mouse_dev.name)
			return usb_mouse_dev


dev = wait_for_usb_mouse()
while True:
	try:
		for event in dev.read_loop():
				if event.type == ecodes.EV_KEY:
					if event.code == ecodes.ecodes['BTN_LEFT'] and categorize(event).keystate == KeyEvent.key_down:
						if not playing:
							#print "Start playing: %s" % LIVESTREAM_URL
							ls = subprocess.Popen(["mplayer", LIVESTREAM_URL])
							playing = True
						else:
							#print "Stop playing stream"
							playing = False
							ls.terminate()
					elif event.code == ecodes.ecodes['BTN_RIGHT']:
						if categorize(event).keystate == KeyEvent.key_down:
							RIGHT_BTN_PRESS_TIMESTAMP = event.timestamp()
						elif categorize(event).keystate == KeyEvent.key_up and RIGHT_BTN_PRESS_TIMESTAMP is not None:
							timedelta = event.timestamp() - RIGHT_BTN_PRESS_TIMESTAMP
							if timedelta >= 3.0:
								print "Pressed %.2f seconds. Shutting down" % timedelta
								
	except:
		print "Mouse disconnected."
		dev = wait_for_usb_mouse()

		
				

			

