/*
 * @Author: Jh Li
 * @github: https://github.com/Aptx4869AC
 * @Created: 2024-01-11
 */

#include "Enclave.h"
#include "Enclave_t.h" /* print_string */
#include <stdarg.h>
#include <stdio.h> /* vsnprintf */
#include <string.h>

/* Implementing the functionality of the trusted function being called */
int printf(const char* fmt, ...)
{
    char buf[BUFSIZ] = { '\0' };
    va_list ap;
    va_start(ap, fmt);
    vsnprintf(buf, BUFSIZ, fmt, ap);
    va_end(ap);
    ocall_print_string(buf);
    return (int)strnlen(buf, BUFSIZ - 1) + 1;
}
void Add(int *res,int a,int b) 
{
	*res=a+b;
}

