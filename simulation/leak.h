#ifndef LEAK_H
#define LEAK_H

/**
 * available leakage types:
 *   - HW: 32-bit Hamming weight leakage
 *   - HW_BYTE: 8-bit Hamming weight leakage, i.e. the HW of each byte is leaked
 *   - HD_L: Hamming distance between LEFT operand and result is leaked
 *   - HD_R: Hamming distance between RIGHT operand and result is leaked
 */
enum leakage_type {HW, HD_L, HD_R, HW_BYTE};

/**
 * opening a new file and starting to leak into it.
 * binary format: unsigned char (i.e. 8 bit per sample)
 */
void leak_start(enum leakage_type,  const char *filename);

/**
 * pausing the leakge, but doesn't close the leakage file
 */
void leak_pause();
/**
 * resuming lekage after leakge has been paused
 */
void leak_resume();
/**
 * stoping leakage and closing leakage file
 */
void leak_end();

/**
 * leaking initializion operation
 * result = left + 0;
 */
unsigned int leak_uint_init(unsigned int left);
/**
 * leaking right shift operation
 * result = left >> right;
 */
unsigned int leak_uint_rightshift(unsigned int left, unsigned int right);
/**
 * leaking left shift operation
 * result = left << right;
 */
unsigned int leak_uint_leftshift(unsigned int left, unsigned int right);
/**
 * leaking binary OR operation
 * result = left | right;
 */
unsigned int leak_uint_or(unsigned int left, unsigned int right);
/**
 * leaking binary AND operation
 * result = left & right;
 */
unsigned int leak_uint_and(unsigned int left, unsigned int right);
/**
 * leaking XOR operation
 * result = left ^ right;
 */
unsigned int leak_uint_xor(unsigned int left, unsigned int right);
/**
 * leaking binary not operation
 * result = ~left;
 */
unsigned int leak_uint_not(unsigned int left);
/**
 * leaking minus operation (32 bit modular subtraction)
 * result = left - right;
 */
unsigned int leak_uint_minus(unsigned int left, unsigned int right);
/**
 * leaking plus operation (32 bit modular addition)
 * result = left + right;
 */
unsigned int leak_uint_plus(unsigned int left, unsigned int right);
/**
 * leaking division operation (32 bit integer division)
 * result = left / right;
 */
unsigned int leak_uint_div(unsigned int left, unsigned int right);




#endif
