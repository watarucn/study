#include "stdafx.h"
#define BUFSIZE 100

char buf[BUFSIZE];
int bufp = 0;

int getch(void)
{
	return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c)
{
	if (bufp >= BUFSIZE)
		printf_s("Ì«¶àµÄ×Ö·û\n");
	else
		buf[bufp++] = c;
}