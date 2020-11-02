# Numerical-base-converter

This package is to convert a value from a numerical base to another.
It can work with python >= 3.0 and was created under python 3.8.5

The 'base' function use the 'convert' function to convert the numbers given (as a string).
If a list/tuple is provided, the function will do all the string in the list/tuple.
If all the numbers in the are not to be converted with the same base, please provided these values in a list following this:
\tbase([n_1, n_2, ..., [n_x, new_w_1, new_t_1], n_x+1, ..., [n_z, new_w_2, new_t_2]], base_written_in, base_to_write_to)
\nHere, 'base_written_in' and 'base_to_write_to' are the main base in wich we have to write in.
and, 'n_1', 'n_2', 'n_x', 'n_x+1' and 'n_z' are numbers we want to convert.
However, the difference lay in the base in wich we want to write them.
'n_x' and all the numbers that follow will be considered written in base 'new_w_1'.
They also will be written in base 'new_t_1' until say otherwise (like with [n_z, new_w_2, new_t_2])
\nSo a lengthy explanation to say that in the example: /!\ /!\ read carefully /!\ /!\
\t\tbase(['0', '1', ['2', 10, 2], '3', ['4', 10, 3], '5', '6'], 2, 10)\n
\t0 and 1 are considered written in base 2 and will be output in base 10. So the output will be ['0', '1']
\t2 is written in base 10 and will be output in base 2, output: '10'
\t3 will be considered like 2 (because we have not asked to change the values of the base), output: '11'
\t4, 5 and 6 are written in base 10 and will be written in base 3, output: ['11', '12', '20']
