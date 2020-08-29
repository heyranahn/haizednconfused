import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = []
    # YOUR CODE GOES HERE
    for value in range(0, 100):
        if value % 3 == 0 and value != 0:
            return_value.append(value**2)
    
    # END SHOULDNT GO BEYOND HERE
    return return_value

if __name__ == "__main__":
   for x in squared_threes():
       print(x)