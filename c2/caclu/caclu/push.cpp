#include "stdafx.h"

extern int sp;
extern double val[];
void push(double f)
{
	if (sp < MAXVAL)
		val[sp++] = f;
	else
		printf_s("Õ»ÒÑÂú\n");
}