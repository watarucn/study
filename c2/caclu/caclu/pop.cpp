#include "stdafx.h"

int sp = 0;
double val[MAXVAL];
double pop(void)
{
	if (sp > 0)
	{
		return val[--sp];

	}
	else 
	{
		printf_s("ջ����");
		return 0.0;
	}
}