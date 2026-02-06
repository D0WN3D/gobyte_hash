#include "gobyte.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>

// NeoScrypt ==> Scrypt,ChaCha,Salsa20,SHA-256,Blake2s | TODO: maybe implement these separately later
#include "sha3/neoscrypt.h" // Gobyte's NeoScrypt implementation

void gobyte_hash(const char *input, int len, char *output)
{
    // neoscrypt writes 32 bytes directly into the 'output' memory address
    neoscrypt((unsigned char *)input, (unsigned char *)output, 0);
}
