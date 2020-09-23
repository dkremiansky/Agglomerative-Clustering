from sys import modules
from Cluster import Cluster
from Link import Link
from CompleteLink import CompleteLink
from SingleLink import SingleLink


class AgglomerativeClustering:

    # initialize
    def __init__(self, link, samples):
        self.link = link
        self.samples = samples

    def run(self, max_clusters, dist_list):
        cluster_list = self.init_clusters()
        current_link = (getattr(modules[__name__], self.link))
        while len(cluster_list) > max_clusters:
            min_dist = current_link.compute(current_link, dist_list, cluster_list[0], cluster_list[1])
            tmp_dist = 0
            # initialize first clusters
            merge_cluster_i = cluster_list[0]
            merge_cluster_j = cluster_list[1]
            for i_cluster in cluster_list[:-1]:  # rows
                next_i_cluster = cluster_list.index(i_cluster)+1
                for j_cluster in cluster_list[next_i_cluster:]:  # cols
                    tmp_dist = current_link.compute(current_link, dist_list, i_cluster, j_cluster)
                    if tmp_dist < min_dist:
                        merge_cluster_i = i_cluster
                        merge_cluster_j = j_cluster
                        min_dist = tmp_dist
            # merge the clusters and remove one of them from the clusters list
            merge_cluster_i.merge(merge_cluster_j)
            if merge_cluster_i.c_id < merge_cluster_j.c_id:
                cluster_list.remove(merge_cluster_j)
            if merge_cluster_j.c_id < merge_cluster_i.c_id:
                cluster_list.remove(merge_cluster_i)
        print(self.link + ":")
        for cluster in list(sorted(cluster_list, key=lambda cluster: (cluster.c_id))):
            cluster.__str__()

    # initialise a list of clusters, and each cluster contains only one sample
    def init_clusters(self):
        tmp_list = []
        for sample in self.samples:
            tmp_set = {sample}
            tmp_cluster = Cluster(sample.s_id, tmp_set)
            tmp_list.append(tmp_cluster)
        return tmp_list





