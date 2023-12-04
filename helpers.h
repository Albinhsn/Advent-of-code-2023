#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *read_file(char *file_path);

int parse_digit(char *line, int *i);

struct Lines {
  int length;
  char **lines;
  int capacity;
};

void initLines(struct Lines *lines);
void resizeLines(struct Lines *lines);
void appendLine(struct Lines* lines, char * line);