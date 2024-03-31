# RSA-App
DES332-1 Computer Security Assignment. Here's some info:

## Members
- Nachat Kaewmeesang, 6422770774
- Noravorn Tonsirianusorn, 6422781458

## Structure
- Layer based: Each branch reflects each layer. `main` branch is for the finished combined product.
  - There should be 3 folders: `App`, `Protocol`, and `RSA`. In the root folder should be `main.py` for running the entire project.
- `App` our demonstration app, currently undecided. This branch should handle UI and API (with TCP, email, or whatever APIs we need to connect)
- `Protocol` handles file IO, type conversion, and PGP header fields
- `RSA` handles prime numbers, modulo exponentiation, and other functions to encrypt and decrypt

## Project Scope
- Demonstration App: build an end-2-end encryption software using PGP, so that 2 hypothetical users can talk securely
  - End product: a program installed locally on 2 devices that does both sending & recieving. The program should interface with an email API if possible, or simply print out the output to the screen where it can be copied-pasted to Gmail app or Line app.
- RSA and PGP implemented using Python. If there are performance problems in the future, we can always write those portions in Golang, compiled to a _shared library_, then call those functions from python. This way we can modularize certain components (and rewrite them, if need be) without affecting the entire project.

## Requirements
1. Implement RSA algorithm. Should handle
  - keys must be big (2048 bits, at least)
  - Performance should be realistic, but not massive consideration
  - Key Generation
  - Encryption
  - Decryption
  - Can handle both text and binary data
2. Develop an app, implementing both RSA and symmetric.
  - Authentication feature
  - Confidentiality feature
  - Allowance: can call existing symmetric encryption algorithms.
