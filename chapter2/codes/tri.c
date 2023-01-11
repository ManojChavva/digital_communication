#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void uniform(char *str, int len)
{
int i;
FILE *fp;
double n1,n2;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
//fprintf(fp,"%lf\n",(double)rand()/RAND_MAX+(double)rand()/RAND_MAX);
n1 = (double)rand()/RAND_MAX;
n2 = (double)rand()/RAND_MAX;
fprintf(fp,"%lf\n",n1+n2);
}
}
int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("triangle.dat", 1000000);

//Gaussian random numbers
//gaussian("gau.dat", 1000000);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}
