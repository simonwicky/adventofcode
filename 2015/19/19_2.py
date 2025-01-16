#!/usr/bin/env python
"""
Now that the machine is calibrated, you're ready to begin molecule fabrication.

Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

e => H
e => O
H => HO
H => OH
O => HH
If you'd like to make HOH, you start with e, and then make the following replacements:

e => O to get O
O => HH to get HH
H => OH (on the second H) to get HOH
So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?
"""

#No will to analyze the replacement to find a clever solution, so from reddit :
"""
Actually, on second analysis, technically the second half didn't require any code. Here's why:

All of the rules are of one of the following forms:

α => βγ
α => βRnγAr
α => βRnγYδAr
α => βRnγYδYεAr
As Rn, Ar, and Y are only on the left side of the equation, one merely only needs to compute

#NumSymbols - #Rn - #Ar - 2 * #Y - 1

Subtract of #Rn and #Ar because those are just extras. Subtract two times #Y because we get rid of the Ys and the extra elements following them. Subtract one because we start with "e".
"""

with open('input','r') as f:
    data = f.read().splitlines()

new_line = data.index("")
molecule = data[new_line + 1]

num = len([c for c in molecule if c.isupper()])- molecule.count("Rn") - molecule.count("Ar") - 2 * molecule.count("Y") - 1
print(num)

