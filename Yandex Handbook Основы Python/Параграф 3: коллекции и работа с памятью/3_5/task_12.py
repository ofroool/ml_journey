filename = input()
even_file = input()
odd_file = input()
eq_file = input()
with open(filename, 'r', encoding='UTF-8') as f_in, \
     open(even_file, 'w', encoding='UTF-8') as f_even, \
     open(odd_file, 'w', encoding='UTF-8') as f_odd, \
     open(eq_file, 'w', encoding='UTF-8') as f_eq:

    for line in f_in:
        even_nums = []
        odd_nums = []
        eq_nums = []

        for num_str in line.split():
            len_even = sum(1 for ch in num_str if ch.isdigit() and int(ch) % 2 == 0)
            len_odd = sum(1 for ch in num_str if ch.isdigit() and int(ch) % 2 != 0)
            if len_even > len_odd:
                even_nums.append(num_str)
            elif len_odd > len_even:
                odd_nums.append(num_str)
            else:
                eq_nums.append(num_str)
        print(" ".join(even_nums), file=f_even)
        print(" ".join(odd_nums), file=f_odd)
        print(" ".join(eq_nums), file=f_eq)