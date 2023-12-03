#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define RED 12
#define GREEN 13
#define BLUE 14

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


bool check_valid_set(char *line) {
  int i = 0, red = 0, green = 0, blue = 0;
  while (i < strlen(line)) {
    // parse the digit
    int digit = parse_digit(line, &i);
    // skip whitespace between digit and color
    i++;

    // parse the color
    switch (line[i]) {
    case 'b': {
      blue += digit;
      i += 4;
      break;
    }
    case 'r': {
      red += digit;
      i += 3;
      break;
    }
    case 'g': {
      green += digit;
      i += 5;
      break;
    }
    default: {
      printf("%s\n", line);
      printf("Expected [b,r,g] not '%c', %d\n", line[i], i);
      exit(1);
    }
    }

    // check whether we're done or we continue
    if (i >= strlen(line) || line[i] == ';') {
      if (red > RED || green > GREEN || blue > BLUE) {
        return false;
      }
      red = green = blue = 0;
    }

    i += 2;
  }
  return true;
}

int parse_p1(char *line) {
  int start = 5;
  int id = parse_digit(line, &start);
  start += 3;
  return check_valid_set(&line[start]) ? id : 0;
}

int solve_p1(char *content) {
  char *line = strtok(content, "\n");
  int answer = 0;
  while (line != NULL) {
    answer += parse_p1(line);
    line = strtok(0, "\n");
  }

  return answer;
}

int get_min_valid_set(char *line) {
  int i = 0;

  int min_red = 0, min_green = 0, min_blue = 0;
  int red = 0, green = 0, blue = 0;

  while (i < strlen(line)) {

    int digit = parse_digit(line, &i);
    i++;

    switch (line[i]) {
    case 'r': {
      red += digit;
      i += 3;
      break;
    }
    case 'b': {
      blue += digit;
      i += 4;
      break;
    }
    case 'g': {
      green += digit;
      i += 5;
      break;
    }
    default: {
      printf("Expected [b,r,g] not '%c', %d\n", line[i], i);
      exit(1);
    }
    }
    // check whether we're done or we continue
    if (i >= strlen(line) || line[i] == ';') {
      min_red = min_red < red ? red : min_red;
      min_blue = min_blue < blue ? blue : min_blue;
      min_green = min_green < green ? green : min_green;

      red = green = blue = 0;
    }

    i += 2;
  }
  return min_red * min_blue * min_green;
}

int parse_p2(char *line) {
  int start = 5;
  while (isdigit(line[start])) {
    start++;
  }
  start += 2;
  return get_min_valid_set(&line[start]);
}

int solve_p2(char *content) {
  char *line = strtok(content, "\n");
  int answer = 0;
  while (line != NULL) {
    int line_score = parse_p2(line);
    answer += line_score;
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
  int p1 = solve_p1(content_cpy);

  memcpy(content_cpy, content, strlen(content));
  int p2 = solve_p2(content_cpy);

  printf("p1: %d\np2: %d\n", p1, p2);

  free(content_cpy);
  free(content);
}
