#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct IntArray {
  int length;
  int *array;
  int capacity;
};

struct Int2DArray {
  int length;
  struct IntArray *array;
  int capacity;
};

struct String {
  uint64_t length;
  char *string;
};

struct StrArray {
  int length;
  struct String *array;
  int capacity;
};

struct LongArray {
  int length;
  long *array;
  int capacity;
};

struct Tuple {
  int start;
  int end;
};

struct QNode {
  struct QNode *next;
  struct QNode *prev;
  long value;
};

struct Queue {
  struct QNode *head;
  struct QNode *tail;
};

struct LongArray *initArray();
struct LongArray *copyArray(struct LongArray *array);
void appendArray(struct LongArray *array, long nmbr);
void freeArray(struct LongArray *array);

char *read_file(char *file_path);

long parse_digit(char *line, int *i);

void appendString(struct StrArray *array, char *string);
void freeStringArray(struct StrArray *array);

struct LongArray *parseIntsFromString(char *content);
struct LongArray *parseLongsFromLine(struct String *line);
struct StrArray *parseLines(char *delim, char *content);
long concatDigitsFromLine(struct String string);
