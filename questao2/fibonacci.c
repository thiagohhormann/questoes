#include <stdio.h>
#include <stdlib.h>

int is_in_fibonacci(int number)
{
    int old_f = 0, f = 1, sum = 0;

    for (int i = 0; i <= number+2; i++)
    {
        old_f = f;
        f = sum;

        if (sum == number)
        {
            return 1;
        };

        sum = old_f + f;
    }
    return 0;
}

int main()
{
    int number, loop_control = 1;
    char *answer;

    while (loop_control)
    {
        printf("Type a number to see if it is in the fibonacci sequence: ");
        scanf("%d", &number);

        if (is_in_fibonacci(number))
        {
            answer = "The number is in the sequence.";
        }
        else
        {
            answer = "The number is not in the sequence.";
        };

        printf("%s\n", answer);
        printf("If you want to continue, type [1]\nIf not, type [0]\n");
        scanf("%d", &loop_control);
    }
} 