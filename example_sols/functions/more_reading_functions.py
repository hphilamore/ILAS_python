def first_n_lines(n, file, mode="r"):
	"Returns the first n lines of file"

	with open(file, mode) as f:

		# cast f (the file contents) as a list
		f = list(f)

		for line in f[0:n]:
			print(line, end="")

# to test
# print(first_n_lines(2, "../../sample_data/poem.txt"))

def last_n_lines(n, file, mode="r"):
	"Returns the first n lines of file"

	with open(file, mode) as f:

		# cast f (the file contents) as a list
		f = list(f)

		for line in f[-n:]:
			print(line, end="")		

# to test
# print(last_n_lines(2, "../../sample_data/poem.txt"))

