import sys
from Data import Data
from AgglomerativeClustering import AgglomerativeClustering as AC


# prepare upper triangular matrix of the distances between the samples
def calculate_distances(samples):
    n = len(samples)
    dist_list = [0]*n
    samples_list = list(sorted(samples, key=lambda sample: (sample.s_id)))
    for sample1 in samples_list[:-1]:
        next_sample1 = samples_list.index(sample1)+1
        row_list = [0] * n
        for sample2 in samples_list[next_sample1:]:
            row_list[sample2.s_id] = sample1.compute_euclidean_distance(sample2)
        dist_list[sample1.s_id] = row_list
    return dist_list


def main(argv):

    # initialize input args
    if len(argv) < 4:
        print('Not enough arguments provided.')
        exit(1)
    input_path = argv[1]
    links_list = [(item) for item in argv[2].strip().split(', ')]
    for i in range(len(links_list)):
        links_list[i] = links_list[i].replace('_', '')
    num_clusters_required = int(argv[3])

    # load the data
    data = Data(input_path)
    samples = data.create_samples()
    dist_list = calculate_distances(samples)
    for link in links_list:
        agglomer_obj = AC(link, samples)
        agglomer_obj.run(num_clusters_required, dist_list)
        print("")
        print("")



if __name__ == "__main__":
    main(sys.argv)