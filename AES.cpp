#include <iostream>
#include <iomanip>
#include <cstdint>

constexpr uint8_t AES_BLOCK_SIZE = 16;
constexpr uint8_t AES_ROUND_COUNT = 10;

const uint8_t sBox[256] = {
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16};

const uint8_t rcon[10] = {
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36};

// Substitute Bytes using S-Box
void SubBytes(uint8_t *state)
{
    for (int i = 0; i < AES_BLOCK_SIZE; i++)
    {
        state[i] = sBox[state[i]];
    }
}

// Shift Rows operation
void ShiftRows(uint8_t *state)
{
    uint8_t temp[AES_BLOCK_SIZE];

    // First row (no change)
    temp[0] = state[0];
    temp[1] = state[1];
    temp[2] = state[2];
    temp[3] = state[3];

    // Second row (1 byte shift left)
    temp[4] = state[5];
    temp[5] = state[6];
    temp[6] = state[7];
    temp[7] = state[4];

    // Third row (2 byte shift left)
    temp[8] = state[10];
    temp[9] = state[11];
    temp[10] = state[8];
    temp[11] = state[9];

    // Fourth row (3 byte shift left)
    temp[12] = state[15];
    temp[13] = state[12];
    temp[14] = state[13];
    temp[15] = state[14];

    // Copy back to state
    for (int i = 0; i < AES_BLOCK_SIZE; i++)
    {
        state[i] = temp[i];
    }
}

// Mix Columns operation
void MixColumns(uint8_t *state)
{
    uint8_t temp[AES_BLOCK_SIZE];
    for (int i = 0; i < 4; ++i)
    {
        temp[i * 4 + 0] = (uint8_t)(2 * state[i * 4 + 0]) ^ (uint8_t)(3 * state[i * 4 + 1]) ^ state[i * 4 + 2] ^ state[i * 4 + 3];
        temp[i * 4 + 1] = state[i * 4 + 0] ^ (uint8_t)(2 * state[i * 4 + 1]) ^ (uint8_t)(3 * state[i * 4 + 2]) ^ state[i * 4 + 3];
        temp[i * 4 + 2] = state[i * 4 + 0] ^ state[i * 4 + 1] ^ (uint8_t)(2 * state[i * 4 + 2]) ^ (uint8_t)(3 * state[i * 4 + 3]);
        temp[i * 4 + 3] = (uint8_t)(3 * state[i * 4 + 0]) ^ state[i * 4 + 1] ^ state[i * 4 + 2] ^ (uint8_t)(2 * state[i * 4 + 3]);
    }
    for (int i = 0; i < AES_BLOCK_SIZE; ++i)
    {
        state[i] = temp[i];
    }
}

// Add Round Key operation
void AddRoundKey(uint8_t *state, const uint8_t *roundKey)
{
    for (int i = 0; i < AES_BLOCK_SIZE; i++)
    {
        state[i] ^= roundKey[i];
    }
}

// Key Expansion
void KeyExpansion(const uint8_t *initialKey, uint8_t *roundKeys)
{
    int bytesGenerated = 16; // Initial 16 bytes are the initial key

    // Copy initial key to round keys
    for (int i = 0; i < AES_BLOCK_SIZE; i++)
    {
        roundKeys[i] = initialKey[i];
    }

    int rconIteration = 1;
    uint8_t temp[4];

    while (bytesGenerated < 176)
    {
        // Read 4 bytes for the core
        for (int i = 0; i < 4; i++)
        {
            temp[i] = roundKeys[i + bytesGenerated - 4];
        }

        if (bytesGenerated % 16 == 0)
        {
            // Core schedule part
            temp[0] = sBox[temp[1]] ^ rcon[rconIteration - 1];
            temp[1] = sBox[temp[2]];
            temp[2] = sBox[temp[3]];
            temp[3] = sBox[temp[0]];
            rconIteration++;
        }

        for (int i = 0; i < 4; i++)
        {
            roundKeys[bytesGenerated] = roundKeys[bytesGenerated - 16] ^ temp[i];
            bytesGenerated++;
        }
    }
}

// Encrypted block
void EncryptBlock(uint8_t *block, const uint8_t *roundKeys)
{
    AddRoundKey(block, roundKeys);

    for (int round = 1; round < AES_ROUND_COUNT; round++)
    {
        SubBytes(block);
        ShiftRows(block);
        MixColumns(block);
        AddRoundKey(block, roundKeys + round * AES_BLOCK_SIZE);
    }

    SubBytes(block);
    ShiftRows(block);
    AddRoundKey(block, roundKeys + AES_ROUND_COUNT * AES_BLOCK_SIZE);
}

void PrintState(uint8_t *state)
{
    for (int i = 0; i < AES_BLOCK_SIZE; i++)
    {
        std::cout << std::hex << std::setw(2) << std::setfill('0') << (int)state[i] << " ";
        if ((i + 1) % 4 == 0)
        {
            std::cout << std::endl;
        }
    }
    std::cout << std::endl;
}

void PrintRoundOutput(int round, uint8_t *block)
{
    std::cout << "Round " << round << " Output:" << std::endl;
    PrintState(block);
}

void PrintRoundKeySchedule(int round, const uint8_t *roundKeys)
{
    std::cout << "Round " << round << " Key Schedule:" << std::endl;
    PrintState((uint8_t *)(roundKeys + round * AES_BLOCK_SIZE));
}

int main()
{
    // Sample key and block for testing
    uint8_t initialKey[16] = {0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x97, 0x75, 0x46, 0x20, 0x63, 0xed};
    uint8_t roundKeys[176];
    uint8_t block[16] = {0x32, 0x88, 0x31, 0xe0, 0x43, 0x5a, 0x31, 0x37, 0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34};

    // Generate round keys
    KeyExpansion(initialKey, roundKeys);

    // Print initial block
    std::cout << "Initial Block:" << std::endl;
    PrintState(block);

    // Encrypt block and print rounds
    for (int round = 0; round <= AES_ROUND_COUNT; round++)
    {
        if (round > 0)
        {
            SubBytes(block);
            ShiftRows(block);
            if (round < AES_ROUND_COUNT)
            {
                MixColumns(block);
            }
            AddRoundKey(block, roundKeys + round * AES_BLOCK_SIZE);
        }

        PrintRoundOutput(round, block);
        if (round < AES_ROUND_COUNT)
        {
            PrintRoundKeySchedule(round, roundKeys);
        }
    }

    return 0;
}
