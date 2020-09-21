def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(",")
            for i in range(len(line)):
                line[i] = eval(line[i])
            res.append(line)
            
    return res
            
 