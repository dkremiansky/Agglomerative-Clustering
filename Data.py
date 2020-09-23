import pandas as pd
from Sample import Sample


class Data:

    # initialize
    def __init__(self, path):
        df = pd.read_csv(path)
        self.data = df.to_dict(orient='list')
        # print("create_samples", self.create_samples())

    # create set of samples
    def create_samples(self):
        samples_list = []
        for i in range(len(self.data['sample'])):
            s_id = i
            label = self.data['label'][i]
            temp_list = [None] * (len(self.data.keys())-2)
            for gene in range((len(self.data.keys())-2)):
                if gene == (len(self.data.keys())-3):
                    # the last gene has another key name
                    name = 'gene_' + str(gene) +'\t'
                else:
                    name = 'gene_' + str(gene)
                temp_list[gene] = self.data[name][i]
            new_sample = Sample(s_id, temp_list,  label)
            samples_list.append(new_sample)
        samples_set = set(samples_list)
        return samples_set
