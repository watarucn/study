// strindex2.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#define MAXLINE 1000

int get_lines(char[], int);
int strrindex(char[], char[]);

int main(void)
{
	char search[] = "ould";
	char line[MAXLINE];
	int index = 0;

	while (get_lines(line, MAXLINE) != 2)
	{
		if ((index = strrindex(line, search)) >= 0)
		{
			printf_s("%d\n", index + 1);
			printf_s("%s", line);
		}
	}

	return 0;
}

int get_lines(char line[], int max)
{
	int c = 0;
	int i = 0;
	while (--max>0 && (c = getchar()) != EOF && c != '\n' && c != '#')
		line[i++] = c;
	if (c == '\n')
	{
		line[i++] = '\n';
		line[i] = '\0';
		return 0;
	}
	else if (c == '#')
	{
		line[i++] = '#';
		line[i] = '\0';
		return 2;
	}
	else return 1;
}

int strrindex(char line[], char search[])
{
	int i, j, k = 0;
	int pos = -1;
	for (i = 0; line[i] != '\0'; i++)
	{
		for (j = i, k = 0; line[j] == search[k]; j++, k++)
			;
		if (k>0 && search[k] == '\0')
			pos = i;
	}

	return pos;
}
