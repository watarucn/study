#include "stdafx.h"
#include <ctype.h>
int getch(void);
void ungetch(int);

int getop(char s[])
{
	int i, c;

	while ((s[0] = c = getch()) == ' ' || c == '\t')
		;
	s[1] = '\0'; //��������if������һ��ֻ��һ���ַ����ַ������� ����[+/0]
	if (!isdigit(c) && c != '.')
		return c;
	
	i = 0;//s[0]�������Ѿ���while���ȷ���ˣ���������ʹ��++i������i++
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