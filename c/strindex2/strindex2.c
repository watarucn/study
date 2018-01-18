#include <stdio.h>
#define MAXLINE 1000

int get_lines(char [],int);
int strrindex(char [],char[]);

int main(void)
{
	char search[]="ould";
	char line[MAXLINE];

	while (get_lines(line,MAXLINE)!=2)
	{
		if (strrindex(line,search)>=0)
			printf("%s",line);
	}

	return 0;
}

int get_lines(char line[],int max)
{
	int c=0;
	int i=0;
	while (--max>0&& (c=getchar()) != EOF &&c!='\n' && c!='#')
		line[i++]=c;
	if (c=='\n')
	{
		line[i++]='\n';
		line[i]='\0';
		return 0;
	}
	else if (c=='#')
	{
		line[i++]='#';
		line[i]='\0';
		return 2;
	}
	else return 1;
}

int strrindex(char line[],char search[])
{
	int i,j,k=0;
	int pos = -1;
	for(i=0;line[i]!='\0';i++)
	{
		for(j=i,k=0;line[j]==search[k];j++,k++)
			;
		if(k>0&&search[k]=='\0')
			pos = i;
	}
	return pos;
}
