def recieve_treats(trick_or_treaters, candy):
    '''
    Adds the given candy to the treats list of each trick_or_treater
    Parameters:
        trick_or_treaters(dict): a dictionary of trick-or-treaters, candy(str): a string representing a candy
    Returns:
        None
    '''
    for tricK_or_treater in trick_or_treaters.values():
        tricK_or_treater["treats"].append(candy)

#Problem 03
def sort_candy(candy_list):
    '''
    Uses the types dict to sort the candies in the candy_list by type
    Parameters:
        candy_list(list): a list of strings, each respresenting a different candy
    Returns:
        dict: types
    '''
    #Setup
    types = {
        'chocolate' : [],
        'fruit' : [],
        'other' : []
    }
    #End Setup
    for candy in candy_list:
        if candy == "hershey bar" or candy == "snickers":
            types["chocolate"].append(candy)
        elif candy == "skittles" or candy == "starburst":
            types["fruit"].append(candy)
        elif candy == "tootsie roll" or candy == "candy corn":
            types["other"].append(candy)
    return types

def main():
    """
    Program entry point.  Handles program workflow (or words to that effect).
    Parameters:
        None
    Returns:
        None
    """
    #Problem 01
    brian = {
        "costume": "wizard",
        "treats" : []
    }

    patrick = {
        "costume": "vampire",
        "treats" : []
    }
    simone = {
        "costume": "mummy",
        "treats" : []
    }

    friends_dict = {
        "brian": brian,
        "patrick": patrick,
        "simone": simone
    }

    friends_dict_items = friends_dict.items()

    #Problem 02
    for candy in "skittles", "snickers" , "candy corn":
        recieve_treats(friends_dict, candy) 

    patrick["treats"].extend(["hershey bar", "starburst", "tootsie roll"])

    #Problem 03
    patricks_candies_sorted = sort_candy(patrick["treats"])
    chocolate_candies = patricks_candies_sorted["chocolate"]
    fruit_candies = patricks_candies_sorted["fruit"]
    other_candies = patricks_candies_sorted["other"]
    return brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies

#Do not modify or delete this line
brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies = main()

#The code below is how main is traditionally called
if __name__ == '__main__':
     main()