import csv

# START LAB EXERCISE 08
print('Lab Exercise 08 \n')

# PROBLEM 1 (5 Points)
def read_csv_file(input_filepath, delimiter=','):
    """
    This function reads a .csv file and parses it into a list of dictionaries,
    where each dictionary is formed from the data on one line of the .csv file.

    Parameters:
        filepath (str): The location of the file to read and parse.
        delimiter (str): delimiter that overrides the default

    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """
    with open(input_filepath, "r", encoding = 'utf-8') as obj_file:
        output = []
        dictionaries = csv.DictReader(obj_file, delimiter=',')
        for row in dictionaries:
            output.append(row)
    return output

# PROBLEM 2 (5 Points)
def hci_database_urls(library_list):
    """
    This function takes a list of library data and returns a new dictionary of databases in the HCI category.
    only the name of the database and the link to the database will be included.

    Parameters:
        library_list (list): A list of dictionaries, where each dictionary contains the
            information on a specific databas.

    Returns:
        dict: A dictionary where the keys are the name of the HCI database and its permalink
    """
    answer = {db['Name'] : db['Permalink'] for db in library_list if db['Category'] == 'Human Computer Interaction' }
    for db in library_list:
        if db['Category'] == 'Human Computer Interaction':
            answer[db['Name']] = db['Permalink']
    return answer

# PROBLEM 3 (5 Points)
def write_csv_file(output_filepath, dict_to_write, header):
    """
    Writes a .csv file using the < csv > module.

    Parameters:
        output_filepath (str): The file path to the new file being created.
        dict_to_write (dict): The information to include in the file being created.
        header (list): The header row in the table.

    Returns:
        None
    """
    with open(output_filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        rows = sorted(dict_to_write.items())
        writer.writerows(rows)

# PROBLEM 4 (5 Points)
def main():
    """
    Entry point for the program. This function will process the library data.

    Parameters:
        None

    Returns:
        None
    """
    first = read_csv_file (input_filepath = "library_databases.csv" ,  delimiter=',')
    second = hci_database_urls(library_list = first)
    third = write_csv_file(output_filepath = "library_hci_databases.csv", dict_to_write = second, header = ["Name", "Permalink"])

if __name__ == '__main__':
    main()
