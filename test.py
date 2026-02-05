import gobyte_hash
from binascii import unhexlify, hexlify

import unittest

# gobyte block #1
# moo@b1:~/.gobyte$ gobyted getblockhash 1
# 00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2
# moo@b1:~/.gobyte$ gobyted getblockheader 00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2
# {
#   "hash": "00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2",
#   "confirmations": 1535025,
#   "height": 1,
#   "version": 536870912,
#   "versionHex": "20000000",
#   "merkleroot": "a0d06cd65fd7feef3b4223cc926ec2b8320a0ddddf8779c6571ce169826dd58f",
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

# gobyte block #1 info
header_hex = (
    "00000020" +  # version (to HEX then LE) // not sure
    "07bcd769a4334e7b88480e9b9b03f792ae4c73141ab090dff85c05013b030000" +  # prev block (32Bit LE)
    "8fd56d8269e11c57c67987dfdd0d0a32b8c26e92cc23423beffed75fd66cd0a0" +  # merkle root (32Bit LE)
    "01960d5a" +  # time (to HEX then LE) //not sure
    "f0ff0f1e" +  # bits (LE)
    "5ce40400"    # nonce (to HEX then LE) //not sure
)

best_hash = "a29cd5d2b7cbd14a4bb3434674f59a421541b11cc875383fae1bf01f8a0c0000"

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_gobyte_hash(self):
        raw_hash = gobyte_hash.getPoWHash(self.block_header)
        self.pow_hash = hexlify(gobyte_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

