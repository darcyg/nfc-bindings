#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generates one ISO14443-A anti-collision process "by-hand"
"""

from __future__ import print_function
import nfc

MAX_FRAME_LEN = 264

abtRx = bytes(0) * MAX_FRAME_LEN

quiet_output = False
force_rats = False
timed = False
iso_ats_supported = False


abtReqa = bytes(0x26)



def transmit_bits(pbtTx, szTxBits):
  
    cycles = 0
    # Show transmitted command
    if not quiet_output:
        print("Sent bits:     ")
        nfc.print_hex_bits(pbtTx, szTxBits)
    
    # Transmit the bit frame command, we don't use the arbitrary parity feature
    if timed:
        szRxBits, pbtRx, cycles = nfc.initiator_transceive_bits_timed(pnd, pbtTx, szTxBits, 0, abtRx, sizeof(abtRx), 0, )
        if szRxBits < 0:
            return False
        if (not quiet_output) and (szRxBits > 0):
            print("Response after %u cycles" % cycles)
        
    else:
        szRxBits, pbtRx = nfc.initiator_transceive_bits(pnd, pbtTx, szTxBits, 0, abtRx, sizeof(abtRx), 0)
        if szRxBits < 0:
            return False
    
    # Show received answer
    if not quiet_output:
        print('Received bits: ')
        nfc.print_hex_bits(abtRx, szRxBits)
    
    # Succesful transfer
    return True






context = nfc.init()
ret, pnd = nfc.open(context, 0)
if ret < 0:
    print('ERROR: Unable to open NFC device.')
    nfc.exit(context)
    exit(1)
    
if(nfc.initiator_init(pnd)<0):
    nfc.perror(pnd, "nfc_initiator_init")
    nfc.close(pnd)
    nfc.exit(context)
    exit(1)
    
    
if (nfc.device_set_property_bool(pnd, nfc.NP_HANDLE_CRC, False) < 0):
    nfc.perror(pnd, "nfc_device_set_property_bool")
    nfc.close(pnd)
    nfc.exit(context)
    exit(1)
  
    
if (nfc.device_set_property_bool(pnd, nfc.NP_EASY_FRAMING, False) < 0):
    nfc.perror(pnd, "nfc_device_set_property_bool")
    nfc.close(pnd)
    nfc.exit(context)
    exit(1)
    
        
if (nfc.device_set_property_bool(pnd, nfc.NP_AUTO_ISO14443_4, False) < 0):
    nfc.perror(pnd, "nfc_device_set_property_bool")
    nfc.close(pnd)
    nfc.exit(context)
    exit(1)
    
print("NFC reader:", nfc.device_get_name(pnd), "opened")

# Send the 7 bits request command specified in ISO 14443A (0x26)
if not transmit_bits(abtReqa, 7):
    print("Error: No tag available")
    nfc.close(pnd)
    nfc.exit(context)
    exit(1)
  
    
    
    