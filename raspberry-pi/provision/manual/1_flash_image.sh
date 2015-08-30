#!/bin/sh
# Write Raspberry Pi image to SD card
#

if [ "$#" -ne 1 ]; then
  echo 'usage: ./1_flash.sh image.img'
  exit 1
fi

diskutil unmountDisk /dev/disk1
sudo dd bs=1m if="$1" of=/dev/rdisk1
