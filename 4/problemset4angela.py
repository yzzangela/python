# START PROBLEM SET 04
print('Problem Set 04')

# START SET UP
summary = [
    'Step 1: Beat It',
    'Step 2: Prep the Pan',
    'Step 3: Add the Eggs',
    'Step 4: Patience Makes Perfect',
    'Step 5: Almost Done',
    'Step 6: Ready to Eat'
]
recipe = [
    "Beat your eggs until they're completely blended. Add a little water, cream or milk to make them tender. Use 1 tablespoon of liquid per egg. Add a pinch of salt.",
    "Next, heat a nonstick skillet over a medium-low flame and toss in a pat of butter. Make sure the butter coats the pan.",
    "Then, pour in the eggs. Pause to let them heat slightly — gentle heat is essential.",
    "Move the eggs across the pan like a bulldozer so the eggs cook evenly. This takes a little time, but it's worth it.",
    "As the eggs start to set, add chopped fresh herbs, or bits of ham or cheese.",
    "Turn your eggs onto warmed plates and dig in! Watch our how-to video for more."
]

# Problem 01
print('\nProblem 1')
step_length = []
for i in recipe:
    step_length.append(len(i))

gte_100 = 0
less_100 = 0 
for i in step_length:
    if i>100:
        gte_100 = gte_100+1
    if i<100:
        less_100 = less_100+1

fives = 0
tens = 0
new_length = step_length[1:]
for i in new_length:
    if i>100:
        tens = tens + 10
    if i<100:
        fives = fives + 5
step_25_mins = tens + fives

# Problem 02
print('\nProblem 2')
step_order_3 = summary[2]
step_order_sub = step_order_3[0:4] + step_order_3[5:6]
step_order = step_order_sub.upper()
step_detail = recipe[2]
recipe_summary_3 = F"{step_order}: {step_detail}"


recipe_summary = []
for i in summary:
    step_order_summary = i[0:4] + i[5:6]
print(i)

# Problem 03
print('\nProblem 3')
count = recipe[2].count("r")
step_r_num