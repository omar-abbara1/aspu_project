from scapy.all import ARP, Ether, srp
import concurrent.futures

def arp_scan(ip):
    arp_pack = ARP(pdst=ip)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req = ether_frame / arp_pack
    result = srp(arp_req, timeout=2, verbose=False)[0]
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def scan_network(ip_range, threads=100):
    ip_list = [f"192.168.1.{i}" for i in range(1, 255)]
    devices = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(arp_scan, ip): ip for ip in ip_list}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                devices.extend(result)
    
    return devices

ip_range = "192.168.1.1/24"
devices = scan_network(ip_range, threads=50)

for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")

