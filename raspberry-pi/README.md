# Raspberry Pi

## Provisioning

1. [Manual Configuration](provision/manual/README.md)
  1. Flash SD card with Raspbian
  2. Configure with sane raspi-config settings
  3. Configure easy dynamic IP address
2. [Automatic Configuration](provision/automatic/README.md)
  1. Configure static IP address
  2. Enable SSH Pub Key usage
  3. Update + install dev tools


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
