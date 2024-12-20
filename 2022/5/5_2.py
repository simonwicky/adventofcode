#!/usr/bin/env python

"""
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
"""


def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Parse initial stack configuration
    stacks = []
    stack_lines = []
    for line in lines:
        if line.strip() == "":
            break
        stack_lines.append(line[:-1])#only line I needed to change
    
    # Determine the number of stacks
    num_stacks = len(stack_lines[-1].split())
    stacks = [[] for _ in range(num_stacks)]
    
    # Fill the stacks
    for line in reversed(stack_lines[:-1]):
        for i in range(num_stacks):
            crate = line[1 + 4 * i]
            if crate != ' ':
                stacks[i].append(crate)
    
    # Parse movement instructions
    instructions = []
    for line in lines[len(stack_lines) + 1:]:
        parts = line.strip().split()
        if parts:
            quantity = int(parts[1])
            from_stack = int(parts[3])
            to_stack = int(parts[5])
            instructions.append((quantity, from_stack, to_stack))
    
    return stacks, instructions

# Read input file
file_path = 'input'
stacks, instructions = parse_input(file_path)

# Execute the movement instructions for CrateMover 9001
for quantity, from_stack, to_stack in instructions:
    # Move multiple crates at once while retaining their order
    crates_to_move = stacks[from_stack - 1][-quantity:]
    stacks[from_stack - 1] = stacks[from_stack - 1][:-quantity]
    stacks[to_stack - 1].extend(crates_to_move)

# Determine the top crate of each stack
top_crates = ''.join(stack[-1] for stack in stacks if stack)

print(top_crates)  # Output the result