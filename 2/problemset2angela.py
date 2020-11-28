# START PROBLEM SET 02
print('Problem Set 02')

# PROBLEM 1 (20 points)
print('\nProblem 1')

cases = [11, 10, 38, 19, 27]

cases_latest = cases[4]

cases[0] = 9

# PROBLEM 2 (20 points)
print('\nProblem 2')

tests = []

tests.append(867)
tests.append(854)
tests.append(1494)
tests.append(1712)
tests.append(1667)

tests_max = max(tests)

tests_max_index =  tests.index(tests_max)

# PROBLEM 3 (20 points)
print('\nProblem 3')

weeks = ' Aug.09,Aug.16,Aug.23,Aug.30,Sep.06 '

weeks_list = weeks.replace('.','').strip().split(',')

print (weeks_list)

# PROBLEM 4 (20 points)
print('\nProblem 4')

weeks_new = '|'.join(weeks_list)
aug_count = weeks_new.count('Aug')

# PROBLEM 5 (20 points)
print('\nProblem 5')

date = 'Aug30'
test_num = 1712
case_num = 19
most_tests = F"In the week starting on {date}, UM has conducted {test_num} tests and reported {case_num} cases."

date = 'Aug23'
test_num = 1494
case_num = 38
most_cases= F"In the week starting on {date}, UM has conducted {test_num} tests and reported {case_num} cases."



#NOTES 
#weeks = ' Aug.09,Aug.16,Aug.23,Aug.30,Sep.06 '

#weeks_list = weeks.strip().replace('.','').split(',')

#print(weeks_list)

#' Aug.09,Aug.16,Aug.23,Aug.30,Sep.06 '
#Aug.09,Aug.16,Aug.23,Aug.30,Sep.06
#Aug09,Aug16,Aug23,Aug30,Sep06 
#['Aug09', 'Aug16', 'Aug23', 'Aug30', 'Sep06']