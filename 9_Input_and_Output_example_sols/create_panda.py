import numpy as np
import pandas as pd

# generate random data
data = np.random.randint(0, high=10, size=(4, 4))

# first column is number 1-4
data[:,0]=np.arange(4)

headers = ["score1", "score2", "score3"]

print(data)

data_frame = pd.DataFrame(data=data[1:,1:],    # values
             	 index=data[1:,0],    # 1st column as index
	     	 columns = headers,   # strings in the list called haeders as the column names
             	 #columns=data[0,1:], # 1st row as the column names
             	 )  

print(data_frame)
