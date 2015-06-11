# Raspberry Pi
We use Raspberry Pi's as low-cost servers to run our various software.


## Installing Raspbian
We chose Raspbian as our operating system because it is the most popular
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


## First Steps
The following steps comes from [this blog post by
phoet](http://nofail.de/2013/01/pulling-strings-on-raspberry-pi/)
> After the PI has booted from the provided Image on the SD-Card, it is
> accessible through SSH:
```
ssh pi@10.0.1.2
```
> It’s a good idea to copy the SSH public key to the machine, so that you do
> not have to type in the passphrase everytime:
```
ssh pi@10.0.1.2 "mkdir -p .ssh"
scp ~/.ssh/id_dsa.pub pi@10.0.1.2:.ssh/authorized_keys
```


## Configuring the Wifi
The plug-and-play wireless USB adapters never seem to live up to the
plug-and-play name. However, after configuring two Raspberry Pi's, I think I
understand what settings you need to change so that the Raspberry Pi can
connect to your wireless network automatically on startup.

### Verify Wireless Adapter Works
First, verify that the wireless adapter works. You can do this by running `sudo
iwlist wlan0 scan`, which will list all available Wifi networks.

### Configure Network Interfaces
There are two different `interfaces` files in this directory. One called
`interfaces` and one called `interfaces-dhcp`. The first one assigns a static
IP address to the Raspberry Pi so that other computers can consistently connect
to it. This is how our Raspberry Pis are configured and we think this is a
sensible option. If you prefer to use dynamic IP addresses, you can skip the
following subsection and continue reading from [Configuring WiFi
credentials](#configuring-wifi-credentials).

#### Configuring Static IP addresses
Refer to [this
article](http://www.modmypi.com/blog/tutorial-how-to-give-your-raspberry-pi-a-static-ip-address).
You need to replace two variables with the values found in that blog post:
- `AAA.AAA.A.AA` refers to the IP address you want use for your Raspberry Pi.
- `BBB.BBB.B.BB` refers to the IP address of your router

After finding these two variables, replace them with the values you found from
the blog post on lines 6, 8, 13, 15.

#### Configuring WiFi Credentials
In either `interfaces` or `interfaces-dhcp`, you need to change lines 16 and 17
to the name of the WiFi network you want to connect to and its password,
respectively. If you decide to use `interfaces-dhcp`, then rename this to
`interfaces` when you use this file on your Raspberry Pi.

Reboot your Raspberry Pi (`sudo reboot`) and it should automatically connect to
the network!


## General
When you've confirmed everything's working, update the software on the
Raspberry Pi:
```
sudo apt-get update
sudo apt-get upgrade
```

### Deploying with Git
It's much easier to develop on my personal computer and to deploy to a Raspberry Pi
than it is to maintain two separate Git repos and have to manually merge them together
every time one makes a change. To that end, I have started deploying projects to the
Raspberry Pi so that all modifications are made on my local computer (instead of making
some changes on local and some on the Raspberry Pi). [See this helpful Digital Ocean
article](https://www.digitalocean.com/community/tutorials/how-to-set-up-automatic-deployment-with-git-with-a-vps)
for more information on how to set up deployment via git.
