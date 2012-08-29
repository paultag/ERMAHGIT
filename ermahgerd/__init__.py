#!/usr/bin/env python
# Shamelessly yanked from:
# http://www.reddit.com/r/funny/comments/x2xn0/my_evening_project_a_text_to_ermahgerd_translator/

import re

exps = {
    r'[AEIOUY]r(?! )': "E",
    r'AA': "A",
    r'EE': "E",
    r'II': "I",
    r'OO': "O",
    r'UU': "U",
    r'YY': "Y",
    r'[AEIOUY]{2,}': "E",
    r'[AEIOUY](?! )': "ER",
    r'[Y]': "ER",
    r'ERH': "ER",
    r'ERR': "ER",
    r'MER': "MAH",
    r'ERWERSERMAH': 'ERSUM',
    r'ERWERSERME': 'ERSUM',
    r'GERSERBERMPS': 'GERSBERMS',
    r'MAHMAH': 'MERM',
    r'MAHME': 'MERM',
    r'ERER': 'ER'
}

def translate(text):
    text = text.upper()
    for exp in exps:
        text = re.sub(exp, exps[exp], text)
    return text

