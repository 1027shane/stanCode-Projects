"""
File: dice_rolls_sum.py
Name: Shane Liu
-------------------------
This program finds all the dice rolls permutations that sum up to a constant TOTAL.
Students will find early stopping a good strategy of decreasing the number of recursive calls
"""

# This constant controls the sum of dice of our interest
TOTAL = 8


def main():
    dice_sum(TOTAL)


def dice_sum(target_sum):
    counter = [0]
    dice_sum_helper(target_sum, [], counter)
    print(f'dice_counter: {counter[0]} times')


def dice_sum_helper(target_sum, current_lst, counter):
    counter[0] += 1  # 避免受個別stake frame影響 --> 資料結構不受影響
    if sum(current_lst) <= target_sum:
        if sum(current_lst) == target_sum:
            print(current_lst)
        else:
            for die in [1, 2, 3, 4, 5, 6]:
                # early stopping
                if die+sum(current_lst) > target_sum:
                    break
                else:
                    # Step1: choose
                    current_lst.append(die)
                    # Step2: explore
                    dice_sum_helper(target_sum, current_lst, counter)
                    # Step3: un-choose
                    current_lst.pop()


if __name__ == '__main__':
    main()
