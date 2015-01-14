# Xbee Configurations
This directory contains Xbee configuration files that can be imported and
exported from the `xctung` program.

There are a three configurations for the Xbees. All Xbees have the same `panid`
(on the same network) and are configured with the correct `DH` and `DL`
settings. After that, each Xbee will have slightly different settings. Every
node should have a different `MY` setting (increment, starting from 0).

## Coordinator
One Xbee will be configured with the `xbee_coordinator_template.xml`. This Xbee
receives data from all other Xbees on the same network (those with the same
`panid`). Notably, this Xbee is set up in `coordinator` mode while all other
Xbees on the same network will use `end-device` mode.

# Energy
Xbees for use in the energy sensors will use the `xbee_energy_template.xml`.
This configures the ports for the amplifier connections from the Kill-A-Watt
(current and voltage data).

## Environmental
Xbees for use in the environmental sensors will use the
`xbee_environmental_template.xml`. These have special configurations for the
light sensors.
