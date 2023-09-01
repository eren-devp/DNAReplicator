def main():
    try:
        name = str(input("What is the file name?\n> "))

        if not name.__contains__('.txt'):
            name += '.txt'

        with open(name) as rf:
            dna = rf.read().upper()
            rf.close()
            print('Original:\n' + dna)
            dna = dna.replace('A', '0')
            dna = dna.replace('G', '1')
            dna = dna.replace('T', 'A')
            dna = dna.replace('C', 'G')
            dna = dna.replace('0', 'T')
            dna = dna.replace('1', 'C')
            print('Replicated:\n' + dna)

            with open(name.removesuffix('.txt') + ' - Replicated.txt', 'w') as wf:
                wf.write(dna)
                wf.close()

    except Exception:
        print('Something went wrong please check values.')


if __name__ == '__main__':
    main()
