from Link import Link


class CompleteLink(Link):

    #  override an abstract method and computing distance between two clusters according to the complete link algorithm
    def compute(self, dist_list, cluster, other):
        max_distances = 0
        tmp_dist = 0
        for sample1 in cluster.samples:
            for sample2 in other.samples:
                # find the distance in the upper triangular matrix of distances
                max_index = sample1.s_id if sample1.s_id > sample2.s_id else sample2.s_id
                min_index = sample1.s_id if sample1.s_id < sample2.s_id else sample2.s_id
                tmp_dist = dist_list[min_index][max_index]
                if max_distances < tmp_dist:
                    max_distances = tmp_dist

        return max_distances

