#include <stdio.h>
#include <stdlib.h>

int main(){
    int a, b, c, d =0, e=1; //0 corresponde a falso
    int x=2, y=3;

    // 1) a= 5>3

    //a= 5>3;
    //printf("%d", a );
    
    // rta: 1 (true)

    // 2) b=( (4<5) && (2>2));

    //b = ( (4<5) && (2>2));
    //printf("%d", d );

    // rta: 0 (false)

    // 3) a=!e;

    //a=!e;
    //printf("%d", a );

    // rta: 0 (false)

    // 4) b=((x%2 ==0) || (x-y <10));
    //b=((x%2 ==0) || (x-y <10));
    //printf("%d", b );

    // rta: 1 (true)

    // 5) c=(d && e);
    //c=(d && e);
    //printf("%d", c ); 

    // rta: 0 (false)

    // 6) c=(d || e);

    //c=(d || e);
    //printf("%d", c ); 

    // rta: 1 (true)

    // 7) c=!(d && e);
    //c=!(d && e);
    //printf("%d", c ); 

    // rta: 1 (true)

    // 8) c=(! d) && (!e);
    //c=(! d) && (!e);
    //printf("%d", c ); 

    // rta: 0 (false)

    // 9) c=(a && (!a));
    //c=(a && (!a));
    //printf("%d", c ); 

    // rta: 0 (false)

    //10) c=(((x<=(y*3.2)) &&(y%2!=0))|| (1));
    //c=(((x<=(y*3.2)) &&(y%2!=0))|| (1));
    //printf("%d", c ); 

    // rta: 1 (true)

    return 0;
}