filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filenames in filenames:
    filenames = filenames.replace('.', '-', 1)
    print(filenames)

