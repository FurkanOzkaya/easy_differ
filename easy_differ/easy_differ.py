'''
Author: Arif Furkan Ozkaya
Date: 04/08/2020
'''

import json

def text_diff(left_text, right_text, get_line=False, prettier=True):
    '''
    Compare texts and return missing lines with json report.
    :param left_text: Type(str)
    :param right_text: Type(str)
    :param get_line: Type(Boolean) Defult = False
    :return: Json report
    '''

    left_lines = left_text.strip().splitlines()
    right_lines = right_text.strip().splitlines()
    returned_left_lines, returned_right_lines = list_diff(left_lines.copy(), right_lines.copy())

    data = {}
    data["report"] = {}
    data["report"]["Description"] = "You can display difference between two text"

    if get_line:
        data["report"]["left_text"] = []
        data["report"]["right_text"] = []

        for ltext in returned_left_lines:
            left_data = {}
            left_data["text"] = ltext
            left_data["line"] = ", ".join(all_index(ltext, left_lines))
            data["report"]["left_text"].append(left_data)

        for rtext in returned_right_lines:
            right_data = {}
            right_data["text"] = rtext
            right_data["line"] = ", ".join(all_index(rtext, right_lines))
            data["report"]["right_text"].append(right_data)
    else:
        data["report"]["left_text"] = returned_left_lines
        data["report"]["right_text"] = returned_right_lines
    if prettier:
        json_report = json.dumps(data, indent=4, sort_keys=True)
    else:
        json_report = json.dumps(data)

    return json_report


def list_diff(left_lines, right_lines):
    '''
    Compare two array and  return missing parts
    :param left_lines: Type(List)
    :param right_lines: Type(List)
    :return: left_lines, right_lines [Type: List]
    '''
    for index_left, left_line_text in enumerate(left_lines):
        left_lines[index_left] = left_line_text.strip()
        if left_line_text == "":
            left_lines.pop(index_left)
            continue
    for index_right, right_line_text in enumerate(right_lines):
        right_lines[index_right] = right_line_text.strip()
        if right_line_text == "":
            right_lines.pop(index_right)
            continue
    copy_left_lines = left_lines.copy()
    for index_left, left_line_text in enumerate(copy_left_lines):
        if left_line_text in right_lines:
            left_lines.remove(left_line_text)
            right_lines.remove(left_line_text)

    return left_lines, right_lines


def all_index(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(str(idx+1))
        except ValueError:
            break
    return indices

