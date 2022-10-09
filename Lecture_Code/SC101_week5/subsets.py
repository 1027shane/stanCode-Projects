"""
File: subsets.py
Name: Shane Liu
-------------------------
This file prints all the sub-lists on Console by calling a recursive function.
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    list_sub_lists([1, 2, 3, 4])


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    helper1(lst, [])
    helper2(lst, [], 0)


def helper1(lst, current_lst):
    # Method 1:
    # 長度不固定
    if len(lst) == 0:
        print(current_lst)
    else:
        # Step1: choose
        ele = lst.pop()
        # Step2: explore without the ele
        helper1(lst, current_lst)
        # Step2: explore with the ele
        current_lst.append(ele)
        helper1(lst, current_lst)
        # Step3: un-choose
        current_lst.pop()
        lst.append(ele)


def helper2(lst, current_lst, current_i):
    # Method 2:
    # 單向排列組合，current_i
    print(current_lst)
    for i in range(current_i, len(lst)):
        # Step1: choose
        current_lst.append(lst[i])
        # Step2: explore
        helper2(lst, current_lst, i+1)
        # Step3: un-choose
        current_lst.pop()


if __name__ == '__main__':
    main()
