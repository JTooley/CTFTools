#include <iostream>
#include <bitset>
#include <unistd.h>

int main()
{
  uint32_t ciphertext = 0x92B552EB;
  uint32_t target_plaintext = 0x3CFC1EB6;


  for (uint32_t i = 0; i < 8192; i++)
  {
    uint32_t sr1 = i;
    uint32_t sr1_out = 0;
    for (int b = 0; b < 32; b++)
    {
      sr1_out |= ((sr1 & 0x1) << (31-b));

      int fb = (sr1 & 0x1); // 0 
      fb ^= (sr1 & 0x8) >> 3; // 3
      fb ^= (sr1 & 0x10) >> 4; // 4
      fb ^= (sr1 & 0x200) >> 9; // 9

      sr1 = sr1 >> 1;
      sr1 |= fb << (13-1);
    }

    for (uint32_t j = 0; j < 256; j++)
    {
      uint32_t sr2 = j;
      uint32_t sr2_out = 0;
      for (int b = 0; b < 32; b++)
      {
        sr2_out |= ((sr2 & 0x1) << (31-b));

        int fb = (sr2 & 0x1); // 0 
        fb ^= (sr2 & 0x2) >> 1; // 1
        fb ^= (sr2 & 0x8) >> 3; // 3
        fb ^= (sr2 & 0x20) >> 5; // 5

        sr2 = sr2 >> 1;
        sr2 |= fb << (8-1);
      }

      for (uint32_t k = 0; k < 32; k++)
      {
        uint32_t sr3 = k;
        uint32_t sr3_out = 0;
        for (int b = 0; b < 32; b++)
        {
          sr3_out |= ((sr3 & 0x1) << (31-b));

          int fb = (sr3 & 0x1); // 0 
          fb ^= (sr3 & 0x2) >> 1; // 1
          fb ^= (sr3 & 0x4) >> 2; // 2
          fb ^= (sr3 & 0x10) >> 4; // 4

          sr3 = sr3 >> 1;
          sr3 |= fb << (5-1);
        }

        uint32_t keystream = (sr1_out & sr2_out) ^ (~sr1_out & sr3_out);
        uint32_t plaintext = keystream ^ ciphertext;

        if (plaintext == target_plaintext)
        {
          std::cout << "DONE!!" << std::endl;
          std::cout << std::bitset<13>(i) << " " << std::bitset<8>(j) << " " << std::bitset<5>(k) << std::endl;
          return 0;
        }
      }
    }
    std::cout << "." << std::flush;
  }
}