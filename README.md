raspberrypi-radio
=================

The files and guide needed to setup a Raspberry Pi as radio


* Raspbian Image runterladen und per win32DiskImager raufspielen

* Shairport:
http://www.raywenderlich.com/44918/raspberry-pi-airplay-tutorial

* Standard Audio auf Klinke stellen:
http://cagewebdev.com/index.php/raspberry-pi-getting-audio-working/

It you get the following error message:

ALSA lib pcm.c:2217:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.front
Edit the file /usr/share/alsa/alsa.conf:

sudo nano /usr/share/alsa/alsa.conf
change the line "pcm.front cards.pcm.front" to "pcm.front cards.pcm.default"


+ WLAN Stick einrichten mit statischer IP:
http://kerneldriver.wordpress.com/2012/10/21/configuring-wpa2-using-wpa_supplicant-on-the-raspberry-pi/

* SSH Server automatisch starten bei Boot:
http://askubuntu.com/questions/3913/start-ssh-server-on-boot

* Mouse input events abfangen:

