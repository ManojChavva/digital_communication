#include<stdio.h>
#include <stdlib.h>
#include <math.h>
void gaussian(char *str, int len)
{
int i,j;
double temp;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = 0;
for (j = 0; j < 12; j++)
{
temp += (double)rand()/RAND_MAX;
}
temp-=6;
fprintf(fp,"%lf\n",temp);
printf("%lf\n",temp);
}
fclose(fp);

}

double mean(char *str)
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
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;

}


double variance(char *str)

{
int i=0,c;
FILE *fp;
double x, temp=0.0,temp1=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+(x*x);
temp1=temp1+x;
}
fclose(fp);
temp = temp/(i-1);
temp1=temp1/(i-1);
return temp-(temp1*temp1);

}

int main()
{
gaussian("gau.dat",1000000);
printf("Mean is :%lf\n",mean("gau.dat"));
printf("variance is :%lf\n",variance("gau.dat"));

return 0;
}
