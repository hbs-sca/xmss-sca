# DPA on a SHA256 PRNG
We propose and implement a DPA on a SHA256 PRNG which is similar to the one proposed for W-OTS+ secret key generation within XMSS (https://datatracker.ietf.org/doc/draft-irtf-cfrg-xmss-hash-based-signatures/).

This work was accepted to COSADE 2018:
Matthias J. Kannwischer, Aymeric Genêt, Denis Butin, Juliane Krämer, and Johannes Buchmann, "Differential Power Analysis of XMSS and SPHINCS", COSADE 2018, Singapore (to appear)


## Dependencies
 - https://www.python.org/
 - http://www.numpy.org/
 - https://pypi.python.org/pypi/fixedint/0.1.2

## Quick Start
 - `cd simulation && make && cd ..`
 - 8-bit DPA attack
    - `./simulation/simulate 100 HW_BYTE ca79af4090c3ca6defec33d631704e018b8ca869c5e2ed26f0b65cf8bbdb5c86`
    - `./analysis/analyze_8bit.py leakage_100.bin secret_data.txt`
 - 32-bit DPA attack on AND
    - `./simulation/simulate 2000 HW ca79af4090c3ca6defec33d631704e018b8ca869c5e2ed26f0b65cf8bbdb5c86`
    - `./analysis/analyze_32bit_and.py leakage_2000.bin secret_data.txt 0.5`
 - 32-bit DPA attack on addition
    - `./simulation/simulate 1000 HW ca79af4090c3ca6defec33d631704e018b8ca869c5e2ed26f0b65cf8bbdb5c86`
    - `./analysis/analyze_32bit_addition.py leakage_1000.bin secret_data.txt 0.5`
 - Note: Success of attack depends upon seed. With the seeds above the attacks succeed. If you use different ones you may need more traces.
## Simulating Power Traces
- `make` in [`simulation/`](simulation/) builds the project
- The power simulation can be used by running `./simulation/simulate n t [k]`, e.g. `./simulation/simulate 1000 HW`
- The parameters are
  - `n` : number of traces, PRNG will be executed for indices: 0 <= i < n
  - `t` : leakage type (`HW`, `HW_BYTE`)
  - `k` : optional, 256-bit seed as hex string without 0x
  - If no `k` is given, a random one will be generated
- We implement 2 leakage modes
    - `HW`: leaking the Hamming weight of the result of each 32-bit operation
    - `HW_BYTE` : leaking the Hamming weight of each byte of the result separately (i.e. 4 data points per operation)
- The simulation produces two files
  - `leakage_<n>.bin` containing the `n` power simulation traces in 8 bit unsigned char binary format
  - `secret_data.txt` containing the seed and iv information - required for validating recovered keys later
- Additionally, for development and debugging purposes we implemented [`partial_leak_prng.c`](simulation/partial_leak_prng.c) which only leaks the relevant operations

## Running the DPA Attack
 - We implemented three DPA attack scripts
 - [analyze_8bit.py](analysis/analyze_8bit.py) implements the DPA in the 8-bit HW leakage model.
    - It can be used by running `./analysis/analyze_8bit.py traceFile secretDataFile`
    - The parameters are
      - `traceFile`: path the binary trace file created in the `HW_BYTE` mode
      - `secretDataFile`: path to the secret data file, usually `secret_data.txt`. This is just use for checking the result
  - [analyze_32bit_addition.py](analysis/analyze_32bit_addition.py) implements DPA1 in the 32-bit HW leakage model, i.e., an DPA on addition.
    - It can be used by running `./analysis/analyze_32bit_addition.py traceFile secretDataFile threshold`
    - The parameters are
      - `traceFile`: path the binary trace file created in the `HW` mode
      - `secretDataFile`: path to the secret data file, usually `secret_data.txt`. This is just use for checking the result
      - `threshold`: threshold used for picking key hypothesis. For different numbers of traces, different thresholds are optimal. See [dpa.py](analysis/dpa.py) for details. `0.5` works fine in most of the cases
  - [analyze_32bit_and.py](analysis/analyze_32bit_addition.py) implements DPA5 in the 32-bit HW leakage model, i.e. an DPA on AND
    - It can be used by running `./analysis/analyze_32bit_and.py traceFile secretDataFile threshold`
    - The parameters are
      - `traceFile`: path the binary trace file created in the `HW` mode
      - `secretDataFile`: path to the secret data file, usually `secret_data.txt`. This is used for checking the result AND to get the required values of E_1 (which is computed from D_0 and delta, which were originally recovered in DPA1 and DPA2). This is cheating - but we just wanted to evaluate DPA5.
      - `threshold`: threshold used for picking key hypothesis. For different numbers of traces, different thresholds are optimal. See [dpa.py](analysis/dpa.py) for details. `0.5` works fine in most of the cases
