#include "stdafx.h"
#include <ctype.h>
int getch(void);
void ungetch(int);

int getop(char s[])
{
	int i, c;

	while ((s[0] = c = getch()) == ' ' || c == '\t')
		;
	s[1] = '\0'; //配合下面的if语句完成一个只有一个字符的字符串数组 例如[+/0]
	if (!isdigit(c) && c != '.')
		return c;
	
	i = 0;//s[0]的内容已经被while语句确定了，所以下面使用++i而不是i++
	if (isdigit(c))
		while (isdigit(s[++i] = c = getch()))
			;
	if (c == '.')
		while (isdigit(s[++i] = c = getch()))
			;
	s[i] = '\0';
	
	if (c != EOF)
		ungetch(c);
	return NUMBER;

}