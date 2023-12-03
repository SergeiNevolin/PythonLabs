import sys

class CompressedDNA:
    def __init__(self, dna_sequence):
        self.validate_input(dna_sequence)
        self.original_dna_str = dna_sequence
        self.bits = self._compress()

    def validate_input(self, dna_sequence):
        valid_nucleotides = {'a', 'c', 'g', 't'}
        if not set(dna_sequence).issubset(valid_nucleotides):
            raise ValueError("Invalid nucleotides in the DNA sequence.")

    def _compress(self):
        nucleotide_mapping = {'a': 0b00, 'c': 0b01, 'g': 0b10, 't': 0b11}
        compressed_bits = 0b00
        for nucleotide in self.original_dna_str:
            compressed_bits <<= 2
            compressed_bits |= nucleotide_mapping[nucleotide]
        return compressed_bits

    def _decompress(self, compressed_bits):
        nucleotides = ''
        nucleotide_mapping = {0b00: 'a', 0b01: 'c', 0b10: 'g', 0b11: 't'}
        while compressed_bits:
            nucleotide_code = compressed_bits & 0b11
            nucleotides += nucleotide_mapping[nucleotide_code]
            compressed_bits >>= 2
        return nucleotides[::-1]

    def __str__(self):
        return self._decompress(self.bits)

if __name__ == "__main__":
    print("1000 нуклеотидов")
    dna_str = open('1000.txt').read().replace('\n', '')
    compressed_dna_str = CompressedDNA(dna_str)
    print(f'Исходная строка: {sys.getsizeof(dna_str)} байтов')
    print(f'Сжатая строка: {sys.getsizeof(compressed_dna_str.bits)} байтов')

    print("10000 нуклеотидов")
    dna_str = open('10000.txt').read().replace('\n', '')
    compressed_dna_str = CompressedDNA(dna_str)
    print(f'Исходная строка: {sys.getsizeof(dna_str)} байтов')
    print(f'Сжатая строка: {sys.getsizeof(compressed_dna_str.bits)} байтов')

    print("100000 нуклеотидов")
    dna_str = open('100000.txt').read().replace('\n', '')
    compressed_dna_str = CompressedDNA(dna_str)
    print(f'Исходная строка: {sys.getsizeof(dna_str)} байтов')
    print(f'Сжатая строка: {sys.getsizeof(compressed_dna_str.bits)} байтов')


    print("1000000 нуклеотидов")
    dna_str = open('1000000.txt').read().replace('\n', '')
    compressed_dna_str = CompressedDNA(dna_str)
    print(f'Исходная строка: {sys.getsizeof(dna_str)} байтов')
    print(f'Сжатая строка: {sys.getsizeof(compressed_dna_str.bits)} байтов')

    print("10000000 нуклеотидов")
    dna_str = open('10000000.txt').read().replace('\n', '')
    compressed_dna_str = CompressedDNA(dna_str)
    print(f'Исходная строка: {sys.getsizeof(dna_str)} байтов')
    print(f'Сжатая строка: {sys.getsizeof(compressed_dna_str.bits)} байтов')
