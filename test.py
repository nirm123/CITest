import sys
import basic_math as bm

if (sys.argv[1].lower() == 'math'):
    if bm.add(1, 2) != 1 + 2:
        raise ValueError('Addition broken')
    if bm.subtract(5, 4) != 5 - 4:
        raise ValueError('Subtraction broken')
    if bm.multiply(1, 2) != 1 * 2:
        raise ValueError('Multiplication broken')
    if bm.divide(1, 2) != 1 / 2:
        raise ValueError('Division broken')
    print("Math functions correct")

else:
    raise ValueError('Test not recognized')
