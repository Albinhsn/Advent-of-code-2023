#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Lines {
  char **lines;
  int length;
};

struct Visited {
  int length;
  int arr[5000][2];
};

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

bool have_visited(struct Visited *visited, int x, int y) {
  for (int i = 0; i < visited->length; i++) {
    if (x == visited->arr[i][0] && y == visited->arr[i][1]) {
      return true;
    }
  }
  return false;
}

struct Lines parse(char *content) {
  struct Lines lines;
  lines.lines = (char **)malloc(sizeof(char *) * 4);
  lines.length = 0;
  int capacity = 4;

  char *line = strtok(content, "\n");
  while (line != NULL) {
    if (lines.length >= capacity) {
      capacity *= 2;
      lines.lines = realloc(lines.lines, sizeof(char *) * capacity);
    }
    lines.lines[lines.length++] = line;
    line = strtok(0, "\n");
  }
  return lines;
}

int found_neighbour(struct Visited *visited, char *line, int x, int y) {
  int start = x, end = x;
  do {
    start--;
  } while (start >= 0 && start < strlen(line) && isdigit(line[start]));
  start++;

  do {
    end++;
  } while (end >= 0 && end < strlen(line) && isdigit(line[end]));

  if (have_visited(visited, start, y)) {
    return 0;
  }

  int diff = end - start;
  char *nmbr_str = malloc(sizeof(char) * (diff + 1));
  memcpy(nmbr_str, &line[start], diff);
  nmbr_str[diff] = '\0';

  int nmbr = atoi(nmbr_str);

  free(nmbr_str);

  int arr[2] = {start, y};
  memcpy(visited->arr[visited->length], &arr, sizeof(arr));
  visited->length++;

  return nmbr;
}

int solve_p2(char *content) {
  struct Lines lines = parse(content);
  int XY[8][2] = {{1, 0}, {-1, 0}, {0, 1},  {0, -1},
                  {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

  struct Visited visited;
  visited.length = 0;

  int answer = 0;
  int x, y;
  for (int i = 0; i < lines.length; ++i) {

    char *line = lines.lines[i];
    for (int j = 0; j < strlen(line); j++) {

      if (line[j] == '*') {
        bool found = false;
        int first_nmbr = -1;

        for (int k = 0; k < 8; k++) {
          x = j + XY[k][0];
          y = i + XY[k][1];

          if (x < 0 || x >= strlen(line) || y < 0 || y >= lines.length) {
            continue;
          }

          if (isdigit(lines.lines[y][x])) {
            int nmbr = found_neighbour(&visited, lines.lines[y], x, y);
            if (nmbr == 0) {
              continue;
            }

            if (found) {
              answer += first_nmbr * nmbr;
            } else {
              found = true;
              first_nmbr = nmbr;
            }
          }
        }
      }
    }
  }

  free(lines.lines);
  return answer;
}

int solve_p1(char *content) {
  struct Lines lines = parse(content);
  int XY[8][2] = {{1, 0}, {-1, 0}, {0, 1},  {0, -1},
                  {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

  struct Visited visited;
  visited.length = 0;

  int answer = 0;

  int x, y;
  for (int i = 0; i < lines.length; ++i) {

    char *line = lines.lines[i];
    for (int j = 0; j < strlen(line); j++) {

      if (!isdigit(line[j]) && line[j] != '.') {
        for (int k = 0; k < 8; k++) {
          x = j + XY[k][0];
          y = i + XY[k][1];

          if (x < 0 || x >= strlen(line) || y < 0 || y >= lines.length) {
            continue;
          }

          if (isdigit(lines.lines[y][x])) {
            answer += found_neighbour(&visited, lines.lines[y], x, y);
          }
        }
      }
    }
  }

  free(lines.lines);
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
