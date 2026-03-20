from enum import IntEnum
from typing import Tuple, List

Nucleotideo: IntEnum = IntEnum('Nucleotideo', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotideo, Nucleotideo, Nucleotideo]
Gene = List[Codon]


def string_to_gene(s: str) -> Gene:  # anotação de tipo
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):  # não avança para além do final
            return gene
        # inicializa Codon a partir de 3 nucleotideos
        codon: Codon = (Nucleotideo[s[i]], Nucleotideo[s[i + 1]], Nucleotideo[s[i + 2]])
        gene.append(codon)

    return gene


def linear_contains(gene: Gene, key_codon: Codon)-> bool:
    for codon in gene:
        if codon == key_codon:
            return True
        return False



gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
my_gene: Gene = string_to_gene(gene_str)
acg: Codon = (Nucleotideo.A, Nucleotideo.C, Nucleotideo.G)
gat: Codon = (Nucleotideo.G, Nucleotideo.A, Nucleotideo.T)
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:  # while there is still a search space
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))  # True
print(binary_contains(my_sorted_gene, gat))  # False