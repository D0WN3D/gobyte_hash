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
    "07bccd469a3ae38788480e9b9b03f792ae92f7341a105df83f5c01053b00000" +
    "8fdd266981ce175c6797f8dddda0a032b8c26e92cc23423bfefd77d5fd6cd0a0"
    "019c0d5a" +
    "f0ff0f1e" +
    "874e0400")
#Little-endian Big-endian
best_hash = 'a29cd5d2b7cbd14a4bb3434674f59a421541b11cc875383fae1bf01f8a0c0000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_gobyte_hash(self):
        self.pow_hash = hexlify(gobyte_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

