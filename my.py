"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.node import RemoteController, Controller

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
        Gate1 = self.addHost('r1')
        Gate2 = self.addHost('r2')
        Switch = self.addSwitch( 's1' )
        # rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( Host1, Switch)
        self.addLink( Host2, Switch)
        self.addLink( Host3, Switch)
        self.addLink( Host4, Switch)
        self.addLink( Gate1, Switch)
        self.addLink( Gate2, Switch)
        
        Host1.setIP('10.0.0.1/24')
        Host1.setMAC('00:00:00:00:00:01')
        Host2.setIP('10.0.0.2/24')
        Host2.setMAC('00:00:00:00:00:02')
        Host3.setIP('10.0.0.3/24')
        Host3.setMAC('00:00:00:00:00:03')
        Host4.setIP('10.0.0.4/24')
        Host4.setMAC('00:00:00:00:00:04')
        Gate1.setIP('10.0.0.5/24')
        Gate1.setMAC('00:00:00:00:00:05')
        Gate2.setIP('10.0.0.5/24')
        Gate2.setMAC('00:00:00:00:00:05')

topos = { 'mytopo': ( lambda: MyTopo() ) }
