#include "../helpers.h"

int solve_p1(char *content) {
    struct Lines *lines = initLines();
    parseLines(lines, "\n", content);

    struct LongArray *seeds = parseIntsFromString(lines->lines[0]);
    int i = 0;

    while (i < lines->length) {
        struct LongArray *newArray = copyArray(seeds);

        while (i < lines->length && isdigit(lines->lines[i][0])) {
            struct LongArray *ranges = parseIntsFromString(lines->lines[i]);

            for (int j = 0; j < seeds->length; ++j) {
                if (ranges->array[1] > seeds->array[j] ||
                    seeds->array[j] > ranges->array[1] + ranges->array[2] ||
                    newArray->array[j] != seeds->array[j]) {
                    continue;
                }

                newArray->array[j] =
                    ranges->array[0] + seeds->array[j] - ranges->array[1];
            }
            freeArray(ranges);
            i++;
        }

        freeArray(seeds);
        seeds = newArray;
        i++;
    }
    int answer = INT_MAX;
    for (int i = 0; i < seeds->length; ++i) {
        answer = answer > seeds->array[i] ? seeds->array[i] : answer;
    }

    freeArray(seeds);
    freeLines(lines);

    return answer;
}

struct Range *getOverlap(struct Range *range, long s_start, long s_end,
                         long d_start) {
    struct Range *newRange = (struct Range *)malloc(sizeof(struct Range));
    newRange->start =
        d_start + (range->start > s_start ? range->start : s_start) - s_start;

    newRange->end =
        d_start + (range->end < s_end ? range->end : s_end) - s_start;

    return newRange;
}

long parse_p2(char *content) {
    struct Lines *lines = initLines();
    parseLines(lines, "\n", content);

    struct LongArray *seeds = parseIntsFromString(lines->lines[0]);
    struct Stack *stack = initStack();
    // for (int i = 0; i < seeds->length; i += 2) {
    //     struct Range *range = (struct Range *)malloc(sizeof(struct Range));
    //     range->start = seeds->array[i];
    //     range->end = seeds->array[i] + seeds->array[i + 1];
    //     push(stack, range);
    // }
    struct Range *range = (struct Range *)malloc(sizeof(struct Range));
    range->start = 82;
    range->end = 87;
    push(stack, range);
    freeArray(seeds);
    int i = 0;
    while (i < lines->length) {
        struct Stack *newStack = copyStack(stack);
        while (i < lines->length && isdigit(lines->lines[i][0])) {
            struct LongArray *ranges = parseIntsFromString(lines->lines[i]);
            long s_start = ranges->array[1], s_dist = ranges->array[2],
                 s_end = ranges->array[1] + ranges->array[2];
            long d_start = ranges->array[0];

            while (true) {
                if (stack->length == 0) {
                    break;
                }
                struct Range *range = pop(stack);
                // Outside the range
                if (range->start > s_end || range->end < s_start) {
                    continue;
                }
                struct Range *newRange =
                    getOverlap(range, s_start, s_end, d_start);
                push(newStack, newRange);

                // Fully within the s_range
                if (range->start >= s_start && range->end <= s_end) {
                    continue;
                }
                // Was above
                struct Range *newRange2 =
                    (struct Range *)malloc(sizeof(struct Range));
                if (range->end > s_end) {
                    newRange2->start = s_end + 1;
                    newRange2->end = range->end;
                    push(newStack, newRange2);
                } else {
                    newRange2->start = range->start;
                    newRange2->end = s_start - 1;
                    push(newStack, newRange2);
                }
            }
            freeArray(ranges);
            i++;
        }
        freeStack(stack);
        stack = newStack;
        i++;
    }
    for (int i = 0; i < stack->length; ++i) {
        printf("%lu -", stack->stack[i].start);
    }
    printf("\n");
    freeLines(lines);
    return 0;
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
    int p2 = parse_p2(content_cpy);

    printf("p1: %d\np2: %d\n", p1, p2);

    free(content_cpy);
    free(content);
}
