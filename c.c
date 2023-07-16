// PRANAV K DILEEP CYBER SECURITY ROLL NO 26

//Write a program print the roots of a quadratic equation
#include<stdio.h>
#include<math.h>
int main()
{
    int a,b,c;
    float d,r1,r2;
    printf("Enter the values of a,b,c\n");
    scanf("%d%d%d",&a,&b,&c);
    d=(b*b)-(4*a*c);
    if(d>0)
    {
        printf("Roots are real and distinct\n");
        r1=(-b+sqrt(d))/(2*a);
        r2=(-b-sqrt(d))/(2*a);
        printf("Roots are %f and %f",r1,r2);
    }
    else if(d==0)
    {
        printf("Roots are real and equal\n");
        r1=(-b+sqrt(d))/(2*a);
        printf("Roots are %f and %f",r1,r1);
    }
    else
    {
        r1 = -b/(2*a);
        r2 = sqrt(-d)/(2*a);
        printf("%f + i%f\n",r1,r2);
        printf("%f - i%f\n",r1,r2);
    }
    return 0;
}