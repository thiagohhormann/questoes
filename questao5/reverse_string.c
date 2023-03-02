#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count_char(char str[])
{

    int count = 0;

    while (str[count] != '\0')
    {
        count++;
    }

    return count;
}

char * reverse_string(char *str, int txt_size)
{

    char tmp_string[txt_size + 1];
    char letter;
    int j;
    for (int i = txt_size - 1, j = 0; j <= txt_size; i--, j++)
    {
        tmp_string[j] = str[i];
    }

    tmp_string[txt_size + 1] = '\0';

    str = strcpy(str, tmp_string);
    return str;
}

int main()
{
    int input_size, txt_size;
    char *new_string;

    printf("Digite o tamanho máximo de letras que serão digitadas:\n");
    scanf("%d", &input_size);

    char *string = (char *)malloc(input_size * sizeof(char));
    char *reversed_string = (char *)malloc(input_size * sizeof(char));

    printf("Digite o texto que será invertido:\n");
    scanf("%s", string);

    txt_size = count_char(string);
    new_string = reverse_string(string, txt_size);

    printf("%s\n", new_string);
}