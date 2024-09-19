# aspu_project
# ARP Spoofing Detection and Prevention Tool

This project is a Python-based ARP Spoofing detection and prevention tool, designed to dynamically detect trusted devices on a local network and monitor for potential ARP poisoning attacks. It can also block attackers using `iptables` and reset ARP entries.

## Features

- Dynamically detect trusted IP and MAC addresses on the local network.
- Monitor ARP traffic and detect spoofing attempts.
- Block attackers using `iptables` rules.
- Harden the network by disabling IP forwarding and enforcing static ARP entries.
- Logging of ARP spoofing events.

## Requirements

- **Python 3.x**
- **scapy** package: `pip install scapy`
- Root privileges for modifying network configurations and running `iptables`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/arp-spoofing-tool.git
   cd arp-spoofing-tool
