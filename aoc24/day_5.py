import os

from collections import defaultdict


def get_input() -> tuple[list[int], list[int]]:
    data_file_path = os.path.join(os.path.dirname(__file__), "../data/day_5.txt")
    with open(data_file_path, "r") as fp:
        _input = [line.replace("\n", "") for line in fp.readlines()]

        rules = [tuple([int(x) for x in line.split("|")]) for line in _input if "|" in line]
        updates = [[int(x) for x in line.split(",")] for line in _input if "," in line]

        return rules, updates


def _process_rules(rules: list[tuple]) -> dict[int, list]:
    ordering_rules = defaultdict(list)
    for rule in rules:
        ordering_rules[rule[0]].append(rule[1])
    return dict(ordering_rules)


def _evaluate_rules(update: list[int], ordering_rules: dict[int, list]) -> tuple[list, list]:
    rule_breaks = []
    valid_rules = []

    for i, page_number in enumerate(update):
        if page_number in ordering_rules:
            for rule in ordering_rules[page_number]:
                if rule in update:
                    if rule in update[i + 1:]:
                        valid_rules.append((page_number, rule))
                    else:
                        rule_breaks.append((page_number, rule))

    return rule_breaks, valid_rules


def _find_middle_value(update: list[int]) -> int:
    middle_index = int(len(update) / 2)
    return update[middle_index]


def _correct_update(update: list[int], rule_breaks: list[tuple], valid_rules: list[tuple]) -> list[int]:
    corrected_update = update.copy()

    for before, after in rule_breaks:
        index_before = corrected_update.index(before)
        index_after = corrected_update.index(after)

        corrected_update[index_before] = after
        corrected_update[index_after] = before

    combined_rules = _process_rules(rule_breaks + valid_rules)
    rule_breaks, valid_rules = _evaluate_rules(corrected_update, combined_rules)
    
    if rule_breaks:
        corrected_update = _correct_update(corrected_update, rule_breaks, valid_rules)
        
    return corrected_update


def implementation(rules: list[tuple], updates: list[int]) -> tuple[int, list]:
    p1 = 0
    p2 = 0
    ordering_rules = _process_rules(rules)

    for update in updates:
        rule_breaks, valid_rules = _evaluate_rules(update, ordering_rules)
        if rule_breaks:
            corrected_update = _correct_update(update, rule_breaks, valid_rules)
            p2 += _find_middle_value(corrected_update)
        else:
            p1 += _find_middle_value(update)

    return p1, p2


if __name__ == "__main__":
    _rules, _updates = get_input()
    p1, p2 = implementation(_rules, _updates)
    print(f"Day 5 Part 1: {p1}")
    print(f"Day 5 Part 2: {p2}")
