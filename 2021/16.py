from dataclasses import dataclass
from math import prod

FILENAME = '16-input.txt'

ENCODINGS = { ord('{:X}'.format(i)): '{:04b}'.format(i) for i in range(16) }

@dataclass
class Operator:
    version: int
    type_id: int
    sub_packets: list

    def version_sums(self):
        return self.version + sum(sp.version_sums() for sp in self.sub_packets) 

    def eval(self):
        if self.type_id == 0:
            return sum(sp.eval() for sp in self.sub_packets)
        if self.type_id == 1:
            return prod(sp.eval() for sp in self.sub_packets)
        if self.type_id == 2:
            return min(sp.eval() for sp in self.sub_packets)
        if self.type_id == 3:
            return max(sp.eval() for sp in self.sub_packets)
        if self.type_id == 5:
            return self.sub_packets[0].eval() > self.sub_packets[1].eval()
        if self.type_id == 6:
            return self.sub_packets[0].eval() < self.sub_packets[1].eval()
        if self.type_id == 7:
            return self.sub_packets[0].eval() == self.sub_packets[1].eval()

@dataclass
class Literal:
    version: int
    value: int

    def version_sums(self):
        return self.version

    def eval(self):
        return self.value

def parse_type_4(msg, bits_taken):
    value = ''
    more_segments = True
    while more_segments:
        bits_taken += 5
        group_flag, group, msg = msg[0], msg[1:5], msg[5:]
        more_segments = group_flag == '1'
        value+=group
    return int(value, 2), msg

def parse_by_bytelen(msg):
    sub_packets = []
    num_bits, msg = int(msg[:15], 2), msg[15:]
    sub_msg = msg[:num_bits]
    while sub_msg:
        sub_packet, sub_msg = parse(sub_msg)
        sub_packets.append(sub_packet)
    return sub_packets, msg[num_bits:]

def parse_by_count(msg):
    sub_packets = []
    num_packets, msg = int(msg[:11], 2), msg[11:]
    for i in range(num_packets):
        sub_packet, msg = parse(msg)
        sub_packets.append(sub_packet)
    return sub_packets, msg

def parse(msg):
    packet_version, msg = int(msg[:3], 2), msg[3:]
    packet_type_id, msg = int(msg[:3], 2), msg[3:]
    if packet_type_id == 4:
        value, msg = parse_type_4(msg, 6)
        return Literal(version=packet_version, value=value), msg
    length_type_id, msg = int(msg[0], 2), msg[1:]
    if length_type_id == 0:
        sub_packets, msg = parse_by_bytelen(msg)

    elif length_type_id == 1:
        sub_packets, msg = parse_by_count(msg)

    return Operator(version=packet_version, type_id=packet_type_id, sub_packets=sub_packets), msg

def part_01(msg):
    op, remainder = parse(msg)
    return op.version_sums()

def part_02(msg):
    op, remainder = parse(msg)
    return op.eval()

with open(FILENAME) as f:
    msg = f.read().strip().translate(ENCODINGS)
    print(part_01(msg))
    print(part_02(msg))
