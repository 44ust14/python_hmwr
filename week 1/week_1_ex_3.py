# -*-coding: utf-8 -*-

txt = 'How are you? Eh, ok. Low or Lower? Ohhh. '
txt_caps = ''
for letter in txt:
    if letter.isupper():
        txt_caps = txt_caps + letter
print(txt_caps)
