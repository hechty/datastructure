#! /usr/bin/env python3
#3.13 Hot Potato using queue data


from Queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


def main():
    s = input("Please input namelist split by space:")
    namelist = s.split()
    num = int(input('Please input a num:'))
    print('winner is ',hotPotato(namelist, num))


if __name__ == '__main__':
    main()

