#!/usr/bin/env python3
"""Convert credit_scoring_primer.txt to LaTeX faithfully - simple approach"""

import re

def escape_latex_simple(text):
    """Escape LaTeX special chars, minimal processing"""
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('$', r'\$')
    text = text.replace('_', r'\_')
    text = text.replace('#', r'\#')
    text = text.replace('FICO®', r'\fico{}')
    text = text.replace('®', r'\textsuperscript{\textregistered}')
    # Remove markdown bold/italic - just strip the asterisks
    text = re.sub(r'\*\*([^*]*)\*\*', r'\1', text)  # Remove **bold**
    text = re.sub(r'\*([^*]*)\*', r'\1', text)       # Remove *italic*
    return text

def convert_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # LaTeX preamble
    latex = r'''\documentclass[11pt,letterpaper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{parskip}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{titlesec}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    pdftitle={Credit Scoring Primer v2.0},
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Credit Scoring Primer v2.0}
\fancyhead[R]{\small Credit Rebels}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\setlength{\headheight}{14pt}

\newcommand{\fico}{FICO\textsuperscript{\textregistered}}

% Adjust section formatting
\titleformat{\section}{\normalfont\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\large\bfseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}{\normalfont\normalsize\bfseries}{\thesubsubsection}{1em}{}

\begin{document}

\begin{center}
{\LARGE\bfseries Credit Scoring Primer v2.0}\\[1cm]
\textit{In memoriam.}\\[0.5cm]
\textbf{Birdman, Birdman7, MFBirdman7}\\
(1976 -- 2023)\\[1cm]
( Last Update: Friday, May 26, 2023 EDT )
\end{center}

\tableofcontents
\newpage

'''

    in_list = False
    skip_header = True
    prev_blank = False

    for line in lines:
        stripped = line.strip()

        # Skip until ## Intro
        if skip_header:
            if stripped.startswith('## Intro'):
                skip_header = False
            else:
                continue

        # Handle headers
        if stripped.startswith('#### '):
            if in_list:
                latex += '\\end{itemize}\n'
                in_list = False
            title = escape_latex_simple(stripped[5:])
            latex += f'\n\\subsubsection{{{title}}}\n\n'
            prev_blank = False
            continue
        elif stripped.startswith('### '):
            if in_list:
                latex += '\\end{itemize}\n'
                in_list = False
            title = escape_latex_simple(stripped[4:])
            latex += f'\n\\subsection{{{title}}}\n\n'
            prev_blank = False
            continue
        elif stripped.startswith('## '):
            if in_list:
                latex += '\\end{itemize}\n'
                in_list = False
            title = escape_latex_simple(stripped[3:])
            latex += f'\n\\section{{{title}}}\n\n'
            prev_blank = False
            continue

        # Handle bullet points
        if stripped.startswith('• '):
            if not in_list:
                latex += '\\begin{itemize}[leftmargin=*]\n'
                in_list = True
            content = escape_latex_simple(stripped[2:])
            latex += f'    \\item {content}\n'
            prev_blank = False
            continue

        # Handle blank lines
        if stripped == '':
            if in_list:
                latex += '\\end{itemize}\n'
                in_list = False
            if not prev_blank:
                latex += '\n'
            prev_blank = True
            continue

        # Regular text
        if in_list:
            # Continuation of list item
            content = escape_latex_simple(stripped)
            latex += f'          {content}\n'
        else:
            content = escape_latex_simple(stripped)
            latex += f'{content}\n'
        prev_blank = False

    if in_list:
        latex += '\\end{itemize}\n'

    latex += '\n\\end{document}\n'

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex)

    print(f"Converted {input_path} to {output_path}")
    print(f"Lines processed: {len(lines)}")

if __name__ == '__main__':
    convert_file('credit_scoring_primer.txt', 'Credit_Scoring_Primer_v2_Original.tex')
