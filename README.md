# orangepi_pc2_h5_gpio_python

Open source modification based on pyA20

https://www.olimex.com/wiki/A20-OLinuXino-MICRO pyA20 https://pypi.python.org/pypi/pyA20

Installation method:
   - Install python headers (sudo apt-get install python-dev)
   - Clone repo to new gpio dir in your home dir (git clone <git repo url> clone gpio)
   - Chage dir to gpio and run install script (python setup.py install)

Set Scheduled job script for OMV at reboot:
   - sleep 30 && nohup python /root/fan.py &

