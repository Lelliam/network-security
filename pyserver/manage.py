#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import data
import time
import threading
from winpcapy import *
import ctypes

class CallBack(WinPcapUtils):
    def packet_printer_callback(win_pcap, param, header, pkt_data):
      try:
        packet = []
        for i in range(0,header.contents.len):
            packet.append(pkt_data[i])
        packetHead = []

        src = "%.2x" % packet[0]
        for i in range(1,6):
            src += ":%.2x" % packet[i]

        dst = "%.2x" % packet[6]
        for i in range(7,12):
            dst += ":%.2x" % packet[i]

        proto = "0x%.4x" % ((packet[12]<<8)+packet[13])
        etherHead = {
            "Source":src,
            "Destination":dst
            }
        if proto in data.etherType:
            etherHead["Protocol Type"] = data.etherType[proto]

        packetHead.append(["Ethernet Information",etherHead])

        item = [
            etherHead["Source"],
            etherHead["Destination"],
            etherHead["Protocol Type"]
            ]
        if proto == "0x0800":
            ipv4Head = {
                "Version":packet[14]>>4,
                "Internet Header Length(IHL)":packet[14] % 16,
                "Differentiated Services Code Point (DSCP)":packet[15]>>2,
                "Explicit Congestion Notification (ECN)":packet[15] % 4,
                "Total Length":(packet[16]<<8)+packet[17],
                "Identification":(packet[18]<<8)+packet[19],
                "Flags":packet[20]>>5,
                "Fragment Offset":((packet[20] % 32)<<8)+packet[21],
                "Time To Live (TTL)":packet[22],
                "Header Checksum":(packet[24]<<8)+packet[25],
                "Source IP Address":"%d.%d.%d.%d" % (packet[26], packet[27], packet[28], packet[29] ),
                "Destination IP Address":"%d.%d.%d.%d" % (packet[30], packet[31], packet[32], packet[33] ),
                }
            ipv4proto = "0x%.2x" % packet[23]
            if ipv4proto in data.ipv4Type:
                ipv4Head["Protocol"] = data.ipv4Type[ipv4proto]
            ds = 34
            if ipv4Head["Internet Header Length(IHL)"] > 5:
                ipv4Head["Copied"] = packet[34]>>7
                ipv4Head["Option Class"] = (packet[34]>>5) % 4
                ipv4Head["Option Number"] = packet[34] % 32
                ipv4Head["Option Length"] = packet[35]
                ds = 36
            packetHead.append(["IPv4 Information",ipv4Head])
            item[0] = ipv4Head["Source IP Address"]
            item[1] = ipv4Head["Destination IP Address"]
            item[2] = ipv4Head["Protocol"]
        print(packetHead)
      except KeyboardInterrupt:
        win_pcap.stop()
        sys.exit(0)
def main():
    cap = WinPcapUtils()
    '''WinPcapUtils.capture_on_and_print("*Intel**Ethernet*")'''
    cap.capture_on("*Ethernet*",CallBack.packet_printer_callback)
if __name__ == '__main__':
    main()