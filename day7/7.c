#include "../helpers.h"

enum Strength {
  HIGH = 0,
  PAIR = 1,
  TWO_PAIR = 2,
  THREE = 3,
  FULL_HOUSE = 4,
  FOUR = 5,
  FIVE = 6
};

struct Hand {
  enum Strength strength;
  int bet;
  struct LongArray *hand;
  char *line;
};

struct HandArray {
  int length;
  int capacity;
  struct Hand *hands;
};

void resizeHandArray(struct HandArray *array) {
  if (array->length >= array->capacity) {
    array->capacity *= 2;
    array->hands = (struct Hand *)realloc(array->hands, sizeof(struct Hand) *
                                                            array->capacity);
  }
}

int parseHandStrengthP2(struct LongArray *array) {
  struct LongArray *found = initArray();
  struct LongArray *count = initArray();

  bool flag;
  int jokers = 0;
  for (int i = 0; i < array->length; ++i) {
    flag = false;
    if (array->array[i] == 1) {
      jokers++;
      continue;
    }
    for (int j = 0; j < found->length; ++j) {
      if (found->array[j] == array->array[i]) {
        count->array[j]++;
        flag = true;
        break;
      }
    }
    if (!flag) {
      appendArray(found, array->array[i]);
      appendArray(count, 1);
    }
  }
  sortLongArray(count);

  switch (count->array[0]) {
  case 5: {
    return FIVE;
  }
  case 4: {
    if (jokers == 1) {
      return FIVE;
    }
    return FOUR;
  }
  case 3: {
    if (count->length >= 2 && count->array[1] == 2) {
      return FULL_HOUSE;
    }
    if (jokers == 2) {
      return FIVE;
    }
    if (jokers == 1) {
      return FOUR;
    }
    return THREE;
  }
  case 2: {
    if (count->array[1] == 2) {
      if (jokers == 1) {
        return FULL_HOUSE;
      }
      return TWO_PAIR;
    }
    if (jokers == 3) {
      return FIVE;
    }
    if (jokers == 2) {
      return FOUR;
    }
    if (jokers == 1) {
      return THREE;
    }
    return PAIR;
  }
  default: {
    if (jokers == 5) {
      return FIVE;
    }
    if (jokers == 4) {
      return FIVE;
    }
    if (jokers == 3) {
      return FOUR;
    }
    if (jokers == 2) {
      return THREE;
    }
    if (jokers == 1) {
      return PAIR;
    }
    return HIGH;
  }
  }
}

int parseHandStrengthP1(struct LongArray *array) {
  struct LongArray *found = initArray();
  struct LongArray *count = initArray();
  appendArray(found, array->array[0]);
  appendArray(count, 1);
  bool flag;
  for (int i = 1; i < array->length; ++i) {
    flag = false;
    for (int j = 0; j < found->length; ++j) {
      if (found->array[j] == array->array[i]) {
        count->array[j]++;
        flag = true;
        break;
      }
    }
    if (!flag) {
      appendArray(found, array->array[i]);
      appendArray(count, 1);
    }
  }
  sortLongArray(count);

  switch (count->array[0]) {
  case 5: {
    return FIVE;
  }
  case 4: {
    return FOUR;
  }
  case 3: {
    if (count->array[1] == 2) {
      return FULL_HOUSE;
    }
    return THREE;
  }
  case 2: {
    if (count->array[1] == 2) {
      return TWO_PAIR;
    }
    return PAIR;
  }
  default: {
    return HIGH;
  }
  }
}

void parseHandP2(struct HandArray *array, char *line) {
  struct Hand *hand = (struct Hand *)malloc(sizeof(struct Hand));
  int i = 0;
  hand->hand = initArray();
  for (; i < 5; i++) {
    switch (line[i]) {
    case 'A': {
      appendArray(hand->hand, 14);
      break;
    }
    case 'K': {
      appendArray(hand->hand, 13);
      break;
    }
    case 'Q': {
      appendArray(hand->hand, 12);
      break;
    }
    case 'J': {
      appendArray(hand->hand, 1);
      break;
    }
    case 'T': {
      appendArray(hand->hand, 10);
      break;
    }
    case '9': {
      appendArray(hand->hand, 9);
      break;
    }
    case '8': {
      appendArray(hand->hand, 8);
      break;
    }
    case '7': {
      appendArray(hand->hand, 7);
      break;
    }
    case '6': {
      appendArray(hand->hand, 6);
      break;
    }
    case '5': {
      appendArray(hand->hand, 5);
      break;
    }
    case '4': {
      appendArray(hand->hand, 4);
      break;
    }
    case '3': {
      appendArray(hand->hand, 3);
      break;
    }
    case '2': {
      appendArray(hand->hand, 2);
      break;
    }
    }
  }
  hand->strength = parseHandStrengthP2(hand->hand);
  i++;
  hand->bet = parse_digit(line, &i);
  hand->line = line;
  resizeHandArray(array);
  array->hands[array->length++] = *hand;
}

void parseHandP1(struct HandArray *array, char *line) {
  struct Hand *hand = (struct Hand *)malloc(sizeof(struct Hand));
  int i = 0;
  hand->hand = initArray();
  for (; i < 5; i++) {
    switch (line[i]) {
    case 'A': {
      appendArray(hand->hand, 14);
      break;
    }
    case 'K': {
      appendArray(hand->hand, 13);
      break;
    }
    case 'Q': {
      appendArray(hand->hand, 12);
      break;
    }
    case 'J': {
      appendArray(hand->hand, 11);
      break;
    }
    case 'T': {
      appendArray(hand->hand, 10);
      break;
    }
    case '9': {
      appendArray(hand->hand, 9);
      break;
    }
    case '8': {
      appendArray(hand->hand, 8);
      break;
    }
    case '7': {
      appendArray(hand->hand, 7);
      break;
    }
    case '6': {
      appendArray(hand->hand, 6);
      break;
    }
    case '5': {
      appendArray(hand->hand, 5);
      break;
    }
    case '4': {
      appendArray(hand->hand, 4);
      break;
    }
    case '3': {
      appendArray(hand->hand, 3);
      break;
    }
    case '2': {
      appendArray(hand->hand, 2);
      break;
    }
    }
  }
  hand->strength = parseHandStrengthP1(hand->hand);
  i++;
  hand->bet = parse_digit(line, &i);

  resizeHandArray(array);
  array->hands[array->length++] = *hand;
}

void swapHands(struct HandArray *array, int i, int j) {
  struct Hand hand = array->hands[j];
  array->hands[j] = array->hands[i];
  array->hands[i] = hand;
}

void sortHands(struct HandArray *array) {
  for (int i = 0; i < array->length - 1; ++i) {
    for (int j = i + 1; j < array->length; j++) {
      struct Hand handI = array->hands[i];
      struct Hand handJ = array->hands[j];
      if (handI.strength > handJ.strength) {
        swapHands(array, i, j);
      }
      if (handI.strength == handJ.strength) {
        for (int k = 0; k < 5; k++) {
          if (handI.hand->array[k] > handJ.hand->array[k]) {
            swapHands(array, i, j);
            break;
          } else if (handI.hand->array[k] < handJ.hand->array[k]) {
            break;
          }
        }
      }
    }
  }
}

int solve_p1(char *content) {
  struct StrArray *lines = parseLines("\n", content);

  struct HandArray *array =
      (struct HandArray *)malloc(sizeof(struct HandArray));
  array->length = 0;
  array->capacity = 8;
  array->hands = (struct Hand *)malloc(sizeof(struct Hand) * array->capacity);

  for (int i = 0; i < lines->length; i++) {
    struct String line = lines->array[i];
    parseHandP1(array, line.string);
  }
  sortHands(array);

  long answer = 0;
  for (int i = 0; i < array->length; ++i) {
    struct Hand hand = array->hands[i];
    answer += (i + 1) * hand.bet;
  }
  freeStringArray(lines);
  return answer;
}

int solve_p2(char *content) {
  struct StrArray *lines = parseLines("\n", content);

  struct HandArray *array =
      (struct HandArray *)malloc(sizeof(struct HandArray));
  array->length = 0;
  array->capacity = 8;
  array->hands = (struct Hand *)malloc(sizeof(struct Hand) * array->capacity);

  for (int i = 0; i < lines->length; i++) {
    struct String line = lines->array[i];
    parseHandP2(array, line.string);
  }
  sortHands(array);

  long answer = 0;
  for (int i = 0; i < array->length; ++i) {
    struct Hand hand = array->hands[i];
    answer += (i + 1) * hand.bet;
  }
  for (int i = 0; i < array->length; ++i) {
    printf("%s\n", array->hands[i].line);
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
