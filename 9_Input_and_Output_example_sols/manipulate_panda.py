from pandas import read_csv
import matplotlib.pyplot as plt

headers = ["X","Y"]

unlabelled_vert = read_csv('../sample_data/noHeader_noIndex_vert.csv', names=headers)

unlabelled_vert.insert(loc=2, column='Z', value=(unlabelled_vert.X * unlabelled_vert.Y + 50))

print(unlabelled_vert)

unlabelled_vert.plot("X", "Z", kind="scatter")

plt.show()
