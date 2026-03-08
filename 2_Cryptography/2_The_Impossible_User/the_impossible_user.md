**Challenge**

This encryption service will encrypt almost any plaintext. Can you abuse the implementation to actually encrypt every plaintext?

**Solution**

This is an AES-ECB encryption service with a padding oracle-like flaw that allows you to encrypt any plaintext. The attack abuses AES-ECB's block independence to encrypt a forbidden plaintext by including it aligned to block boundaries in a longer allowed plaintext, then extracting the corresponding ciphertext blocks.

Here the message is divided into blocks and each block is encrypted separately.

Make your crafted message- payload
Convert to hex
Get the encryption - Encrypt it via /encrypt?user=...
From result, remove first 32 hex characters
Use remainder with /get_flag?user=...
Get flag!

the encryption works in chunks of 16 letters