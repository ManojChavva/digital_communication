#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void other(char *str, int len)
{
int i;
FILE *fp;
double c;
fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{

fprintf(fp,"%lf\n",-2*log(1-(double)rand()/RAND_MAX));
}
fclose(fp);
}


int  main(void) //main function begins
{
 
other("other.dat", 1000000);

return 0;
}
