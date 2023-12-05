#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct IntArray {
  int length;
  int *array;
  int capacity;
};

struct IntArray * initArray();
struct IntArray *copyArray(struct IntArray *array);
void resizeArray(struct IntArray *array);
void appendArray(struct IntArray *array, int nmbr);
void freeArray(struct IntArray *array);
struct IntArray *parseIntsFromString(char *content);

struct Lines {
  int length;
  char **lines;
  int capacity;
};

char *read_file(char *file_path);

int parse_digit(char *line, int *i);

struct Lines * initLines();
void resizeLines(struct Lines *lines);
void appendLine(struct Lines *lines, char *line);
void freeLines(struct Lines *lines);
void parseLines(struct Lines *lines, char *delim, char *content);
