"""
File: huffman_encoding.py
Name: Shane Liu
-------------------------
This program demonstrates the idea of zipping/unzipping, 
through the algorithm of Huffman Encoding.
"""

from ds import Tree, PriorityQueue
# The string to be zipped/unzipped
TARGET = 'stancode sc001 sc101'


def main():
    print('----------1----------')
    d = build_dict()
    print(d)

    print('----------2----------')
    priority_queue = put_key_val_to_pq(d)
    priority_queue.traversal_tree_elements()

    print('----------3----------')
    tree = encoding_tree(priority_queue)
    bfs(tree)

    print('----------4----------')
    zipped = encoding(tree)
    print(f'{TARGET} (bits: {len(TARGET)*8}) \nEncoded: {zipped} (bits: {len(zipped)})')

    print('----------5----------')
    decoding(tree, zipped)


def build_dict():
    """
    :return: Dict, a Python dictionary containing ch as key,
             the number of ch occurrence as value
    """
    d = {}
    for ch in TARGET:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d


def put_key_val_to_pq(d):
    """
    :param d : Dict[str: int], key is character and the value is its occurance
    :return : PriorityQueue, with Tuple(Tree, count) as its elements
    --------------------------------
    This function constructs a priority queue based on the chatacter occurance in d.
    """
    pq = PriorityQueue()
    for ch, count in d.items():
        tree = Tree(None, ch, None)
        data = (tree, count)
        pq.enqueue(data)
    return pq


def encoding_tree(pq):
    """
    :param pq: PriorityQueue, containing all the ch we need to encode
    :return: Tree, a binary tree that has all the ch encoded
    """
    while True:
        first_data = pq.dequeue()
        first_tree, first_count = first_data  # Method 1

        if pq.is_empty():
            return first_tree

        second_data = pq.dequeue()
        second_tree, second_count = second_data[0], second_data[1]  # Method 2

        # construct a tree
        new_count = first_count+second_count
        new_tree = Tree(first_tree, new_count, second_tree)
        new_data = (new_tree, new_count)
        pq.enqueue(new_data)


def encoding(tree):
    """
    :param tree: Tree, Huffman Tree containing the Huffman codes for characters in TARGET
    :return: str, the zipped string of TARGET
    """
    encoding_d = {}
    dfs(tree, encoding_d, '')
    print(encoding_d)
    # TODO: get all the coding as a single string!
    ans = ''
    for ch in TARGET:
        ans += encoding_d[ch]
    return ans


def dfs(cur, encoding_d, cur_encoding):
    """
    :param cur : Tree, the pointer of current position
    :param encoding_d: Dict[str, str], holding each character as key and its Huffman code as value
    :param cur_encoding: str, the current path encoding ('0' goes left ; '1' goes right)
    """
    if cur.left is None and cur.right is None:  # leaf
        encoding_d[cur.val] = cur_encoding
    else:
        dfs(cur.left, encoding_d, cur_encoding+'0')
        dfs(cur.right, encoding_d, cur_encoding+'1')


def decoding(tree, zipped_words):
    """
    :param tree: Tree, the binary tree that contains all the ch encoded
    :param zipped_words: str, the mystery compressed binary digits to be unzipped
    """
    ans_lst = []
    add_to_ans_lst(tree, zipped_words, ans_lst, tree)
    print('Decoding...')
    print(''.join(ans_lst))  # str.join(sequence)


def add_to_ans_lst(root, zipped_words, ans_lst, cur):
    """
    :param root: Tree, the binary tree that contains all the ch encoded
    :param zipped_words: str, binaries that were zipped from TARGET
    :param ans_lst: List[str], containing characters that are in leaf node
    :param cur: Tree, pointer of where the current node is
    --------------------------------
    This function trace all the binaries in zipped_words down to leaves
    and add the character to ans_lst.
    """
    if cur.left is None and cur.right is None:
        # Base Case!
        ans_lst.append(cur.val)
        if zipped_words:  # len(zipped_words) != 0
            # back to initial
            add_to_ans_lst(root, zipped_words, ans_lst, root)
    else:
        if zipped_words[0] == '0':
            add_to_ans_lst(root, zipped_words[1:], ans_lst, cur.left)
        else:
            add_to_ans_lst(root, zipped_words[1:], ans_lst, cur.right)


def bfs(tree):
    """
    :param tree: Tree, class defined in ds.py in which constructor creates objects with 
                 one value and two pointers.
    --------------------------------        
    This function traverses the tree and prints all elements out
    """
    queue = [tree]
    while len(queue) != 0:
        ele = queue.pop(0)
        print(ele.val, end=' | ')
        if ele.left is not None:
            queue.append(ele.left)
        if ele.right is not None:
            queue.append(ele.right)
    print('')


if __name__ == '__main__':
    main()
