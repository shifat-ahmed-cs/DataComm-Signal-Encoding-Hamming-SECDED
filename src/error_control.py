"""
Error Detection & Correction: CRC-16 / CRC-32 and Hamming(7, 4) SECDED Code.
"""
from typing import Tuple, List

class CRC:
    # CRC-16-CCITT polynomial: x^16 + x^12 + x^5 + 1 -> 0x1021
    POLY_16 = 0x1021

    @classmethod
    def compute_crc16(cls, data: bytes) -> int:
        crc = 0xFFFF
        for byte in data:
            crc ^= (byte << 8)
            for _ in range(8):
                if crc & 0x8000:
                    crc = ((crc << 1) ^ cls.POLY_16) & 0xFFFF
                else:
                    crc = (crc << 1) & 0xFFFF
        return crc

    @classmethod
    def verify_crc16(cls, frame: bytes) -> bool:
        """Verifies frame where last 2 bytes are big-endian CRC16."""
        if len(frame) < 2:
            return False
        data, received_crc = frame[:-2], int.from_bytes(frame[-2:], byteorder='big')
        return cls.compute_crc16(data) == received_crc

class HammingCode74:
    """Standard (7, 4) Hamming Code with 4 data bits and 3 parity bits."""
    @staticmethod
    def encode(d: Tuple[int, int, int, int]) -> Tuple[int, int, int, int, int, int, int]:
        d1, d2, d3, d4 = d
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4
        return (p1, p2, d1, p3, d2, d3, d4)

    @staticmethod
    def decode_and_correct(r: Tuple[int, int, int, int, int, int, int]) -> Tuple[Tuple[int, int, int, int], int]:
        """Returns ((d1, d2, d3, d4), error_position) where error_position 0 means no error."""
        p1, p2, d1, p3, d2, d3, d4 = r
        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4
        syndrome = s1 + 2 * s2 + 4 * s3

        corrected = list(r)
        if syndrome > 0:
            corrected[syndrome - 1] ^= 1  # Correct single-bit error

        return (corrected[2], corrected[4], corrected[5], corrected[6]), syndrome
