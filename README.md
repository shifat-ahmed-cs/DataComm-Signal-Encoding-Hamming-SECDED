# DataComm: Physical & Data Link Layer Protocol & Modulation Simulator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![Domain: Networking](https://img.shields.io/badge/domain-Data%20Communications-blue.svg)]()
[![Academic: BRACU CSE320](https://img.shields.io/badge/course-CSE%20320-orange.svg)]()

## 📌 Course Context: CSE 320 (Data Communications)
*Department of Computer Science and Engineering, BRAC University*  
**Core Principles:** Signal Encoding Techniques (NRZ, Manchester, AMI), Transmission Impairments, Error Detection (CRC-16/32), Forward Error Correction (Hamming Codes), and Flow Control ARQ Protocols.

---

## 🎯 Communication Layers & Protocols Implemented

1. **Digital Line Coding Schemes:**
   - **Polar NRZ-L & NRZ-I:** Level vs Differential inversion.
   - **Manchester Encoding:** Guaranteed self-synchronizing transition at each bit center.
   - **Bipolar AMI:** Alternate mark inversion eliminating DC bias.
2. **CRC-16-CCITT Error Detection:**
   - Generator Polynomial: $G(x) = x^{16} + x^{12} + x^5 + 1$ (`0x1021`).
   - Bitwise shift-and-XOR hardware simulation.
3. **Hamming(7, 4) Single-Bit Forward Error Correction:**
   - Parity check matrix syndrome decoding: corrects single-bit transmission noise without retransmission.

---

## 🚀 Quickstart & Testing
```bash
# Run demonstration
python main.py

# Run unit tests
python -m unittest discover -s tests
```
