# -*- coding: utf-8 -*-
from http import HTTPStatus
import dashscope

response = dashscope.Generation.call(
    model='qwen-max',
    prompt="def generate_css_from_constraints(layout):\n    exemplar = f\"Exemplar :\" + r\"\n\"\n    constraints = []\n    css_out = \"\"\n    for page_number, page_constraints in enumerate(layout, start=1):\n        elements = page_constraints.split()\n        type_s = \"\"\n        for element in elements:\n            e_layout = element.split(';')\n            element_type, left, top, width, height = e_layout[0], e_layout[1], e_layout[2], e_layout[3], e_layout[4]\n            css_class = f\".page_{page_number}_{element_type}\"\n            css_properties = f\"\"\"{{ left: {left}px; top: {top}px; width: {width}px; height: {height}px; }}\"\"\"\n            type_s += (f\"{element_type}\") + \" \"\n            css_out += css_class + \" \" + css_properties + r\"\n\"\n        constraints.append(type_s)\n    exemplar += \"Constraints:\" + str(constraints) + r\"\n\"\n    exemplar += \"CSS_output:\" + r\"\n\"\n    exemplar += css_out\n    return exemplar\n\n\ninput = ['text0 text1 text2 text3 text4 \\n', 'title0 text1 text2 text3 text4 text5 title6 text7 \\n', 'text0 figure1 text2 text3 title4 text5 \\n', 'title0 text1 text2 text3 text4 title5 text6 \\n', 'figure0 text1 text2 text3 text4 text5 text6 \\n', 'text0 table1 figure2 text3 title4 text5 text6 text7 \\n', 'text0 figure1 text2 text3 text4 \\n', 'text0 text1 title2 text3 text4 text5 \\n']\noutput = ['text0;26;23;68;10 text1;26;33;68;17 text2;26;51;68;33 text3;26;85;68;29 text4;26;115;68;19 ', '\\n', 'title0;26;117;68;17 text1;26;52;68;7 text2;26;40;68;7 text3;26;75;68;17 text4;26;28;68;5 text5;26;102;68;5 title6;26;111;19;3 text7;26;23;17;3 ', '\\n', 'text0;26;96;68;21 figure1;26;127;68;7 text2;39;23;44;2 text3;36;89;44;2 title4;26;121;16;3 text5;26;26;68;61 ', '\\n', 'title0;31;61;57;48 text1;26;122;68;12 text2;36;111;44;2 text3;28;38;64;18 text4;38;34;44;2 title5;26;117;18;3 text6;33;23;54;6 ', '\\n', 'figure0;26;96;68;14 text1;26;40;68;4 text2;26;68;68;25 text3;26;48;68;7 text4;26;129;68;5 text5;26;116;68;5 text6;26;18;67;19 ', '\\n', 'text0;26;79;68;27 table1;26;106;68;19 figure2;26;129;68;5 text3;31;68;57;2 title4;33;23;44;2 text5;29;75;22;2 text6;26;26;67;39 text7;28;26;66;39 ', '\\n', 'text0;26;76;68;24 figure1;26;105;68;29 text2;26;68;67;2 text3;36;23;44;2 text4;26;26;67;40 ', '\\n', 'text0;26;79;68;24 text1;26;106;68;17 title2;26;127;68;7 text3;26;57;68;9 text4;26;35;68;15 text5;26;70;33;3 ', '\\n']\n\nprint(generate_css_from_constraints(output))\n\nTask Description: learn from the code above and follow the format above to complete the coordinates of input below\nLayout Domain: document layout\nCanvas Size: canvas width is 120px, canvas height is 160px\nRules: the title bounding box is smaller and shorter; different bounding boxes do not overlap; boundaries of all elements should not exceed the page size (120px *160px);\nRules: keep the same left, right, top and bottom margins on each page; elements well aligned; keep the bounding boxes spaced; keep the same number of columns on each page.\n\n\ninput = [\"['text0 title1 text2 text3 text4 title5 title6 text7 \\n', 'text0 figure1 text2 title3 text4 title5 text6 text7 \\n', 'text0 figure1 text2 text3 title4 text5 text6 \\n', 'title0 title1 text2 text3 text4 text5 title6 text7 title8 text9 text10 \\n', 'text0 text1 text2 text3 text4 text5 text6 \\n', 'text0 text1 text2 text3 title4 text5 text6 \\n', 'table0 table1 text2 text3 text4 title5 text6 figure7 text8 figure9 text10 \\n', 'text0 text1 text2 text3 text4 \\n']\"]\noutput = ?",
    seed=1234,
    top_p=0.8,
    result_format='message',
    enable_search=False,
    max_tokens=2000,
    temperature=0.85,
    repetition_penalty=1.0,
    api_key="sk-abb7c2c5b36c4f239a048c597cb0ea1a"
)
if response.status_code == HTTPStatus.OK:
    print(response)
else:
    print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
        response.request_id, response.status_code,
        response.code, response.message
    ))