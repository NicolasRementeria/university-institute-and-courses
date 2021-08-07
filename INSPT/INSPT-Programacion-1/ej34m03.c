#include <stdio.h>
#include <stdlib.h>

void mostrarNumeros(int n){

    if (n==0){
        ;
    } else {
        printf("%d\n",n);
        mostrarNumeros(n-1);
        printf("%d\n",n);
    }
}

int calcularResto(int dividendo, int divisor){

    if (dividendo-divisor>=divisor){
        // seguir restando
        return calcularResto(dividendo-divisor,divisor);
    } else {
        return dividendo-divisor;
    }
}

int calcularCociente(int dividendo, int divisor){
    return calcularCocienteAux(dividendo, divisor, 0);
}

int calcularCocienteAux(int dividendo, int divisor, int cociente){
    if (dividendo-divisor>=0){
        cociente++;
        return calcularCocienteAux(dividendo-divisor,divisor,cociente);
    } else {
        return cociente;
    }
}

int calcularCuadrado(int valor){

    if (valor==0){
        return 0;
    } else {
        return (2*valor-1) + calcularCuadrado(valor-1);
    }
}

void mostrarFila(int valor){
    if (valor==0){
        printf("\n");
    } else {
        printf("%d",valor);
        mostrarFila(valor-1);
    }
}

void mostrarPiramide(int valor){
   if (valor==0){
        ;
    } else {
        mostrarPiramide(valor-1);
        mostrarFila(valor);
        //printf("%d\n",valor);
    }
}

int main(){
    int x = 5;

    mostrarPiramide(5);
/*
    x=calcularCociente(5,2);
    printf("cociente dividendo=%d\n",x);

    x=calcularCociente(6,2);
    printf("cociente dividendo=%d\n",x);

    x=calcularCuadrado(4);
    printf("Cuadrado=%d\n",x);

    x=calcularResto(5,2);
    printf("resto=%d\n",x);

*/
    return 0;
}

