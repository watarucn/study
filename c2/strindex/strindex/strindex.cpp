// strindex.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#define MAXLINE 1000

int getline_s(char line[], int max);
int strindex(char source[], char searchfor[]);

char pattern[] = "ould";

int main(void)
{
	char line[MAXLINE];
	int found = 0;
	int i = 0;
	while (getline_s(line, MAXLINE) > 0) {

		if (strindex(line, pattern) >= 0) {
			printf_s("%s", line);
			found++;
		}
	}
	getchar();
	return found;
}

int getline_s(char s[], int lim)
{
	int c, i;
	i = 0;
	while (--lim>0 && (c = getchar()) != EOF && c != '\n')
		s[i++] = c;
	if (c == '\n')
		s[i++] = c;
	s[i] = '\0';
	return i;
}

int strindex(char s[], char t[])
{
	int i, j, k;

	for (i = 0; s[i] != '\0'; i++) {
		for (j = i, k = 0; t[k] != '\0' && s[j] == t[k]; j++, k++)
			;
		if (k>0 && t[k] == '\0')
			return i;
	}
	return -1;
}

