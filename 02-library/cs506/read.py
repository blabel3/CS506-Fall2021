def parse_data(entry):
    if (entry.isnumeric()):
        return int(entry)
    try:
        return float(entry)
    except ValueError:
        #string
        return entry.replace("'", "").replace('"', "")

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    file = open(csv_file_path, "r")
    file_content = file.read()
    file.close()
    
    file_lines = file_content.splitlines()
    
    data_matrix = [line.split(',') for line in file_lines]

    cleaned_matrix = [[parse_data(entry) for entry in row] for row in data_matrix]
        
    return cleaned_matrix
