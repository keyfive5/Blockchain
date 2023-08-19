import hashlib

from Block import Block

blockchain = []

genesis_block = Block("I will end world hunger", ["Victor sent 1 BTC to Adam",
                                                  "Ayaan sent 5 BTC to Mustafa",
                                                  "Victor sent 5 BTC to GSE-Faarxn"])

second_block = Block(genesis_block.block_hash, ["Adam sent 5 BTC to Feroz"])

third_block = Block(genesis_block.block_hash, ["A to C 5 BTC", "G to D 4 BTC"])

print("Block hash: Genesis Block")
print(genesis_block.block_hash)

print("Block hash: Second Block")
print(second_block.block_hash)

print("Block hash: Third Block")
print(third_block.block_hash)
