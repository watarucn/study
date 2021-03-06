// caclu.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int main()
{
	int type;
	double op2;
	char s[MAXOP];

	while ((type = getop(s)) != EOF) {
		switch (type)
		{
		case NUMBER:
			push(atof(s));
			break;

		case '+':
			push(pop() + pop());
			break;

		case '*':
			push(pop() * pop());
			break;

		case '-':
			op2 = pop();
			push(pop() - op2);
			break;

		case '/':
			op2 = pop();
			if (op2 != 0.0) {
				push(pop() / op2);
			}
			else {
				printf_s("除数不能为0\n");
			}
			break;

		case '\n':
//			printf_s("\t%8.g\n", pop());
			printf_s("%f\n", pop());
			break;

		default:
			printf_s("输入的东西不对\n");
			break;
		}
	}
	return 0;
}

