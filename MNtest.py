from mininet.topo import Topo
class Router_Topo(Topo):
    def __init__(self):
        "Create P2P topology."
        # Initialize topology
        Topo.__init__(self)
        # Add hosts and switches
        H1 = self.addHost('ah1')
        H4 = self.addHost('h4')
        H2 = self.addHost('h2')
        H3 = self.addHost('h3')
        S1 = self.addSwitch('s1')
        # Add links
        self.addLink(H1, S1)
        self.addLink(H4, S1)
        self.addLink(H2, S1)
        self.addLink(H3, S1)
topos = {
    'router': (lambda: Router_Topo())
}
