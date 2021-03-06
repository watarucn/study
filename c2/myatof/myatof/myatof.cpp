// myatof.cpp: 定义控制台应用程序的入口点。
//将字符串s转换为双精度小数，合法输入模式为：(+)123.45(e-7)

#include "stdafx.h"
#define MAXLINE 1000

int get_lines(char[], int);
double myatof(char[]);
double power(int sign, int pow);

int main()
{
	char source[MAXLINE];

	while (get_lines(source, MAXLINE) != 2)
		printf_s("%f\n", myatof(source));


	return 0;
}

int get_lines(char source[], int max)
{
	int c = 0;
	int i = 0;
		while (--max > 0 && (c = getchar()) != EOF && c != '\n' && c != '#')
			source [i++] = c;
	if (c == '\n')
	{
		source[i++] = '\n';
		source[i] = '\0';
		return 0;
	}
	else if (c == '#')
	{
		source[i++] = '#';
		source[i] = '\0';
		return 2;
	}
	else return 1;
}

double myatof(char source[])
{
	int i, sign ,sign2= 0;
	double result = 0;
	double pow = 1;
	int pow2 = 0;

	for (i = 0; isspace(source[i]); i++)
		;
	sign = (source[i] == '-' ? -1 : 1);
	if (source[i] == '+' || source[i] == '-')
		i++;
	for (i; isdigit(source[i]); i++)
		result = 10 * result + (source[i] - '0');
	if (source[i] == '.')
		i++;
	for (i; isdigit(source[i]); i++)
	{
		result = 10 * result + (source[i] - '0');
		pow *= 10;
	}
	if (source[i] == 'e' || source[i] == 'E')
		i++;
	sign2 = (source[i] == '-' ? -1 : 1);
	if (source[i] == '+' || source[i] == '-')
		i++;
	for (i; isdigit(source[i]); i++)
		pow2 = 10 * pow2 + (source[i] - '0');

	result = sign*(result / pow) * power(sign2,pow2);

	return result;
}

double power(int sign,int pow)
{
	if (pow == 0)
		return 1;
	if (sign == 1)
	{
		if (pow == 1)
			return 10;
		else
			return 10 * power(sign, --pow);
	}
	else
	{
		if (pow == 1)
			return 0.1;
		else
			return 0.1 * power(sign, --pow);
	}

}