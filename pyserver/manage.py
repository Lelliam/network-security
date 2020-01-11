#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import data
import time
import threading
from winpcapy import *
import ctypes
import pymysql

# conn = pymysql.connect('xxxx','root','123456','network')
#
# cursor = conn.cursor()
# sql = "INSERT INTO USER1(name, age) VALUES ('ss', 'ss'),('ss','ss'),();"
# username = "Alex"
# age = 18
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交事务
#     conn.commit()
# except Exception as e:
#     # 有异常，回滚事务
#     conn.rollback()
#
# cursor.close()
# conn.close()

def GetData():
    conn = pymysql.connect('xxxx','root','123456','network')
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    times = 0
    sqlinsert = "insert into test1(Time) values"
    T = ""
    sqlquery = "select * from test1"
    try:
    # 执行SQL语句
        cursor1.execute(sqlquery)
        for TestTime in cursor1.fetchall():
            times = times+1
            #print(TestTime)
    # 提交事务
        conn.commit()
    except Exception as e:
    # 有异常，回滚事务
        conn.rollback()
    try:
        while(times):
            cursor2.execute("insert into test1(Time) values('%s')" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))
            conn.commit()
            times = times - 1
    except Exception as e:
        conn.rollback()
    cursor1.close()
    cursor2.close()
    conn.close()




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
        else:
            etherHead["Protocol Type"] = '无'

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


            ## analyze TCP header
            if (ipv4proto) == "0x06":
                tcpHead = {
                    "time":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                    "Source port number": (packet[ds] << 8) + packet[ds + 1],
                    "Destination port number": (packet[ds + 2] << 8) + packet[ds + 3],
                    "Window size": (packet[ds + 14] << 8) + packet[ds + 15]
                }
                packetHead.append(["TCP Information", tcpHead])


            ## analyze UDP header
            if (ipv4proto) == "0x11":
                udpHead = {
                    "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                    "Source port number": (packet[ds] << 8) + packet[ds + 1],
                    "Destination port number": (packet[ds + 2] << 8) + packet[ds + 3],
                    "Length": (packet[ds + 4] << 8) + packet[ds + 5],
                }
                packetHead.append(["UDP Information", udpHead])
        print(packetHead)
        DataResult = {}
      except KeyboardInterrupt:
        win_pcap.stop()
        sys.exit(0)

def main():
    cap = WinPcapUtils()
    '''WinPcapUtils.capture_on_and_print("*Intel**Ethernet*")'''
    cap.capture_on("*Ethernet*",CallBack.packet_printer_callback)

if __name__ == '__main__':
    GetData()
