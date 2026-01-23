#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re

def main():
    def prtUsage(msg=None):
        if msg is None:
            print("Usage: create V3S bin from uboot bin, v3s dtb bin, openwrt bin", file=sys.stderr)
            print("python createbin uboot.bin v3s_dtb.bin openwrt_sysupgrade.bin", file=sys.stderr)
        else:
            print(msg, file=sys.stderr)

    if len(sys.argv) != 4:
        prtUsage()
        return 1
    
    uboot = open(sys.argv[1], "rb").read()
    if len(uboot) > 0x10000*6:
        print("Too large uboot bin", file=sys.stderr)
        return 1
    elif len(uboot) < 0x10000*2:
        print("Too small uboot bin", file=sys.stderr)
        return 1

    dtb = open(sys.argv[2], "rb").read()
    if len(dtb) > 0x10000:
        print("Too large dtb bin", file=sys.stderr)
        return 1
    elif len(dtb) < 4096:
        print("Too small dtb bin", file=sys.stderr)
        return 1

    openwrt = open(sys.argv[3], "rb").read()
    if len(openwrt) > 0x100000 * 6:
        print("Too large openwrt bin", file=sys.stderr)
        return 1
    elif len(openwrt) < 0x100000:
        print("Too small openwrt bin", file=sys.stderr)
        return 1

    sys.stdout.buffer.write(uboot)
    sys.stdout.buffer.write(b'\xff' * (0x10000*6 - len(uboot)))
    sys.stdout.buffer.write(dtb)
    sys.stdout.buffer.write(b'\xff' * (0x10000 - len(dtb)))
    sys.stdout.buffer.write(openwrt)
    return 0;


if __name__ == '__main__':
    sys.exit(main())    
