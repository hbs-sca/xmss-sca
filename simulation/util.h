#ifndef UTIL_H
#define UTIL_H
#include <stdlib.h>

void print_hex_uint(const unsigned int *data, int length);
void print_hex(const unsigned char *data, int length);


void uint_to_uchar(unsigned int *in, size_t size, unsigned char *out);

void uchar_to_uint(unsigned char *in, size_t size, unsigned int *out);
void hex_to_uchar(const char *hex, size_t size, unsigned char *out);
#endif
