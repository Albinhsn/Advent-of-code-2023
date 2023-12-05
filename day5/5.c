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

long parse_p2(char *content) {
    struct Lines *lines = initLines();
    parseLines(lines, "\n", content);

    struct LongArray *seeds = parseIntsFromString(lines->lines[0]);

    // Create LongArray ** with ranges
    // Create stack from LongArray** and iterate until empty
    // repeat

    freeLines(lines);
    freeArray(seeds);
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
