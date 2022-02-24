<h1 style="text-align: center;font-weight:bold"><br><br>&#8811;THM NOTES&#8810;<br ></br></h1>
<h3 style="text-align: center;font-weight:bold">&#10629;PRE SECURITY&#10630;<br>Network Fundamentals<br/></br><br></br></h3>


#### &#9312; LAN TOPOLOGIES
<ul>
<li><h5>STAR TOPOLOGY</li></h5>
  Devices are individually connected via a central networking device such as a switch or hub

  Any information sent to a device in this topology is sent *via the central device* to which it connects.

  It is more expensive than any of the other topologies.

  Easy to add more devices as the demand for the network increases.

  If the centralised hardware that connects devices fails, other devices will no longer be able to send or receive data. 

<li><h5>BUS TOPOLOGY</li></h5>
 All data travels along the same cable (backbone cable).

 Prone to becoming slow and bottlenecked,  if backbone cable were to break, devices can no longer receive or transmit data along the bus.

 Difficult to identify which device is experiencing issues with data all travelling along the same route.

 Cost-efficient, easy to set up. 

<li><h5>RING TOPOLOGY</li></h5>
  Also known as Token topology.

  Devices are connected directly to each other to form a loop.
  
  Data is sent across the loop until it reaches the destined device making it easy to troubleshoot but not efficient, because it has to visit many other devices on the way.

  A device will only send received data from another device in this topology if it does not have any to send itself. If the device happens to have data to send, it will send its own data first before sending data from another device.

  Less prone to bottlenecks than bus topology.

  Fault such as cut cable, or broken device will result in the entire networking breaking.
</ul>

#### &#9313; ARP Protocol

ARP - Address Resolution Protocol

A host wishing to obtain a physical address broadcasts an ARP request onto the TCP/IP network. The host on the network that has the IP address in the request then replies with its physical hardware address. 

There is also Reverse ARP (RARP) which can be used by a host to discover its IP address. In this case, the host broadcasts its physical address and a RARP server replies with the host's IP address. 

#### &#9314; DHCP Protocol

DHCP - Dynamic Host Configuration Protocol

When a device first connects to a network it sends out a request (DHCP Discover) to see if any DHCP servers are on the network. The DHCP server then replies back with an IP address the device could use (DHCP Offer). The device then sends a reply confirming it wants the offered IP Address (DHCP Request), and then lastly, the DHCP server sends a reply acknowledging this has been completed, and the device can start using the IP Address (DHCP ACK).

