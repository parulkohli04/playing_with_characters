#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    char ch;
    char s[24];
    char t[100];
    
    scanf("%c", &ch);
    scanf("%s", s);
    getchar();
    scanf("%[^\n]%*c", t);
    
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", t);
    return 0;
}
