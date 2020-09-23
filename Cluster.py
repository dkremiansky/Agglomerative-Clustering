

class Cluster:

    # initialize
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    # get two clusters and merge them into one
    def merge(self, other):
        if self.c_id < other.c_id:
            self.samples.update(other.samples)
        if self.c_id > other.c_id:
            other.samples.update(self.samples)

    # find the most popular label and calculate it's purity
    def compute_purity(self):
        size = len(self.samples)
        label_dict = {}
        max_key = None
        max_value = 0

        # count the number each label appears in the current cluster
        for sample in self.samples:
            checked = False
            tmp_label = sample.label
            # if the label exist in the label_dict - count it
            for key in label_dict.keys():
                if key == tmp_label:
                    checked = True
                    label_dict[key] += 1
            # if the label does not exist in the label_dict - add new label key and count it
            if checked == False:
                label_dict[tmp_label] = 1

        # find the label with the max appearances
        for key in sorted(label_dict.keys(), key=lambda x: x.lower()):
            if max_value < label_dict[key]:
                max_key = key
                max_value = label_dict[key]

        # compute the purity
        purity = max_value / size
        return purity, max_key

    # print the information about the cluster
    def __str__(self):
        purity, dominate_label = self.compute_purity()
        samples_id_set = set({})
        for sample in self.samples:
            samples_id_set.add(sample.s_id)
        print("Cluster {0}: {1}, dominant label: {2}, purity: {3}".format(self.c_id, sorted(samples_id_set),
                                                                          dominate_label, purity))
