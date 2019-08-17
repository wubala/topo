#!/usr/bin/python

"""
A simple minimal topology script for Mininet.

Based in part on examples in the [Introduction to Mininet] page on the Mininet's
project wiki.

[Introduction to Mininet]: https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#apilevels
mn --custom sw.py --topo sw
python sw.py
为了测试ovs NXM 
ovs-ofctl add-flow s1 "table=0,in_port=1,priority=33,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00,actions=flood,resubmit(,3)"
ovs-ofctl add-flow s1 "table=0,in_port=2,priority=33,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00,actions=flood,resubmit(,3)"
ovs-ofctl add-flow s1 "table=3,priority=10, actions=learn(table=0, priority=30, NXM_OF_ETH_DST[]=NXM_OF_ETH_SRC[],output:NXM_OF_IN_PORT[])"
"""

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch

class MinimalTopo( Topo  ):
    "Minimal topology with a single switch and two hosts"

    def build( self  ):
    # Create two hosts.
        h1 = self.addHost( 'h1'  )
        h2 = self.addHost( 'h2'  )
        h3 = self.addHost( 'h3'  )
        h4 = self.addHost( 'h4'  )
        ha = self.addHost( 'ha'  )
        hb = self.addHost( 'hb'  )
        hc = self.addHost( 'hc' )
        hd = self.addHost( 'hd' )

        # Create a switch
        s1 = self.addSwitch( 's1'  )
        s2 = self.addSwitch( 's2'  )

        # Add links between the switch and each host
        self.addLink( s1, h1  )
        self.addLink( s1, h2  )
        self.addLink( s1, h3  )
        self.addLink( s1, h4  )
        self.addLink( s1, ha  )
        self.addLink( s1, hb  )
        self.addLink( s2, hc  )
        self.addLink( s2, hd )
    # Actually start the network

def runMinimalTopo():
    "Bootstrap a Mininet network using the Minimal Topology"

    # Create an instance of our topology
    topo = MinimalTopo()


    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
    topo=topo,
    controller=lambda name: RemoteController( name, ip='127.0.0.1'  ),
    #controller=None,
    switch=OVSSwitch ,
    autoSetMacs=True 
    )

    net.start()
    net.get('h1').setIP("1.1.1.1/24")
    net.get('h2').setIP("1.1.1.2/24")
    net.get('h3').setIP("1.1.1.3/24")
    net.get('h4').setIP("1.1.1.4/24")
    net.get('h1').setMAC("00:00:00:00:00:0a")
    net.get('h2').setMAC("00:00:00:00:00:0b")
    net.get('h3').setMAC("00:00:00:00:00:0c")
    net.get('h4').setMAC("00:00:00:00:00:0d")

    # Actually start the network
    # Drop the user in to a CLI so user can run commands.
    CLI( net  )

    # After the user exits the CLI, shutdown the network.
    #net.stop()

if __name__ == '__main__':
    # This runs if this file is executed directly
    setLogLevel( 'info'  )
    runMinimalTopo()

# Allows the file to be imported using `mn --custom <filename> --topo minimal`
topos = {
#'minimal': MinimalTopo
'sw': MinimalTopo
}
"""
"""
