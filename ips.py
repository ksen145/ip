import ipaddress

def ipnum(ip):
    return int(ipaddress.IPv4Address(ip))

def nlead0_32(x):
    z = 0
    print('x', x)
    while x > 0:
        x >>= 1
        z += 1
    print('z', z)
    return 32 - z

def largest_mask(ips):
    prev_ip = ipnum(ips[0])
    min_lead = 32
    for ip in ips[1:]:
        lead0 = nlead0_32(prev_ip ^ ipnum(ip))
        print('prev_ip', prev_ip, 'ipnum(ip)', ipnum(ip), 'lead0', lead0)
        min_lead = min(min_lead, lead0)
    ones = (1 << min_lead) - 1
    return ipaddress.ip_address(prev_ip & (ones << (32 - min_lead)))

ips = ['192.168.0.1', '192.168.0.5' , '192.168.3.4', '192.168.2.143']

print(largest_mask(ips))
