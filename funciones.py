def reescribir_archivo(input_text):
    lines = input_text.split("\n")
    variables = {}
    
    for line in lines:
        if line.startswith("let"):
            var_name, value = line[4:].split(" = ")
            variables[var_name] = value.strip("'")

    for var_name, value in variables.items():
        for dependent_var in variables:
            variables[dependent_var] = variables[dependent_var].replace(var_name, f"({value})")

    output_lines = []
    for var_name, value in variables.items():
        output_lines.append(f"let {var_name} = '{value}'")

    return "\n".join(output_lines)


def get_values_list(rewritten_text):
    lines = rewritten_text.split("\n")
    values_list = []

    for line in lines:
        if line.startswith("let"):
            _, value = line.split(" = ")
            value = value.strip("'")
            values_list.append(value)

    return values_list
