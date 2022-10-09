"""
File: priority_queue_list.py
Name: Shane Liu
-------------------------
This program shows how to build a priority queue by using Python "list".
We will be discussing 3 different conditions while appending:
(1)Prepend
(2)Append
(3)Append in between
"""

# This constant controls when to stop the user input
EXIT = ''


def main():
    priority_queue = []

    print('--------------------------------')
    while True:
        name = input('Patient: ')
        if name == EXIT:
            break
        priority = int(input('Priority: '))
        data = (name, priority)

        # first data
        if len(priority_queue) == 0:
            priority_queue.append(data)
        else:
            # (1)Prepend
            if priority < priority_queue[0][1]:
                priority_queue.insert(0, data)
            # (2)Append
            elif priority >= priority_queue[-1][1]:
                priority_queue.append(data)
            else:
                # (3)In between, 一次比較兩個，長度-1
                for i in range(len(priority_queue)-1):  # for loop: NOT dynamic
                    if priority_queue[i][1] <= priority < priority_queue[i+1][1]:
                        priority_queue.insert(i+1, data)
                        break
    print('--------------------------------')

    print(priority_queue)


if __name__ == '__main__':
    main()
