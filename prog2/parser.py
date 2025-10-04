"""
jack baretz
csci 365
10/3/2025
scanning text file for language
"""

import re

ID_REX = r"^[A-Za-z][A-Za-z0-9]*"
NUM_REX = r"-?\d+(\.\d+)?"
LPAREN_REX = r"\("
RPAREN_REX = r"\)"
ADDOP_REX = r"[+-]"
MULTOP_REX = r"(\*|/|//|%)"
RELOP_REX = r"(<=|>=|==|!=|<|>)"
ASSIGN_REX = r"="
READ_REX = r"read"
WRITE_REX = r"write"
IF_REX = r"if"
ELSE_REX = r"else"
KEYWORD_REX = rf"({READ_REX}|{WRITE_REX}|{IF_REX}|{ELSE_REX})"

rex_table = {
    "id": (ID_REX, "<id>"),
    "num": (NUM_REX, "<num>"),
    "lparen": (LPAREN_REX, "<lparen>"),
    "rparen": (RPAREN_REX, "<rparen>"),
    "addop" : (ADDOP_REX, "<add_op>"),
    "multop": (MULTOP_REX, "<mult_op"),
    "relop": (RELOP_REX, "<rel_op>"),
    "assign": (ASSIGN_REX, "<assign_op>"),
    "read": (READ_REX, "<read>"),
    "write": (WRITE_REX, "<write>"),
    "iff" : (IF_REX, "<if>"),
    "elsee": (ELSE_REX, "<else>")
}


def matching(rex, inp) -> bool:
    if rex == ID_REX:
        return bool(re.fullmatch(rex, inp)) and not (re.fullmatch(KEYWORD_REX, inp))
    else:
        return bool(re.fullmatch(rex, inp))

def token_parse(inp: str) -> str:
    for rex in rex_table.keys():
        if matching(rex_table[rex][0], inp):
            return rex_table[rex][1]
    return "<error>"


def get_token_positions(line):
    """
    Returns a list of column positions (0-indexed) where each token starts.
    """
    tokens = []
    positions = []

    for match in re.finditer(r'\S+', line):
        tokens.append(match.group())
        positions.append(match.start())

    return positions


def parse_file(lineArr):
    token_lists = []

    for i in range(len(lineArr)):
        stripped = lineArr[i].strip()

        #empty line
        if stripped == "":
            token_lists.append([])
            continue
        #comment line
        if lineArr[i].strip()[0] == "#":
            token_lists.append([])
            continue

        column_list = get_token_positions(lineArr[i])
    
        split = lineArr[i].strip().split(" ")

        if len(column_list) != len(split):
            print("Column list and split list ERROR")

        if " " in split:
            split = split.remove(" ")

        token_list = []

        # split and column list will have the same length
        for j in range(len(split)):
            token_l = token_parse(split[j])
            if token_l == "<error>":
                return (token_l, split[j], i+1, column_list[j])

            else:
                token_list.append((token_l, split[j], i+1, column_list[j]))
        token_lists.append(token_list)
    return token_lists


def print_output(lists):
    if type(lists) == list:
        for i in range(len(lists)):
            if lists[i] == []:
                continue

            for j in range(len(lists[i])):
                print(f"{lists[i][j][0]}, {lists[i][j][1]}, {lists[i][j][2]}, {lists[i][j][3]}")
    else:
        print(f"{lists[0]}, {lists[1]}, {lists[2]}, {lists[3]}")


def main():
    source = open("sample.txt", "r")
    arr = source.read().split("\n")

    res = parse_file(arr)
    print_output(res)

main()