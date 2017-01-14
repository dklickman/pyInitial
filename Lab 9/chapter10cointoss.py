import random

# The Coin class simulates a coin that can be flipped

class Coin:
    # The __init__ method initialized the sideup data
    # attribute with "Heads."
    def __init__(self):
        self.sideup = 'Heads'

    # The Toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to "Heads"
    # otherwise, sideup is set to "Tails."

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    # the get_sideup method returns the value
    # referenced by sideup

    def get_sideup(self):
        return self.sideup
    


def main():
    # Create an object from the Coin class
    my_coin = Coin()

    # Display the results of the coin that is facing up
    print("This side is up: ", my_coin.get_sideup())
        
    # Toss the coin
    print("I am tossing that coinage dude.")
    my_coin.toss()

    # Display the side of the coin taht isfacing.
    print("This side is up:", my_coin.get_sideup())

# Call that sweet main
main()
