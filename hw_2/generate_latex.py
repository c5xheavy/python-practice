def generate_latex_table(data):
    num_rows = len(data)
    if num_rows == 0:
        return '\\begin{tabular}{c}\n\\end{tabular}'
    num_cols = len(data[0])
    col_types = ['c'] * num_cols  
    latex_table = '\\begin{tabular}{' + ''.join(col_types) + '}\n'
    latex_table += '\\hline\n'
    for row in data:
        row_str = ' & '.join(str(cell) for cell in row)
        latex_table += row_str + ' \\\\\n'
        latex_table += '\\hline\n'
    latex_table += '\\end{tabular}'
    return latex_table
