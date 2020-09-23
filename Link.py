from abc import abstractmethod


class Link:

    #  Abstract method of computing distance between two clusters
    @abstractmethod
    def compute(self, dist_list, cluster, other):
        pass


