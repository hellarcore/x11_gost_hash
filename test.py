import x11_gost_hash
from binascii import unhexlify, hexlify

import unittest

# Sibcoin block #1
# ivan@b1:~/.sibcoin$ sibcoin-cli getblockhash 1
# 0000085b23aeab914465a41fc753d61e0e39ca05d5870e77f6287763928cd9b0
# ivan@b1:~/.sibcoin$ sibcoin-cli getblock 0000085b23aeab914465a41fc753d61e0e39ca05d5870e77f6287763928cd9b0
#{
#    "hash" : "0000085b23aeab914465a41fc753d61e0e39ca05d5870e77f6287763928cd9b0",
#    "confirmations" : 351337,
#    "size" : 186,
#    "height" : 1,
#    "version" : 3,
#    "merkleroot" : "8db686f7eabfe0ba61e2e0601f3bd557a5926da4f68fa96fe1dafa5b98980c91",
#    "tx" : [
#        "8db686f7eabfe0ba61e2e0601f3bd557a5926da4f68fa96fe1dafa5b98980c91"
#    ],
#    "time" : 1431130209,
#    "nonce" : 569046,
#    "bits" : "1e0ffff0",
#    "difficulty" : 0.00024414,
#    "chainwork" : "0000000000000000000000000000000000000000000000000000000000200020",
#    "previousblockhash" : "00000c492bf73490420868bc577680bfc4c60116e7e85343bc624787c21efa4c",
#    "nextblockhash" : "00000722c462136d5a41d80f3a7f36f24777e4276b7e141933649fc47dddd071"
#}

header_hex = ("03000000" +
    "4cfa1ec2874762bc4353e8e71601c6c4bf807657bc6808429034f72b490c0000" +
    "910c98985bfadae16fa98ff6a46d92a557d53b1f60e0e261bae0bfeaf786b68d"
    "61504d55" +
    "f0ff0f1e" +
    "d6ae0800")

best_hash = 'b0d98c92637728f6770e87d505ca390e1ed653c71fa4654491abae235b080000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_x11_gost_hash(self):
        self.pow_hash = hexlify(x11_gost_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

