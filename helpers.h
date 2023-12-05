#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct LongArray {
  int length;
  long *array;
  int capacity;
};

struct Stack {
  int length;
  long **stack;
  int capacity;
};

long *pop(struct Stack *stack);
void push(struct Stack *stack, long *node);
void freeStack(struct Stack *stack);
struct Stack *initStack();

struct LongArray *initArray();
struct LongArray *copyArray(struct LongArray *array);
void resizeArray(struct LongArray *array);
void appendArray(struct LongArray *array, long nmbr);
void freeArray(struct LongArray *array);
struct LongArray *parseIntsFromString(char *content);

struct Lines {
  int length;
  char **lines;
  int capacity;
};

char *read_file(char *file_path);

long parse_digit(char *line, int *i);

struct Lines *initLines();
void resizeLines(struct Lines *lines);
void appendLine(struct Lines *lines, char *line);
void freeLines(struct Lines *lines);
void parseLines(struct Lines *lines, char *delim, char *content);
