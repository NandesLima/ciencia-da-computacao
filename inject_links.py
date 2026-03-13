import os
import glob

# Injection Logic for Free Courses into the parsed Markdown tables
file_path_module1 = "/root/.openclaw/workspace/ciencia-da-computacao/docs/04-introducao-a-computacao.md"
file_path_module2 = "/root/.openclaw/workspace/ciencia-da-computacao/docs/05-aprofundamento-de-conceitos-introdutorios.md"
file_path_module3 = "/root/.openclaw/workspace/ciencia-da-computacao/docs/06-desenvolvimento-tecnico.md"
file_path_module5 = "/root/.openclaw/workspace/ciencia-da-computacao/docs/08-aprofundamento-tecnico.md"

def inject_link(filepath, match_str, link_html):
    if not os.path.exists(filepath): return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the matching string with itself + the new link
    # We look for the exact markdown link text
    content = content.replace(match_str, match_str + " <br><br>⚡ " + link_html)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# 1. Python Basics
inject_link(
    file_path_module1, 
    "[Algoritmos e Programação em Python](https://www.youtube.com/playlist?list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0)", 
    "**Rápido/Livre:** [Python (Siraj Raval)](https://github.com/NandesLima/Learn_Computer_Science_in_5_Months#week-1-2)"
)

# 2. Discrete Math
inject_link(
    file_path_module2, 
    "[Lógica e Matemática Discreta](https://www.youtube.com/playlist?list=PLxI8Can9yAHf6oB0nf8FwLhqSOcBLqOxH)", 
    "**Rápido/Livre:** [Matemática Acelerada](https://github.com/NandesLima/learn_math_fast)"
)

# 3. Data Structures
inject_link(
    file_path_module3, 
    "[Estruturas de Dados](https://www.youtube.com/playlist?list=PLxI8Can9yAHf8k8LrUePyj0y3lNptrSerial)", 
    "**Rápido/Livre:** [Data Structures (Siraj)](https://github.com/NandesLima/Learn_Computer_Science_in_5_Months#week-3-4)"
)

# 4. Databases
inject_link(
    file_path_module5, 
    "[Bancos de Dados](https://www.youtube.com/playlist?list=PLxI8Can9yAHdzyR4sDqKzXoYpQ111n-m)", 
    "**Rápido/Livre:** [Databases (Siraj)](https://github.com/NandesLima/Learn_Computer_Science_in_5_Months#week-7)"
)

# 5. Networking
inject_link(
    file_path_module5, 
    "[Redes de Computadores](https://www.youtube.com/playlist?list=PLxI8Can9yAHe_4jMepWw2_q18G7iF-Fp3)", 
    "**Rápido/Livre:** [Networking (Siraj)](https://github.com/NandesLima/Learn_Computer_Science_in_5_Months#week-8)"
)
