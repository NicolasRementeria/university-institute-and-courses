#include <stdio.h>
#include <stdlib.h>

int main()
{

    /*
        El código morse, también conocido como alfabeto Morse, es un sistema de representación de letras 
        y números mediante señales emitidas de forma intermitente. Construye un programa que permita 
        ingresar un carácter, letra o número y convertirlo en código. Datos:

        A 	· — 	  	N 	— · 	  	0 	— — — — —
        B 	— · · · 	             	1 	· — — — —
        C 	— · — · 	O 	— — — 	  	2 	· · — — —
                     	P 	· — — · 	3 	· · · — —
        D 	— · · 	  	Q 	— — · — 	4 	· · · · —
        E 	· 	  	    R 	· — · 	  	5 	· · · · ·
        F 	· · — · 	S 	· · · 	  	6 	— · · · ·
        G 	— — · 	  	T 	— 	  	    7 	— — · · ·
        H 	· · · · 	U 	· · — 	  	8 	— — — · ·
        I 	· · 	  	V 	· · · — 	9 	— — — — ·
        J 	· — — — 	W 	· — — 	  	
        K 	— · — 	  	X 	— · · — 	
        L 	· — · · 	Y 	— · — — 	 
        M 	— — 	  	Z 	— — · · 	
    */
    char caracter;
    printf("Ingrese letra o numero: ");
    scanf("%c", &caracter);

    switch (caracter)
    {
    case 'a':
    case 'A':
        printf("%c es \' . - \' en morse", caracter);
        break;
    case 'b':
    case 'B':
        printf("%c es \' - . . . \' en morse", caracter);
        break;
    case 'c':
    case 'C':
        printf("%c es \' - . - . \' en morse", caracter);
        break;
    case 'd':
    case 'D':
        printf("%c es \' - . . \' en morse", caracter);
        break;
    case 'e':
    case 'E':
        printf("%c es \' . \' en morse", caracter);
        break;
    case 'f':
    case 'F':
        printf("%c es \' . . - . \' en morse", caracter);
        break;
    case 'g':
    case 'G':
        printf("%c es \' - - . \' en morse", caracter);
        break;
    case 'h':
    case 'H':
        printf("%c es \' . . . . \' en morse", caracter);
        break;
    case 'i':
    case 'I':
        printf("%c es \' . . \' en morse", caracter);
        break;
    case 'j':
    case 'J':
        printf("%c es \' . - - - \' en morse", caracter);
        break;
    case 'k':
    case 'K':
        printf("%c es \' - . - \' en morse", caracter);
        break;
    case 'l':
    case 'L':
        printf("%c es \' . - . . \' en morse", caracter);
        break;
    case 'm':
    case 'M':
        printf("%c es \' - - \' en morse", caracter);
        break;
    case 'n':
    case 'N':
        printf("%c es \' - . \' en morse", caracter);
        break;
    case 'o':
    case 'O':
        printf("%c es \' - - - \' en morse", caracter);
        break;
    case 'p':
    case 'P':
        printf("%c es \' . - - . \' en morse", caracter);
        break;
    case 'q':
    case 'Q':
        printf("%c es \' - - . - \' en morse", caracter);
        break;
    case 'r':
    case 'R':
        printf("%c es \' . - . \' en morse", caracter);
        break;
    case 's':
    case 'S':
        printf("%c es \' . . . \' en morse", caracter);
        break;
    case 't':
    case 'T':
        printf("%c es \' - \' en morse", caracter);
        break;
    case 'u':
    case 'U':
        printf("%c es \' . . - \' en morse", caracter);
        break;
    case 'v':
    case 'V':
        printf("%c es \' . . . - \' en morse", caracter);
        break;
    case 'w':
    case 'W':
        printf("%c es \' . - - \' en morse", caracter);
        break;
    case 'x':
    case 'X':
        printf("%c es \' - . . - \' en morse", caracter);
        break;
    case 'y':
    case 'Y':
        printf("%c es \' - . - - \' en morse", caracter);
        break;
    case 'z':
    case 'Z':
        printf("%c es \' - - . . \' en morse", caracter);
        break;
    case '1':
        printf("%c es \' . - - - - \' en morse", caracter);
        break;
    case '2':
        printf("%c es \' . . - - - \' en morse", caracter);
        break;
    case '3':
        printf("%c es \' . . . - - \' en morse", caracter);
        break;
    case '4':
        printf("%c es \' . . . . - \' en morse", caracter);
        break;
    case '5':
        printf("%c es \' . . . . . \' en morse", caracter);
        break;
    case '6':
        printf("%c es \' - . . . . \' en morse", caracter);
        break;
    case '7':
        printf("%c es \' - - . . . \' en morse", caracter);
        break;
    case '8':
        printf("%c es \' - - - . . \' en morse", caracter);
        break;
    case '9':
        printf("%c es \' - - - - . \' en morse", caracter);
        break;
    case '0':
        printf("%c es \' - - - - - \' en morse", caracter);
        break;
    default:
        printf("%c no se puede traducir a morse", caracter);
        break;
    }

    printf("\n");
    system("pause");

    return 0;
}