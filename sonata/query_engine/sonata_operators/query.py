#!/usr/bin/env python
#  Author:
#  Arpit Gupta (arpitg@cs.princeton.edu)


class Query(object):
    """
    Abstract Query Class
    """
    basic_headers = ['ipv4.hdrChecksum', 'tcp.dport', 'ethernet.dstMac', 'udp.len', 'tcp.ctrl',
                     'ethernet.srcMac', 'udp.sport', 'udp.dport', 'tcp.res', 'ipv4.ihl', 'ipv4.diffserv',
                     'ipv4.totalLen', 'ipv4.dstIP', 'ipv4.flags', 'ipv4.proto', 'udp.checksum', 'tcp.seqNo',
                     'ipv4.ttl', 'tcp.ackNo', 'ipv4.srcIP', 'ipv4.version', 'ipv4.identification', 'tcp.ecn',
                     'tcp.window', 'tcp.checksum', 'tcp.dataOffset', 'ipv4.fragOffset', 'tcp.sport',
                     'tcp.urgentPtr', 'ethernet.ethType']
<<<<<<< HEAD
    payload_headers = ['dns.ns.type', 'dns.qdcount','dns.qd.qname', 'dns.qd.ttl']
=======
    payload_headers = ['dns.ns.type', 'dns.ancount','dns.an.rrname', 'dns.an.ttl']
>>>>>>> b83e2640160edda4f631dc95f71c54f1ba12c114
    refinement_headers = ["ipv4.dstIP", "ipv4.srcIP"]

    def __init__(self, *args, **kwargs):
        self.fields = []
        self.keys = []
        self.values = []
        self.expr = ''
        self.name = ''

    def get_init_keys(self):
        return self.keys

    def eval(self):
        """
        evaluate this policy
        :param ?
        :type pkt: ?
        :rtype: ?
        """
        return self.expr