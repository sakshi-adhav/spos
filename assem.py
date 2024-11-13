# Define the opcode table and directives
OPCODE_TABLE = {
    "LOAD": "01",
    "STORE": "02",
    "ADD": "03",
    "SUB": "04",
    "JUMP": "05",
    "JUMPZ": "06",
}
DIRECTIVES = {"START": "START", "END": "END"}

# Symbol table and intermediate code list
symbol_table = {}
intermediate_code = []


# Pass-I: Generate intermediate code and symbol table
def pass_one(assembly_code):
    location_counter = 0
    for line in assembly_code:
        parts = line.strip().split()
        if not parts:
            continue

        # Handle the START directive
        if parts[0] == "START":
            location_counter = int(parts[1])
            continue
        # Handle the END directive and stop processing
        if parts[0] == "END":
            break

        label = None
        # If the first part is not an opcode, it's a label
        if parts[0] not in OPCODE_TABLE:
            label, parts = parts[0], parts[1:]
            symbol_table[label] = location_counter  # Save label and its address

        # Now, process the instruction and its operand (if any)
        instruction = parts[0]
        operand = parts[1] if len(parts) > 1 else None
        intermediate_code.append((location_counter, instruction, operand))
        location_counter += 1

    return intermediate_code, symbol_table


# Pass-II: Convert intermediate code to machine code
def pass_two(intermediate_code, symbol_table):
    machine_code = []
    for address, instruction, operand in intermediate_code:
        # Get the opcode for the instruction
        opcode = OPCODE_TABLE.get(instruction, "??")

        # If the instruction has an operand, resolve its address from the symbol table
        if operand:
            operand_address = symbol_table.get(operand, "0000")
            machine_code.append(f"{address:04} {opcode} {operand_address:04}")
        else:
            machine_code.append(f"{address:04} {opcode} 0000")  # No operand
    return machine_code


# Sample Assembly Code
assembly_code = [
    "START 100",
    "LOOP LOAD A",
    "ADD B",
    "STORE C",
    "SUB D",
    "JUMPZ END",
    "JUMP LOOP",
    "END STORE E",
]

# Run Pass-I
intermediate_code, symbol_table = pass_one(assembly_code)
print("Intermediate Code (Pass-I Output):", *intermediate_code, sep="\n")

print("\nSymbol Table (Pass-I Output):", symbol_table)

# Run Pass-II
machine_code = pass_two(intermediate_code, symbol_table)
print("\nMachine Code (Pass-II Output):", *machine_code, sep="\n")
