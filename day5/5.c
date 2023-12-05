#include "../helpers.h"

int parse_p1(char *content) {
  int answer = 0;
  struct Lines lines;
  parseLines(&lines, "\n", content);

  freeLines(&lines);
  return answer;
}

int parse_p2(char *content) {
  char *line = strtok(content, "\n\n");
  int answer = 0;

  while (line != NULL) {
    line = strtok(0, "\n");
  }
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
