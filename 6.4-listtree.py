#! /usr/bin/env python3

myTree = ['a', ['b',['d',[],[]],['e',[],[]]],['c',['f',[],[]],[]]]
print(myTree)
print('left subtree = ', myTree[1])
print('root = ',myTree[0])
print('right subtree = ', myTree[2])

def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1,[new_branch,[], []])

    return root

def insert_right(root, new_branch):
    t = root.pop()
    if len(t) > 1:
        root.append([new_branch, [], t])
    else:
        root.append([new_branch, [], [] ])

    return root

def get_root_value(root):
    return root[0]

def set_root_value(root, new_value):
    root[0] = new_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

r = binary_tree(15)
insert_left(r,45)
insert_right(r,73)
insert_left(r,55)
insert_right(r,83)
l = get_left_child(r)
print(r)
print(l)
set_root_value(l, 14)
print(r)
insert_left(l, 11)
print(r)
print(get_right_child(get_right_child(r)))

