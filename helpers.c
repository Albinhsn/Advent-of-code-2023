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
struct LongArray *parseLongsFromLine(struct String *line) {
  struct LongArray *array = initArray();
  int i = 0;
  while (i < line->length) {
    if (isdigit(line->string[i])) {
      appendArray(array, parse_digit(line->string, &i));
    } else {
      i++;
    }
  }

  return array;
}

long parse_digit(char *line, int *i) {
  int prev = *i;
  while (isdigit(line[*i])) {
    (*i)++;
  }
  int diff = *i - prev;

  char *id_str = malloc(sizeof(char) * (diff + 1));
  memcpy(id_str, &line[prev], diff);
  id_str[diff] = '\0';

  long id = atol(id_str);

  free(id_str);
  return id;
}

static inline void resizeStringArray(struct StrArray *array) {
  if (array->length >= array->capacity) {
    array->capacity *= 2;
    array->array = (struct String *)realloc(
        array->array, sizeof(struct String) * array->capacity);
  }
}

void appendString(struct StrArray *array, char *string) {
  struct String str;
  str.string = string;
  str.length = strlen(string);
  resizeStringArray(array);
  array->array[array->length++] = str;
}

void freeStringArray(struct StrArray *array) {
  free(array->array);
  free(array);
}

struct StrArray *initStringArray() {
  struct StrArray *array = (struct StrArray *)malloc(sizeof(struct StrArray));
  array->length = 0;
  array->capacity = 8;
  array->array =
      (struct String *)malloc(sizeof(struct String) * array->capacity);

  return array;
}

struct StrArray *parseLines(char *delim, char *content) {
  struct StrArray *array = initStringArray();
  char *line = strtok(content, delim);
  while (line != NULL) {
    resizeStringArray(array);
    appendString(array, line);
    line = strtok(0, delim);
  }

  return array;
}

struct LongArray *copyArray(struct LongArray *array) {
  struct LongArray *newArray = initArray();
  for (int i = 0; i < array->length; ++i) {
    appendArray(newArray, array->array[i]);
  }

  return newArray;
}

void sortLongArray(struct LongArray *array) {
  for (int i = 0; i < array->length - 1; ++i) {
    for (int j = i + 1; j < array->length; j++) {
      if (array->array[i] < array->array[j]) {
        long tmp = array->array[i];
        array->array[i] = array->array[j];
        array->array[j] = tmp;
      }
    }
  }
}

struct LongArray *initArray() {
  struct LongArray *array =
      (struct LongArray *)malloc(sizeof(struct LongArray));
  array->length = 0;
  array->capacity = 16;
  array->array = (long *)malloc(sizeof(long) * array->capacity);

  return array;
}

void resizeArray(struct LongArray *array) {
  if (array->length >= array->capacity) {
    array->capacity = 2 * array->capacity;
    array->array =
        (long *)realloc(array->array, sizeof(long) * array->capacity);
  }
}

void appendArray(struct LongArray *array, long nmbr) {
  resizeArray(array);
  array->array[array->length++] = nmbr;
}

inline void freeArray(struct LongArray *array) {
  free(array->array);
  free(array);
}

struct LongArray *parseIntsFromString(char *content) {
  struct LongArray *array = initArray();
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

long concatDigitsFromLine(struct String string) {
  int count = 0;
  long nmbr = 0;
  int i = (int)string.length - 1;
  while (i >= 0) {
    if (isdigit(string.string[i])) {
      nmbr += (string.string[i] - '0') * pow(10, count);
      count++;
    }
    i--;
  }
  return nmbr;
}
