#include "../helpers.h"

int solve_p1(char *content) {
  struct Lines *lines = initLines();
  parseLines(lines, "\n", content);
}

long solve_p2(char *content) {}

int main(int argc, char *argv[]) {
  if (argc == 1) {
    printf("Need file name\n");
    return 0;
  }

  char *content = read_file(argv[1]);
  char *content_cpy = (char *)malloc(sizeof(char) * strlen(content));

  memcpy(content_cpy, content, strlen(content));
  int p1 = solve_p1(content_cpy);

  memcpy(content_cpy, content, strlen(content));
  int p2 = solve_p2(content_cpy);

  printf("p1: %d\np2: %d\n", p1, p2);

  free(content_cpy);
  free(content);
}
