# Answer to Review Excercise: Python files - Importing user-defined functions.
import reading_functions as rf

print(rf.read_whole("../sample_data/dot.txt"))




# Answer to Review Exercise: Importing Python files from subdirectories - reading part of a text file.
import functions.more_reading_functions as mf

print(mf.first_n_lines(10, "../sample_data/sea.txt", mode="r"))

print(mf.last_n_lines(10, "../sample_data/sea.txt", mode="r"))
