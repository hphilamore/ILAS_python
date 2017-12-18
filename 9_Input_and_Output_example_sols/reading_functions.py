# Answer to Review Excercise: Python files - Storing Functions.

# function to read whole file with default argument to read only mode="r"
def read_whole(file, mode="r"):
	"Reads whole file. Returns contents" 
	with open(file, mode) as f:
		contents = f.read()
		return contents

# to test
#print(read_whole("../sample_data/poem.txt", "r"))

#print(read_whole("../sample_data/poem.txt"))
	
