#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>


// steel
int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar k");
        return 1;
    }

    for (int k = 0; k < strlen(argv[1]); k++)
    {
        if (isalpha(argv[1][k]))
        {
            printf("Usage: ./cesar key\n");
            return 1;
        }
    }

    int k = atoi(argv[1]) % 26; // if k is > 26, store the division remainder i
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
// splash
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (!isalpha(plaintext[i]))
        {
            printf("%c", plaintext[i]);
            continue;
        }
// the end
        int ascii_offset = isupper(plaintext[i]) ? 65 : 97;

        int pi = plaintext[i] - ascii_offset;
        int ci = (pi + k) % 26;

        printf("%c", ci + ascii_offset);
    }
// styl
    printf("\n");
    return 0;
}
