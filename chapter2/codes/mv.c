#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"
//Defining the function for calculating the variance of random numbers
double mean11(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x*x;
}
fclose(fp);
temp = temp/(i-1);
return temp;

}

int  main(void) //main function begins
{
 double x,y,var;
//mean of Uniform random numbers
x=mean("uni.dat");
printf("%lf",x);
y=mean11("uni.dat");
var=y-x*x;
printf("%lf",var);
//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}
