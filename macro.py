# Complete Two-Pass Macro Processor Implementation

def pass_one(source_code):
    MNT = {}
    MDT = []
    intermediate_code = []
    mdt_index = 0
    in_macro = False

    for line in source_code:
        tokens = line.strip().split()

        # Check for the start of macro definition
        if tokens[0].lower() == 'macro':
            in_macro = True
            macro_name = tokens[1]
            params = tokens[2:]  # Macro parameters
            MNT[macro_name] = {"mdt_index": mdt_index, "param_count": len(params)}
            continue

        # Check for the end of macro definition
        if tokens[0].lower() == 'mend':
            MDT.append({"line": 'MEND'})
            in_macro = False
            mdt_index += 1
            continue

        if in_macro:
            # Add the macro body to MDT
            MDT.append({"line": line})
            mdt_index += 1
        else:
            # Add non-macro lines to intermediate code
            intermediate_code.append(line)

    return MNT, MDT, intermediate_code


def pass_two(MNT, MDT, intermediate_code):
    expanded_code = []

    for line in intermediate_code:
        tokens = line.strip().split()

        # Check if the line contains a macro call
        if tokens[0] in MNT:
            macro_name = tokens[0]
            macro_info = MNT[macro_name]
            param_count = macro_info["param_count"]
            actual_args = tokens[1:]  # Arguments passed to the macro

            # Create an ALA (Argument List Array) to map formal parameters to actual arguments
            ALA = actual_args

            # Fetch macro definition from MDT and expand
            mdt_index = macro_info["mdt_index"]
            while MDT[mdt_index]["line"] != 'MEND':
                macro_line = MDT[mdt_index]["line"]
                for i in range(param_count):
                    macro_line = macro_line.replace(f"&ARG{i + 1}", ALA[i])
                expanded_code.append(macro_line)
                mdt_index += 1
        else:
            # No macro call, copy the line as it is
            expanded_code.append(line)

    return expanded_code


# Example usage
source_code = [
    "MACRO MAC1 &ARG1 &ARG2",
    "LDA &ARG1",
    "ADD &ARG2",
    "MEND",
    "START 100",
    "MAC1 A, B",
    "END"
]

# Pass-I: Process the source code, generate MNT, MDT, and Intermediate Code
MNT, MDT, intermediate_code = pass_one(source_code)

# Output of Pass-I
print("Pass-I Output:")
print("MNT (Macro Name Table):", MNT)
print("MDT (Macro Definition Table):", MDT)
print("Intermediate Code File:", intermediate_code)

# Pass-II: Expand the macros using the information from Pass-I
expanded_code = pass_two(MNT, MDT, intermediate_code)

# Output of Pass-II
print("\nPass-II Output (Expanded Code):")
for line in expanded_code:
    print(line)
