"""
Unit tests for DataComm line coding and CRC/Hamming algorithms.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.line_coding import nrz_l, bipolar_ami
from src.error_control import CRC, HammingCode74

class TestDataCommunications(unittest.TestCase):
    def test_line_coding(self):
        bits = [1, 0, 1]
        self.assertEqual(nrz_l(bits), [1, -1, 1])
        self.assertEqual(bipolar_ami(bits), [1, 0, -1])

    def test_crc16(self):
        msg = b"Hello World"
        c = CRC.compute_crc16(msg)
        frame = msg + c.to_bytes(2, byteorder='big')
        self.assertTrue(CRC.verify_crc16(frame))
        self.assertFalse(CRC.verify_crc16(msg + b"\x00\x00"))

    def test_hamming74(self):
        nibble = (0, 1, 1, 0)
        codeword = HammingCode74.encode(nibble)
        dec, err = HammingCode74.decode_and_correct(codeword)
        self.assertEqual(dec, nibble)
        self.assertEqual(err, 0)

        # Inject error at position 3
        noisy = list(codeword)
        noisy[2] ^= 1
        dec_corr, err_pos = HammingCode74.decode_and_correct(tuple(noisy))
        self.assertEqual(dec_corr, nibble)
        self.assertEqual(err_pos, 3)

if __name__ == "__main__":
    unittest.main()
