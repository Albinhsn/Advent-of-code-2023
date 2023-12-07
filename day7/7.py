from collections import Counter
from enum import Enum, auto
from functools import cmp_to_key


class HandStr(Enum):
    HIGH = auto()
    PAIR = auto()
    TWO_PAIR = auto()
    THREE = auto()
    FULL_HOUSE = auto()
    FOUR = auto()
    FIVE = auto()


def parse_p1(line):
    hcm = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    hand, bet = line.split()
    counter = Counter([i for i in hand])

    most_common = counter.values()

    if 5 in most_common:
        hand_str = HandStr.FIVE
    elif 4 in most_common:
        hand_str = HandStr.FOUR
    elif 3 in most_common:
        if 2 in most_common:
            hand_str = HandStr.FULL_HOUSE
        else:
            hand_str = HandStr.THREE
    elif 2 in most_common:
        if len([i for i in counter if counter[i] == 2]) == 2:
            hand_str = HandStr.TWO_PAIR
        else:
            hand_str = HandStr.PAIR
    else:
        hand_str = HandStr.HIGH
    h = (hand_str, [hcm[i] for i in hand], int(bet))
    return h


def parse_p2(line):
    hcm = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1,
    }
    hand, bet = line.split()
    counter = Counter([i for i in hand if i != "J"])

    jokers = len([i for i in hand if i == "J"])
    most_common = counter.values()

    if 5 in most_common:
        hand_str = HandStr.FIVE
    elif 4 in most_common:
        if jokers == 1:
            hand_str = HandStr.FIVE
        else:
            hand_str = HandStr.FOUR
    elif 3 in most_common:
        if 2 in most_common:
            hand_str = HandStr.FULL_HOUSE
        else:
            if jokers == 2:
                hand_str = HandStr.FIVE
            elif jokers == 1:
                hand_str = HandStr.FOUR
            else:
                hand_str = HandStr.THREE
    elif 2 in most_common:
        if len([i for i in counter if counter[i] == 2]) == 2:
            if jokers == 1:
                hand_str = HandStr.FULL_HOUSE
            else:
                hand_str = HandStr.TWO_PAIR
        else:
            if jokers == 3:
                hand_str = HandStr.FIVE
            elif jokers == 2:
                hand_str = HandStr.FOUR
            elif jokers == 1:
                hand_str = HandStr.THREE
            else:
                hand_str = HandStr.PAIR
    else:
        if jokers in [4, 5]:
            hand_str = HandStr.FIVE
        elif jokers == 3:
            hand_str = HandStr.FOUR
        elif jokers == 2:
            hand_str = HandStr.THREE
        elif jokers == 1:
            hand_str = HandStr.PAIR
        else:
            hand_str = HandStr.HIGH
    h = (hand_str, [hcm[i] for i in hand], int(bet))
    return h


def compare(item1, item2):
    def resolve_high_card(cards1: list, cards2: list):
        if cards1[0] > cards2[0]:
            return 1
        elif cards2[0] > cards1[0]:
            return -1
        return resolve_high_card(cards1[1:], cards2[1:])

    if item1[0].value > item2[0].value:
        return 1
    elif item1[0].value < item2[0].value:
        return -1

    return resolve_high_card(item1[1], item2[1])


lines = sorted(
    [parse_p1(i) for i in open("input").read().split("\n")[:-1]],
    key=cmp_to_key(compare),
)
print("p1:", sum([(idx + 1) * i[2] for idx, i in enumerate(lines)]))

lines = sorted(
    [parse_p2(i) for i in open("input").read().split("\n")[:-1]],
    key=cmp_to_key(compare),
)
print("p2:", sum([(idx + 1) * i[2] for idx, i in enumerate(lines)]))
