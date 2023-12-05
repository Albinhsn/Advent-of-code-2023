#include "../helpers.h"

int solve_p1(char *content) {
    struct Lines *lines = initLines();
    parseLines(lines, "\n", content);

    struct IntArray *seeds = parseIntsFromString(lines->lines[0]);
    int i = 0;

    while (i < lines->length) {
        struct IntArray *newArray = copyArray(seeds);

        if (i < lines->length && isdigit(lines->lines[i][0])) {
            for (int j = 0; j < seeds->length; ++j) {
                printf("%d - ", seeds->array[j]);
            }
            printf("\n");
        }

        while (i < lines->length && isdigit(lines->lines[i][0])) {
            struct IntArray *ranges = parseIntsFromString(lines->lines[i]);

            for (int j = 0; j < seeds->length; ++j) {
                if (ranges->array[1] > seeds->array[j] ||
                    seeds->array[j] > ranges->array[1] + ranges->array[2]) {
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
        printf("%d - ", seeds->array[i]);
        answer = answer > seeds->array[i] ? seeds->array[i] : answer;
    }
    printf("\n");

    freeArray(seeds);
    freeLines(lines);

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
    int p1 = solve_p1(content_cpy);

    memcpy(content_cpy, content, strlen(content));
    int p2 = parse_p2(content_cpy);

    printf("p1: %d\np2: %d\n", p1, p2);

    free(content_cpy);
    free(content);
}
