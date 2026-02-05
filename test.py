import gobyte_hash
from binascii import unhexlify, hexlify

import unittest

# gobyte block #1
# moo@b1:~/.gobyte$ gobyted getblockhash 1
# 00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2
# moo@b1:~/.gobyte$ gobyted getblock # 00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2
#{
#   "hash": "00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2",
#   "confirmations": 1534987,
#   "size": 179,
#   "height": 1,
#   "version": 536870912,
#   "versionHex": "20000000",
#   "merkleroot": "a0d06cd65fd7feef3b4223cc926ec2b8320a0ddddf8779c6571ce169826dd58f",
#   "tx": [
#     "a0d06cd65fd7feef3b4223cc926ec2b8320a0ddddf8779c6571ce169826dd58f"
#   ],
#   "time": 1510848001,
#   "mediantime": 1510848001,
#   "nonce": 320604,
#   "bits": "1e0ffff0",
#   "difficulty": 0.000244140625,
#   "chainwork": "0000000000000000000000000000000000000000000000000000000000200020",
#   "nTx": 1,
#   "previousblockhash": "0000033b01055cf8df90b01a14734cae92f7039b9b0e48887b4e33a469d7bc07",
#   "nextblockhash": "000006413fc948dc46cd4da718b0bf59d2abfa81c06703db56e7642102581e46",
#   "chainlock": false
# }

#Little-endian Big-endian
header_hex = ("20000000" +
    "073bd7d4334ae3878df805b14b01f000e92f743b9b9b0e48887b4e33a469d7bc0" +
    "58dd269816ce169c6579f8dddd0a3282b8c26e92cc23423befedf75fd66cd0a0"
    "5a0d9a5a" +
    "f0ff0f1e" +
    "4e040004")
#Little-endian Big-endian
best_hash = 'A29CD5D2B7CBD14A4BB3434674F59A421541B11CC875383FAE1BF01F8A0C0000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_gobyte_hash(self):
        self.pow_hash = hexlify(gobyte_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

