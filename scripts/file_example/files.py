import pandas
import glob2

file_list = glob2.glob("/home/www/python-studies/scripts/file_example/*.txt")

for file in file_list:
    df = pandas.read_csv(file)
    m = df.mean()
    m = float(m)
    print(m)

