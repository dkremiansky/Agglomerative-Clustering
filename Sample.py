from math import sqrt
from math import pow


class Sample:

    # initialize
    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    # compute the euclidean distance between two point and return it
    def compute_euclidean_distance(self, other):
        temp_sum = 0
        for gene in range((len(self.genes))):
            temp_sum = temp_sum + pow((self.genes[gene] - other.genes[gene]), 2)
        euclidean_distance = sqrt(temp_sum)
        return euclidean_distance

