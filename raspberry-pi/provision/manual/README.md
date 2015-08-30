# Manual instructions

Download a Raspbian image from [the official site](https://www.raspberrypi.org/downloads/)
into this directory.

1. Flash SD card with Raspbian
  1. `./1_flash.sh image.img`
2. Configure with sane raspi-config settings
  1. Run raspbi-config on Raspberry Pi and change the following settings:

  ```
  1 Expand Filesystem
  2 Change User Password
  4 Internationalisation Options
    I1 Change Locale
    I2 Change Timezone
  8 Advanced Options
    A2 Hostname
    A4 SSH
    A8 Serial
  ```

3. Configure WiFi with dynamic IP address
  1. Modify `/etc/network/interfaces` on the Raspberry Pi

    ```
    # /etc/network/interfaces
    auto lo
    iface lo inet loopback

    auto eth0
    allow-hotplug eth0
    iface eth0 inet manual

    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet dhcp
    wpa-ssid "YOUR_SSID"
    wpa-psk "YOUR_PASSWORD"
    ```
  2. Restart WiFi:

    ```bash
    sudo ifdown wlan0
    sudo ifup wlan0
    ```
