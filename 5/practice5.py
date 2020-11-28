recipe = [
    'Preheat oven to 350 degrees F (175 degree C).\n',
    'Place the sliced apples in a 9x13 inch pan.\n',
    'Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over the apples.\n',
    'Pour water evenly over all.\n',
    'Combine the oats, 1 cup of flour, brown sugar, baking powder, baking soda and melted butter together.\n',
    'Crumble evenly over the apple mixture.\n',
    'Bake at 350 degrees F (175 degrees C) for about 45 minutes.'
    ]

def create_step_length(step_list):
    step_length = {}

    for step in step_list:
        step_order, step_content = step.split(": ")
        step_length[step_order.lower()] = len(step_content)

    return step_length

p3_test = ['Step1: Preheat oven','Step2: Place the sliced apples','Step3: Mix the white sugar']
p3_test_ans = {'step1': 12, 'step2': 23, 'step3': 19}
p3_res = create_step_length(p3_test)
print(f"\nProblem 3:\nThe following two lines should be the same: \n{p3_test_ans}")
print(f"{p3_res}")

