# RPL Encoding and Decoding Utilities for HP 48

This repository contains utilities designed for encoding and decoding in System RPL for the HP 48 calculator, alongside corresponding Python routines to facilitate these processes.

## Contents

- `DEC.rpl`: RPL routine for decoding.
- `ENC.rpl`: RPL routine for encoding.
- `enc_dec_mod.py`: Python utility for encoding and decoding.
- `charmap.json`: Character mapping file used by the Python scripts.
- `README.md`: This file.

## Overview

The `DEC.rpl` and `ENC.rpl` are RPL routines that can be used directly on the HP 48 calculator, allowing for encoding and decoding operations within the calculator's environment. These routines are complemented by `enc_dec.py` and `enc_dec_mod.py`, which offer similar functionality within a Python environment, providing a bridge between your computer and the HP 48.

## Usage

To use these routines on your HP 48, especially if you are compiling them with the Jazz compiler, it is crucial to transfer `DEC.rpl` and `ENC.rpl` using the Kermit protocol. Given that these files contain strings, the following header is recommended for ensuring a successful transfer and successive compilation:

```
%%HP: T(3)A(R)F(.);
C$ 1843
```

This header helps in preparing the calculator to correctly receive and compile the RPL routines, avoiding common issues related to string handling and file transfer protocols.

## Contributing

Contributions to improve or enhance these utilities are welcome. Please ensure any pull requests are well-documented and tested on actual HP 48 devices when possible.

Thank you for your interest in these RPL encoding and decoding utilities for the HP 48.
