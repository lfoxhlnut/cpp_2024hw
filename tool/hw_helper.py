# 与老师原始发的文件相比, 如下修改:
# 图片文件需要与源文件置于同一文件夹
# 源文件支持中文了

import os
from privacy import hw_path, hw_name, en_name, student_id

my_output_path = r"""../output/"""


def custom_key(item):
    parts = item.split('.')
    if len(parts) > 2:
        return int(parts[1])
    else:
        return 0
    
files = sorted(os.listdir(hw_path), key=custom_key)
cpp_files = []
codes = []

for file in files:
    if '.cpp' in file:
        cpp_files.append(file)
        with open(hw_path + file) as cpp_file:
            codes.append(cpp_file.read())


write_head_1 = r"""
\documentclass{article}
\usepackage{CJK}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[a4paper, margin=1in]{geometry}
\usepackage{graphicx}
"""
write_head_2 = "\\graphicspath{{ {{{0}}} }}"

write_head_3 = r"""

\usepackage{minted}
\large
\title{C++ Assignment}
\begin{document}
\begin{titlepage}
    \begin{center}
    \line(1,0){300}\\
    [0.65cm]
    \huge{\bfseries Assignment I}\\
    \line(1,0){300}\\
    \textsc{\Large C++ Course}\\
    \textsc{\LARGE \today}\\
    [5.5cm]     
    \end{center}
    \begin{flushright}
    \textsc{\Large Econ School\\"""

write_head_4 = '{0}\\\\{1}'

write_head_5 =r"""}\\[0.5cm]
            \textsc{\Large Operating System\\Ubuntu 22.04}\\[0.5cm]
    \end{flushright}
\end{titlepage}
"""

write_section = r"""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section*{{{content}}}"""

write_code1 = r"""
\begin{CJK*}{UTF8}{gkai}
\begin{minted}[frame=lines, linenos, fontsize=\large]
{c++}
"""

write_code2 = r"""
\end{minted}
\end{CJK*}

\subsection*{Output}

\begin{figure}[h]
    \centering"""

write_pic = """
    \includegraphics[width=\\textwidth]{{{}}}
\\end{{{}}}
"""

with open(my_output_path + hw_name + '.tex', 'w') as hw_tex:
    hw_tex.write(write_head_1)
    # tex 文件中, 路径的斜线需要转义
    hw_tex.write(write_head_2.format(hw_path.replace('\\', '\\\\')))
    hw_tex.write(write_head_3)
    hw_tex.write(write_head_4.format(en_name, student_id))
    hw_tex.write(write_head_5)

    for code, file in zip(codes, cpp_files):
        hw_tex.write(write_section.format(content=file))
        hw_tex.write(write_code1)
        hw_tex.write(code)
        hw_tex.write(write_code2)
        hw_tex.write(write_pic.format(file[:file.find('.cpp')] + '.png', 'figure'))
    
    hw_tex.write(r'\end{document}')
