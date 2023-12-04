#include "../helpers.h"

struct Copies {
  int length;
  int *copies;
  int capacity;
};

void initCopies(struct Copies *copies, int capacity) {
  copies->capacity = capacity;
  copies->copies = (int *)malloc(sizeof(int) * copies->capacity);

  for (int i = 0; i < copies->capacity; i++) {
    copies->copies[i] = 0;
  }
}

void resizeCopies(struct Copies *copies, int length) {
  if (length >= copies->capacity) {
    int prev_cap = copies->capacity;
    copies->capacity = 2 * copies->capacity;
    copies->copies =
        (int *)realloc(copies->copies, sizeof(int) * copies->capacity);
    for (int i = prev_cap; i < copies->capacity; i++) {
      copies->copies[i] = 0;
    }
  }
}

int get_number_matches(char *line) {
  int i = 0;
  while (!isdigit(line[i])) {
    i++;
  }
  int id = parse_digit(line, &i);

  int winning[10];
  int length = 0, count = 0;

  while (line[i] != '|') {
    if (isdigit(line[i])) {
      winning[length++] = parse_digit(line, &i);
    }
    i++;
  }

  int digit;
  while (i < strlen(line) && line[i] != '\0' && line[i] != '\n') {
    if (isdigit(line[i])) {
      digit = parse_digit(line, &i);
      for (int j = 0; j < length; j++) {
        if (digit == winning[j]) {
          count++;
          break;
        }
      }
    } else {
      i++;
    }
  }

  return count;
}

int parse_p1(char *content) {
  char *line = strtok(content, "\n");
  int i = 1, answer = 0, line_score;

  while (line != NULL) {
    line_score = get_number_matches(line);
    if (line_score != 0) {
      answer += (int)(pow(2.0, (double)(line_score - 1)) + 0.5);
    }

    line = strtok(0, "\n");
    i++;
  }
  return answer;
}

int parse_p2(char *content) {
  char *line = strtok(content, "\n");
  int line_score;

  struct Lines lines;
  initLines(&lines);

  struct Copies copies;
  initCopies(&copies, lines.capacity);

  while (line != NULL) {
    line_score = get_number_matches(line);

    if (line_score) {
      resizeCopies(&copies, lines.length + line_score);
      for (int i = 1; i <= line_score; i++) {
        copies.copies[lines.length + i] += 1;
      }
    }

    resizeLines(&lines);
    appendLine(&lines, line);

    line = strtok(0, "\n");
  }

  int answer = lines.length;
  for (int i = 1; i < lines.length; i++) {
    int line_score;
    answer += copies.copies[i];

    line_score = get_number_matches(lines.lines[i]);
    for (int j = 1; j <= line_score; j++) {
      copies.copies[i + j] += copies.copies[i];
    }
  }

  for (int i = 0; i < lines.length; i++) {
    free(lines.lines[lines.length]);
  }
  free(lines.lines);
  free(copies.copies);

  return answer;
}

int main(int argc, char *argv[]) {
  if (argc == 1) {
    printf("Need file name\n");
    return 0;
  }

  char *content = read_file(argv[1]);
  char *content_cpy = (char *)malloc(sizeof(char) * strlen(content));

  memcpy(content_cpy, content, strlen(content));
  int p1 = parse_p1(content_cpy);

  memcpy(content_cpy, content, strlen(content));
  int p2 = parse_p2(content_cpy);

  printf("p1: %d\np2: %d\n", p1, p2);

  free(content_cpy);
  free(content);
}
