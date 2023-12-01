
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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

int match_substr(char *subbuff) {
  if (strcmp(subbuff, "one") == 0) {
    return 1;
  }
  if (strcmp(subbuff, "two") == 0) {
    return 2;
  }
  if (strcmp(subbuff, "three") == 0) {
    return 3;
  }
  if (strcmp(subbuff, "four") == 0) {
    return 4;
  }
  if (strcmp(subbuff, "five") == 0) {
    return 5;
  }
  if (strcmp(subbuff, "six") == 0) {
    return 6;
  }
  if (strcmp(subbuff, "seven") == 0) {
    return 7;
  }
  if (strcmp(subbuff, "eight") == 0) {
    return 8;
  }
  if (strcmp(subbuff, "nine") == 0) {
    return 9;
  }
  return 0;
}

int match_str(int *arr, char *contents, int i, int len) {
  char subbuff[6];
  int start = i - 2;
  for (int j = 3; j <= 5 && contents[start + j - 1] != '\n'; j++) {
    memcpy(subbuff, &contents[start], j);
    subbuff[j] = '\0';
    int matched = match_substr(subbuff);
    if (matched != 0) {
      arr[len++] = matched;
    };
  }
  return len;
}
int solve_p1(char *contents) {
  int answer = 0, i = 0, len = 0;
  int *arr = (int *)malloc(sizeof(int) * 50);
  while (contents[i] != '\0') {
    if (contents[i] == '\n') {
      answer += arr[0] * 10 + arr[len - 1];
      len = 0;

    } else if (isdigit(contents[i])) {
      arr[len++] = contents[i] - '0';
    }
    i++;
  }
  free(arr);
  return answer;
}

int solve_p2(char *contents) {
  int answer = 0, i = 0, len = 0;
  int *arr = (int *)malloc(sizeof(int) * 50);
  while (contents[i] != '\0') {
    if (contents[i] == '\n') {
      answer += arr[0] * 10 + arr[len - 1];
      len = 0;

    } else if (isdigit(contents[i])) {
      arr[len++] = contents[i] - '0';
    } else if (i >= 2) {
      len = match_str(arr, contents, i, len);
    }
    i++;
  }
  free(arr);
  return answer;
}

int main(int argc, char *argv[]) {
  if (argc == 1) {
    printf("Need file name\n");
    return 0;
  }

  char *contents = read_file(argv[1]);
  int p1 = solve_p1(contents);
  int p2 = solve_p2(contents);

  free(contents);
  printf("p1: %d\np2: %d\n", p1, p2);
}
