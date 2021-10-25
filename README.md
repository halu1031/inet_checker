# inet_checker
Small Python script that checks the internet connection and blinks if there is no connection.

Resistor with **230Ω**

![GPIO Layout Raspi Zero](https://github.com/iamluhae/inet_checker/blob/main/gpio.png)

Edit **inet_checker.py** script

Add python script to autostart

`sudo nano /etc/rc.local`

Add following code

`sudo python /home/pi/inet_checker.py &`

Reboot Raspberry Pi Zero
