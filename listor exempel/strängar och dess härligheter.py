import random


dice_1 = """

    *

"""

dice_2 = """
*

        *
"""

dice_3 = """
        *
    *
*
"""

dice_4 = """
*       *
    *
*       *
"""

dice_5 = """
*       *
    *
*       *
"""

dice_6 = """
*       *
*       *
*       *
"""
# '*\t*\r\v*\t*\r\v*\t*' -> ekvivalent med dice_6

# print('-'*20)
# print(dice_1)
# print('-'*20)
# print(dice_2)
# print('-'*20)
# print(dice_3)
# print('-'*20)
# print(dice_4)
# print('-'*20)
# print(dice_5)
# print('-'*20)
# print(dice_6)

random_dice_number = random.randint(1,6)

# The if way
if random_dice_number == 1:
    print(dice_1)

elif random_dice_number == 2:
    print(dice_2)

elif random_dice_number == 3:
    print(dice_3)

elif random_dice_number == 4:
    print(dice_4)

elif random_dice_number == 5:
    print(dice_5)

else:
    print(dice_6)

# The list way

list_of_dice = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]

print(list_of_dice[random_dice_number - 1])

print(dice_1 + dice_2)