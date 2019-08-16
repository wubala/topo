"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch
#from mininet.topo import Topo
#from mininet.node import RemoteController, Controller

class MyTopo(Topo):
    def __init__(self):
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
"        
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
"
def runMinimalTopo():
    "Bootstrap a Mininet network using the Minimal Topology"
    # Create an instance of our topology
    topo = MyTopo()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController( name, ip='127.0.0.1'  ),
        switch=OVSSwitch,
        autoSetMacs=True 
    )

    # Actually start the network
    net.start()
    # Drop the user in to a CLI so user can run commands.
    CLI( net  )
    # After the user exits the CLI, shutdown the network.
    net.stop()

if __name__ == '__main__':
    # This runs if this file is executed directly
    setLogLevel( 'info'  )
    runMinimalTopo()

topos = { 'mytopo': ( lambda: MyTopo() ) }
