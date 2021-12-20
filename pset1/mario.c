#include <stdio.h>
#include <cs50.h>
int main(void)
{
   // vaiable
    int num;
    // for imput value from 1 to 8
    do
    {
        num = get_int("enter a number: ");
    }
    while (num <= 0 || num > 8);
    // loop
    for (int n1 = 0; n1 < num; n1++)
    {
        // nasted loop
        for (int n2 = 0; n2 < num; n2++)
    {
        if (n1 + n2 < num - 1)
        {
            printf(" ");
        }
        else
        {
           printf("#");
        }

    }
   printf("\n");
    }
}


