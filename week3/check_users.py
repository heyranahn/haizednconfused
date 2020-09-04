import logging
logging.basicConfig(level=logging.DEBUG)

def check_users(current_users, new_users):
    pass
    #YOUR CODE HERE
if __name__ == "__main__":
    current_us = ['chris', 'tabitha', 'Sam', 'miguel', 'katherine']
    new_us = ['thomas', 'kAtHeRiNe', 'PAUL', 'tami']
    check_users(current_us, new_us)
    
    current_us_lower = [us.lower() for us in current_us]
    # new list that's a copy of current users
    # containing lowercase versions of all existing users
    #using list comprehension

    for new_user in new_us:
        if new_user.lower() in current_us_lower:
            print("The username " + new_user + " is taken.")
        else:
            print("That username " + new_user + " is available.")
    #END CODE
