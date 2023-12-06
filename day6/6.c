#include "../helpers.h"
#include <math.h>
#include <stdint.h>

int solve_p1(char *content) {
  struct StrArray *lines = parseLines("\n", content);
  struct LongArray *times = parseLongsFromLine(&lines->array[0]);
  struct LongArray *distances = parseLongsFromLine(&lines->array[1]);
  long answer = 1;
  for (int i = 0; i < times->length; ++i) {
    long score = 0;
    long time = times->array[i];
    long dist = distances->array[i];
    for (int j = 1; j < time; j++) {
      if (dist < j * (time - j)) {
        score++;
      }
    }

    answer *= score;
  }
  freeStringArray(lines);
  freeArray(times);
  freeArray(distances);
  return answer;
}

long solve_p2(char *content) {
  struct StrArray *lines = parseLines("\n", content);
  long answer = 0;
  long time = concatDigitsFromLine(lines->array[0]);
  long dist = concatDigitsFromLine(lines->array[1]);
  for (int j = 1; j < time; j++) {
    if (dist < j * (time - j)) {
      answer++;
    }
  }

  freeStringArray(lines);

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
  int p1 = solve_p1(content_cpy);

  memcpy(content_cpy, content, strlen(content));
  int p2 = solve_p2(content_cpy);

  printf("p1: %d\np2: %d\n", p1, p2);

  free(content_cpy);
  free(content);
}
