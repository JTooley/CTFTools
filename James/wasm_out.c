/* Preamble: 
	Decompiled Web Assembly generated by wasmdec.
	Note: this section of code isn't decompiled webassembly,
	just support functions in cased decompiled code requires it

*/
#include <stdint.h> // For the bit size specific types
#include <math.h> // For certian WASM operations
typedef const char* wasm_table_t; // WASM tables
// Bit size specific types not declared in stdint.h:
typedef float float32_t;
typedef double float64_t;
// C implementation of WASM expressions:
unsigned int _rotl(const unsigned int value, int shift) {
	if ((shift &= sizeof(value) * 8 - 1) == 0)
		return value;
	return (value << shift) | (value >> (sizeof(value)*8 - shift));
}
unsigned int _rotr(const unsigned int value, int shift) {
	if ((shift &= sizeof(value) * 8 - 1) == 0)
		return value;
	return (value >> shift) | (value << (sizeof(value)*8 - shift));
}
#define MAX(a,b) ((a) > (b) ? a : b)
#define MIN(a,b) ((a) < (b) ? a : b)
// Host functions: used to request information from host machine.
extern int32_t host_has_feature(int32_t feature_opcode);
extern void host_grow_memory(int32_t size);
extern int32_t host_get_current_memory(void);
extern int32_t host_get_page_size(void);
// End of preamble

// WASM globals:
extern int gimport$0; /* import */
int global$0 = 0;
int global$1 = 0;
const int global$2 = 5242880;

int f0() {
	// Parsed WASM function locals:
	int local0; 
	if (	*(void*)(local0 = 	*(void*)(gimport$0 + 5242880)) != 76) {
	return 1;

	} // <No else block>
	if (	*(void*)(local0) != 111) {
	return 1;

	} // <No else block>
	if (	*(void*)(local0) != 119) {
	return 1;

	} // <No else block>
	if (	*(void*)(local0) != 32) {
	return 1;

	} // <No else block>
	if (	*(void*)(local0) != 108) {
	return 1;

	} // <No else block>
	if (	*(void*)(local0) != 101) {
	return 1;

	} // <No else block>
	if (	*(void*)(local0) != 118) {
	return 1;

	} // <No else block>
	if (	*(void*)(local0) != 101) {
	return 1;

	} // <No else block>
	if (	*(void*)(local0) == 108) {
	*(void*)(local0) != 32
	} else {
	1
	}}
int f1(int local0) {
local0 ^ 559108179}
int f2() {
	f1(	*(void*)(	*(void*)(gimport$0 + 5242880)));
 != 1433609018}
int f3(int local0) {
local0 + -16712191}
int f4() {
	// Parsed WASM function locals:
	int local0; 
	if (	f3(	*(void*)(local0 = 	*(void*)(gimport$0 + 5242880)));
 != 1629578089) {
	return 1;

	} // <No else block>
	f3(	*(void*)(local0));
 != 544567654}
int f5() {
	// Parsed WASM function locals:
	int local0; 
	local0 = 	f0();
;
	f2();
 + local0 + 	f4();
}
void f6() {
	// <Nop expression>
}
void f7() {
	global$0 = gimport$0;
	global$1 = global$0 + 5242880	f6();
}
