#include "./helpers.h"

char *read_file(char *file_path) {
  FILE *fp;
  fp = fopen(file_path, "r");
  fseek(fp, 0, SEEK_END);
  long len = ftell(fp);
  fseek(fp, 0, SEEK_SET);

  char *buffer = (char *)malloc(sizeof(char) * len + 1);
  buffer[len] = '\0';
  fread(buffer, len, 1, fp);
  fclose(fp);

  return buffer;
}

int parse_digit(char *line, int *i) {
  int prev = *i;
  while (isdigit(line[*i])) {
    (*i)++;
  }
  int diff = *i - prev;

  char *id_str = malloc(sizeof(char) * (diff + 1));
  memcpy(id_str, &line[prev], diff);
  id_str[diff] = '\0';

  int id = atoi(id_str);

  free(id_str);
  return id;
}

struct Lines *initLines() {
  struct Lines *lines = (struct Lines *)malloc(sizeof(struct Lines));
  lines->length = 0;
  lines->capacity = 16;
  lines->lines = (char **)malloc(sizeof(char *) * lines->capacity);

  return lines;
}

inline void resizeLines(struct Lines *lines) {
  if (lines->length >= lines->capacity) {
    lines->capacity = 2 * lines->capacity;
    lines->lines =
        (char **)realloc(lines->lines, sizeof(char *) * lines->capacity);
  }
}

void appendLine(struct Lines *lines, char *line) {
  resizeLines(lines);

  lines->lines[lines->length] = (char *)malloc((strlen(line) + 1));
  memcpy(lines->lines[lines->length], line, strlen(line));
  lines->lines[lines->length][strlen(line)] = '\0';
  lines->length++;
}

void freeLines(struct Lines *lines) {
  for (int i = 0; i < lines->length; ++i) {
    free(lines->lines[i]);
  }
  free(lines->lines);
}

void parseLines(struct Lines *lines, char *delim, char *content) {
  char *line = strtok(content, delim);
  while (line != NULL) {
    resizeLines(lines);
    appendLine(lines, line);
    line = strtok(0, delim);
  }
}

struct IntArray *copyArray(struct IntArray *array) {
  struct IntArray *newArray = initArray();
  for (int i = 0; i < array->length; ++i) {
    appendArray(newArray, array->array[i]);
  }

  return newArray;
}

struct IntArray *initArray() {
  struct IntArray *array = (struct IntArray *)malloc(sizeof(struct IntArray));
  array->length = 0;
  array->capacity = 16;
  array->array = (int *)malloc(sizeof(int) * array->capacity);

  return array;
}

void resizeArray(struct IntArray *array) {
  if (array->length >= array->capacity) {
    array->capacity = 2 * array->capacity;
    array->array = (int *)realloc(array->array, sizeof(int) * array->capacity);
  }
}

void appendArray(struct IntArray *array, int nmbr) {
  resizeArray(array);
  array->array[array->length++] = nmbr;
}
inline void freeArray(struct IntArray *array) {
  free(array->array);
  free(array);
}
struct IntArray *parseIntsFromString(char *content) {
  struct IntArray *array = initArray();
  int i = 0;
  while (i < strlen(content)) {
    if (isdigit(content[i])) {
      appendArray(array, parse_digit(content, &i));
    } else {
      i++;
    }
  }
  return array;
}
