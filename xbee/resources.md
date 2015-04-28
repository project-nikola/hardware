# Helpful XBee Resources
[Difference between series 1 and
2](http://www.digi.com/support/kbase/kbaseresultdetl?id=2213)

"One unique benefit of the 802.15.4 Series 1 XBee is that it can have the
DigiMesh firmware installed. DigiMesh is Digi proprietary mesh network protocol
and is directly comparable to ZigBee. This allows a small network to be
implemented as a Star topology, then later converted into a full mesh network
without replacing hardware. A whitepaper comparing DigiMesh and ZigBee can be
found here: http://www.digi.com/pdf/wp_zigbeevsdigimesh.pdf."

According to [this
link](http://www.digi.com/support/kbase/kbaseresultdetl?id=3150), we can
install the DigiMesh firmware onto our series 1 xbee's

[Differences between ZigBee and
DigiMesh](http://www.digi.com/pdf/wp_zigbeevsdigimesh.pdf)


http://www.digi.com/support/forum/3634/setting-up-simple-digimesh-network

I guess, for the most basic setup, configuring Channel and PanId is enough. Let
it be in API disable mode and all rest parameters set to defaults. DigiMesh is
a self healing network and all nodes will join and form mesh without user's
intervention.
