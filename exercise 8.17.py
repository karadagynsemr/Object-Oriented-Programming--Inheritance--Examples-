import numpy as np
class TallySheet:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tallies = {}
        self.min_val = float('inf')
        self.max_val = float('-inf')

    def readValues(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                val = float(line.strip())
                self.tallies[val] = self.tallies.get(val, 0) + 1
                self.min_val = min(self.min_val, val)
                self.max_val = max(self.max_val, val)



def writeHistogram(file_name, values, n_bins=10):
    hist, edges = np.histogram(values, bins=n_bins)

    with open(file_name, 'w') as file:
        for i in range(n_bins):
            file.write(f"{edges[i]:.1f} to {edges[i+1]:.1f}: {hist[i]}\n")

values = [float(line.strip()) for line in open("values.txt")]
writeHistogram("decades.txt", values, n_bins=10)