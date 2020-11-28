# START PROBLEM SET 08 
print('Problem set 08 \n')

# SETUP
import csv

state2state_id = {
    'Alabama' : 'AL',
    'Alaska' : 'AK',
    'Arizona' : 'AZ',
    'Arkansas' : 'AR',
    'California' : 'CA',
    'Colorado' : 'CO',
    'Connecticut' : 'CT',
    'Delaware' : 'DE',
    'Florida' : 'FL',
    'Georgia' : 'GA',
    'Hawaii' : 'HI',
    'Idaho' : 'ID',
    'Illinois' : 'IL',
    'Indiana' : 'IN',
    'Iowa' : 'IA',
    'Kansas' : 'KS',
    'Kentucky' : 'KY',
    'Louisiana' : 'LA',
    'Maine' : 'ME',
    'Maryland' : 'MD',
    'Massachusetts' : 'MA',
    'Michigan' : 'MI',
    'Minnesota' : 'MN',
    'Mississippi' : 'MS',
    'Missouri' : 'MO',
    'Montana' : 'MT',
    'Nebraska' : 'NE',
    'Nevada' : 'NV',
    'New Hampshire' : 'NH',
    'New Jersey' : 'NJ',
    'New Mexico' : 'NM',
    'New York' : 'NY',
    'North Carolina' : 'NC',
    'North Dakota' : 'ND',
    'Ohio' : 'OH',
    'Oklahoma' : 'OK',
    'Oregon' : 'OR',
    'Pennsylvania' : 'PA',
    'Rhode Island' : 'RI',
    'South Carolina' : 'SC',
    'South Dakota' : 'SD',
    'Tennessee' : 'TN',
    'Texas' : 'TX',
    'Utah' : 'UT',
    'Vermont' : 'VT',
    'Virginia' : 'VA',
    'Washington' : 'WA',
    'West Virginia' : 'WV',
    'Wisconsin' : 'WI',
    'Wyoming' : 'WY'
}

# END SETUP

### PROBLEM 1.1
def read_txt(filepath):
    """Returns a list of lists where each item (list) is formed from the data split by tab.

    Parameters:
        filepath (str): a filepath that includes a filename with its extension

    Returns:
        list: a list of lists that contain states and total number of cases
    """
    file_obj = open(filepath, "r")
    data = file_obj.readlines()
    file_obj.close()
    output = []
    for line in data[1:]:
        output.append(line.rstrip('\n').split('\t'))
    return output


### PROBLEM 1.2
def read_csv(filepath):
    """Returns a list of dictionaries where each dictionary is formed from the data.

    Parameters:
        filepath (str): a filepath that includes a filename with its extension

    Returns:
        list: a list of dictionaries where each dictionary is formed from the data
    """
    with open(filepath, "r", newline = '\n', encoding = 'utf-8') as file_obj:
        output = []
        reader = csv.DictReader(file_obj)
        for line in reader:
            output.append(line)
    return output


### PROBLEM 2
def convert_to_dict(data):
    """Returns a dictionary of US state and the total number of COVID-19 cases as key-value pairs.

    Parameters:
        data (list): a list of lists that contain states and total number of cases
    
    Returns:
        dict: a dictionary that contains state and the total number of cases as key-value pairs
    """
    dictionaries = csv.DictReader(data)
    output = {}
    for state, count in data:
        output[state] = count
    return output

### PROBLEM 3
def get_total_num_policies(data):
    """Returns a dictionary of US state id and the total number of state-level policies as key-value pairs.

    Parameters:
        data (list): a list of dictionaries where each dictionary is formed from the data.
    
    Returns:
        state_id_2_policy_counts (dict): a dictionary of US state id and the total number of state-level policies as key-value pairs
    """
    state_id_2_policy_counts = {}
    for policy in data:
        if policy['policy_level'] == 'state' and policy['start_stop'] == 'start':
            state = policy['state_id']
            if state not in state_id_2_policy_counts:
                state_id_2_policy_counts[state] = 1
            else:
                state_id_2_policy_counts[state] += 1
    return state_id_2_policy_counts


### PROBLEM 4
def summarize_data(state2state_id, state_id_2_policy_counts, state_2_case_counts):
    """Returns a list of dictionaries that contain four key-value pairs: US state, US state id, the total number of state-level policies, and the total number of COVID-19 cases.
    
    Keys are state, state_id, total_policies, and total_cases.

    Parameters:
        three dictionaries: 
            state2state_id is a dictionary of state names and their ids as key-value pairs
            state_id_2_policy_counts is a dictionary of US state id and the total number of state-level policies as key-value pairs
            state_2_case_counts is a dictionary of US state and the total number of COVID-19 cases as key-value pairs
    
    Returns:
        data (list): a list of dictionaries with four key-value pairs.
    """
    data = []
    for state, state_id in state2state_id.items():
        state_summary = {}
        #state_summary = {
            #'state_id' : state_id,
            #'state' : state,
            #'total_policies' : state_id_2_policy_counts[state_id],
            #'total_cases' : state_2_case_counts[state]
        #}
        state_summary['state_id'] = state_id
        state_summary['state'] = state
        state_summary['total_policies'] = state_id_2_policy_counts[state_id]
        state_summary['total_cases'] = state_2_case_counts[state]
        data.append(state_summary)
    return data
    


### PROBLEM 5
def write_csv(data, filepath):
    """Writes a csv file from an input data given a filepath.
    
    Parameters:
        data (list): a list of dictionaries with state, state_id, the total number of state-level policies, and the total number of COVID-19 cases.
        filepath (str):  a filepath to store data to a csv file.
    
    Returns:
        None
    """
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main():
    """Program entry point.  Handles program workflow (or words to that effect).

    Parameters:
        None

    Returns:
       None
    """
    pass #TODO implement

    ### Problem 1 (20 points) 
    cases = read_txt("us_covid19_cases.txt")
    policies = read_csv("us_policy_updates.csv")

    ### Problem 2 (10 points)
    state2cases = convert_to_dict(cases)
    # print(state2cases)
    # print(policies)
    ### Problem 3 (30 points)
    state_id2policies = get_total_num_policies(policies)
    # print(state_id2policies)

    ### Problem 4 (30 points)
    summarized_info = summarize_data(state2state_id, state_id2policies, state2cases)
    # print(summarized_info)

    ### Problem 5 (10 points)
    write_csv(summarized_info, "temp.csv")
    state_id = 'AK'
    print(state_id2policies[state_id], state_id)


#Do not delete the lines below.
if __name__ == '__main__':
    main()