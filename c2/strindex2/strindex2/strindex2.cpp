// strindex2.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#define MAXLINE 1000

int get_lines(char l[], int i);
int strindex2(char l[], char p[]);

int main()
{
	char line[MAXLINE];
	char c[] = "ould";

	while (get_lines(line, MAXLINE) != 2)
		if (strindex2(line,c) > 0)
			printf_s("%s", line);

	getchar();

	return 0;
}
int get_lines(char line[], int max)
{
	int c = 0;
	int i = 0;
	while ((c = getchar()) != EOF && c!='\n' && c != '#' && --max > 0)
	{
		 line [i++] = c;
	}
	
	if (c == '\n')
	{
		line [i++] = '\n';
		line [i] = '\0';
		return 0;
	}
	else if (c == '#')
	{
		line [i++] = '#';
		line [i] = '\0';
		return 2;
	}

	return 1;
}

int strindex(char s[],char p[])
{
	int i, j, k = 0;
	for (i = 0; s[i] != '/0'; i++)
		for (j = i, k = 0; s[j] == p[k]; j++, k++)
			;
	if (k > 0 && p[k++] == '\0')
		return i;
	return -1;
}
