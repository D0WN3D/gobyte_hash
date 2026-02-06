import gobyte_hash
import struct
from binascii import unhexlify, hexlify
import unittest

# BLOCK 1 DATA (Straight from gobyted JSON)
VERSION = 536870912
PREV_BLOCK = "0000033b01055cf8df90b01a14734cae92f7039b9b0e48887b4e33a469d7bc07"
MERKLE_ROOT = "a0d06cd65fd7feef3b4223cc926ec2b8320a0ddddf8779c6571ce169826dd58f"
TIMESTAMP = 1510848001
BITS = 0x1e0ffff0
NONCE = 320604

# THE TARGET: BLOCK 1 HASH (RPC 'hash' field)
BEST_HASH = "00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2"

def get_block_header():
    # < = Little Endian
    # I = 4 bytes (uint32_t)
    header = struct.pack("<I", VERSION)
    header += unhexlify(PREV_BLOCK)[::-1]  # Reverse to internal LE
    header += unhexlify(MERKLE_ROOT)[::-1] # Reverse to internal LE
    header += struct.pack("<I", TIMESTAMP)
    header += struct.pack("<I", BITS)
    header += struct.pack("<I", NONCE)
    return header

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.block_header = get_block_header()
        self.best_hash = BEST_HASH

    def test_gobyte_hash(self):
        # 1. Get raw PoW hash (32 bytes)
        raw_hash = gobyte_hash.getPoWHash(self.block_header)
        
        # 2. Reverse to match RPC string format
        self.pow_hash = hexlify(raw_hash[::-1]).decode()
        
        print(f"\nHeader Hex: {hexlify(self.block_header).decode()}")
        print(f"Calculated: {self.pow_hash}")
        print(f"Target:     {self.best_hash}")
        
        self.assertEqual(self.pow_hash, self.best_hash)

if __name__ == '__main__':
    unittest.main()
