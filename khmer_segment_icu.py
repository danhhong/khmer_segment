# -*- coding: utf-8 -*-
"""
Wrapper for PyICU word segmentation
https://github.com/ovalhub/pyicu/blob/master/samples/break.py
"""
import re
from typing import List
from icu import BreakIterator, Locale 

def gen_khm_words(text: str) -> str:
    bi = BreakIterator.createWordInstance(Locale("km"))
    bi.setText(text)
    start = bi.first()
    for end in bi:
        yield text[start:end]
        start = end

def khm_segment(text: str) -> List[str]:
    if not text or not isinstance(text, str):
        return []
    text = re.sub("([^\u1780-\u17FF\n ]+)", " \\1 ", text)
    return list(gen_khm_words(text))

if __name__ == "__main__":
    khmertext = "ចេញពីតំបន់ដែនជម្រកសត្វព្រៃណាំលៀរ"
    word_list = khm_segment(khmertext)
    print(word_list)

#out: ['ចេញពី', 'តំបន់', 'ដែន', 'ជម្រក', 'សត្វ', 'ព្រៃ', 'ណាំលៀរ']