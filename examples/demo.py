"""
Demonstration of DataComm: Line Coding, CRC-16 Frame Check, and Hamming(7,4) Single-Bit Correction.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.line_coding import nrz_l, nrz_i, manchester, bipolar_ami
from src.error_control import CRC, HammingCode74

def main():
    print("=" * 65)
    print("       DATACOMM: DATA COMMUNICATIONS & PROTOCOL SUITE        ")
    print("=" * 65)

    # 1. Line Coding Analysis
    bitstream = [1, 0, 1, 1, 0, 0, 1]
    print(f"[+] Bitstream: {bitstream}")
    print(f"    - Polar NRZ-L   : {nrz_l(bitstream)}")
    print(f"    - Polar NRZ-I   : {nrz_i(bitstream)}")
    print(f"    - Bipolar AMI   : {bipolar_ami(bitstream)}")
    print(f"    - Manchester    : {manchester(bitstream)}")

    # 2. CRC-16 Checksum
    payload = b"BRAC_UNIVERSITY_CSE"
    checksum = CRC.compute_crc16(payload)
    transmitted_frame = payload + checksum.to_bytes(2, byteorder='big')
    is_valid = CRC.verify_crc16(transmitted_frame)
    print(f"\n[+] CRC-16 CCITT Verification:")
    print(f"    - Payload: {payload.decode('ascii')}")
    print(f"    - Computed Checksum: 0x{checksum:04X}")
    print(f"    - Frame Valid: {is_valid}")

    # Corrupt a byte in transmission
    corrupted_frame = bytearray(transmitted_frame)
    corrupted_frame[4] ^= 0xFF
    print(f"    - Corrupted Frame Verification: {CRC.verify_crc16(bytes(corrupted_frame))}")

    # 3. Hamming(7, 4) Error Correction
    data_nibble = (1, 0, 1, 1)
    encoded = HammingCode74.encode(data_nibble)
    print(f"\n[+] Hamming(7, 4) Error Correction:")
    print(f"    - Original Data Nibble : {data_nibble}")
    print(f"    - Transmitted 7-bit Code: {encoded}")

    # Introduce single-bit error at position 5 (index 4)
    noisy = list(encoded)
    noisy[4] ^= 1
    decoded, err_pos = HammingCode74.decode_and_correct(tuple(noisy))
    print(f"    - Received with Error  : {tuple(noisy)}")
    print(f"    - Error Detected at Bit: Position {err_pos}")
    print(f"    - Corrected Data Output: {decoded}")
    print("=" * 65)

if __name__ == "__main__":
    main()
