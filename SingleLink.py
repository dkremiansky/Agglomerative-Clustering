from Link import Link


class SingleLink(Link):

    #  override an abstract method and computing distance between two clusters according to the single link algorithm
    def compute(self, dist_list, cluster, other):
        #  random value to initialize the minimum
        min_distances = 1000
        tmp_dist = 0
        for sample1 in cluster.samples:
            for sample2 in other.samples:
                # find the distance in the upper triangular matrix of distances
                max_index = sample1.s_id if sample1.s_id > sample2.s_id else sample2.s_id
                min_index = sample1.s_id if sample1.s_id < sample2.s_id else sample2.s_id
                tmp_dist = dist_list[min_index][max_index]
                if min_distances > tmp_dist:
                    min_distances = tmp_dist

        return min_distances
