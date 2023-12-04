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

void initLines(struct Lines *lines) {
  lines->length = 0;
  lines->capacity = 16;
  lines->lines = (char **)malloc(sizeof(char *) * lines->capacity);
}

void resizeLines(struct Lines *lines) {
  if (lines->length >= lines->capacity) {
    lines->capacity = 2 * lines->capacity;
    lines->lines =
        (char **)realloc(lines->lines, sizeof(char *) * lines->capacity);
  }
}

void appendLine(struct Lines *lines, char *line) {
  lines->lines[lines->length] = (char *)malloc((strlen(line) + 1));
  memcpy(lines->lines[lines->length], line, strlen(line));
  lines->lines[lines->length][strlen(line)] = '\0';
  lines->length++;
}
