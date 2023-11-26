# imports
import pytest  # used for our unit tests
import random  # used in our function

# function to test
def RandomLotteryPicker():
    """ Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner"""
    lottery_tickets_list = []
    print("creating 100 random lottery tickets")
    # to get 100 ticket
    for i in range(100):
        # ticket number must be 10 digit (1000000000, 9999999999)
        lottery_tickets_list.append(random.randrange(1000000000, 9999999999))
    # pick 2 luck tickets
    winners = random.sample(lottery_tickets_list, 2)
    print("Lucky 2 lottery tickets are", winners)
    return winners, lottery_tickets_list  # return values for testing

# unit tests
def test_RandomLotteryPicker():
    # call the function
    winners, lottery_tickets_list = RandomLotteryPicker()

    # check if two unique winners are returned
    assert len(winners) == 2
    assert winners[0] != winners[1]

    # check if winners are in the list of generated tickets
    assert winners[0] in lottery_tickets_list
    assert winners[1] in lottery_tickets_list

    # check if 100 unique tickets are generated
    assert len(lottery_tickets_list) == 100
    assert len(set(lottery_tickets_list)) == 100

    # check if all tickets are within the specified range
    assert all(1000000000 <= ticket <= 9999999999 for ticket in lottery_tickets_list)