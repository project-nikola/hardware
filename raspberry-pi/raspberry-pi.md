# Raspberry Pi
We use Raspberry Pi's as low-cost servers to run our various software.


## Installing Raspbian
We use Raspbian as our operating system of choice. It is the most popular
distribution for Raspberry Pi and has the most support online.

### Download Raspian
[You can download the latest version of Raspbian
here](http://www.raspberrypi.org/downloads/). Verify the sha-1 hash of the
downloaded file. This is especially important if you torrented the file. For
Mac OS X, just run `openssl sha1 downloaded_raspian.zip`.

### Writing an Image to an SD Card
For platform specific instructions, [see the official Raspberry Pi
documentation](http://www.raspberrypi.org/documentation/installation/installing-images/).
Bob Gardner only has experience with writing an image from a Mac, so the other
methods are untested. For a mac:
```
diskutil list
# identify the disk of your SD card
# diskutil unmountDisk /dev/<disk# from diskutil>
diskutil unmountDisk /dev/disk1
sudo dd bs=1m if=image.img of=/dev/disk1
```

In Bob's experience, this command takes longer than a few minutes (about 35
minutes give or take).

### Verify OS installed correctly
To verify that Raspbian has installed correctly, eject the SD card and plug it
into the Raspberry Pi. Then, attach an HDMI or video cable to the Raspberry Pi
and connect it to a nearby computer monitor or television. After plugging in
the power to the Raspberry Pi, you should see various console output appear on
screen. After a minute or two, you should see a configuration screen. Follow
the on screen instructions and you will have successfully installed Raspian on
your Raspberry Pi!


## Configuring the Wifi
The plug-and-play wireless USB adapters never seem to live up to the
plug-and-play name. However, after configuring two Raspberry Pi's, I think I
understand what settings you need to change so that the Raspberry Pi can
connect to your wireless network automatically on startup.

### Verify Wireless Adapter Works
First, verify that the wireless adapter works. You can do this by running `sudo
iwlist wlan0 scan`, which will list all available Wifi networks.

### Configure WPA Supplicant
[Complete the WPA Supplicant configuration
here](http://www.raspberrypi.org/documentation/installation/installing-images/).
Refer to `wpa_supplicant.conf` in this repo as a reference.

### Configure Network Interfaces
Your `/etc/network/interfaces` file should look like the one in this repo.

Reboot your Raspberry Pi (`sudo reboot`) and it should automatically connect to
the network!


## General
When you've confirmed everything's working, update the software on the
Raspberry Pi:
```
sudo apt-get update
sudo apt-get upgrade
```
