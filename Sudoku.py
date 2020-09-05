import numpy as np
import random

a = np.zeros((9, 9), dtype=np.uint8)
done = True
queue1 = True
queue2 = True
queue3 = True
queue4 = True
queue5 = True
queue6 = True
queue7 = True
queue8 = True
queue9 = True
icount = 0
q3count = 0
q5count = 0
q6count = 0
q7count = 0
q8count = 0
q9count = 0


def get_value(q, k):
    return q[k]


def arrange(q, rs, re, cs, ce):
    for i in range(rs, re):
        for j in range(cs, ce):
            k = 0
            success = True
            while success:
                val = get_value(q, k)
                if val not in a[i, :] and val not in a[:, j]:
                    a[i, j] = val
                    q.remove(val)
                    success = False
                else:
                    if len(q) - 1 != k:
                        k += 1
                        success = True
                    else:
                        break


def make_zero(rs, re, cs, ce):
    for i in range(rs, re):
        for j in range(cs, ce):
            a[i, j] = 0


def rand_num():
    rn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(rn)
    return rn


def smain():
    global done
    global queue1
    global queue2
    global queue3
    global queue4
    global queue5
    global queue6
    global queue7
    global queue8
    global queue9
    global icount
    global q3count
    global q5count
    global q6count
    global q7count
    global q8count
    global q9count

    while done:
        icount += 1
        if icount > 200:
            icount = 0
            queue1 = True
            queue2 = True
            queue3 = True
            queue4 = True
            queue5 = True
            queue6 = True
            queue7 = True
            queue8 = True
            queue9 = True
            make_zero(0, 3, 0, 3)
            make_zero(0, 3, 3, 6)
            make_zero(0, 3, 6, 9)
            make_zero(3, 6, 0, 3)
            make_zero(3, 6, 3, 6)
            make_zero(3, 6, 6, 9)
            make_zero(6, 9, 0, 3)
            make_zero(6, 9, 3, 6)
            make_zero(6, 9, 6, 9)

        if queue1:
            q1 = rand_num()
            arrange(q1, 0, 3, 0, 3)
            if len(q1) != 0:
                queue1 = True
                make_zero(0, 3, 0, 3)
            else:
                queue1 = False
        elif queue2:
            q2 = rand_num()
            arrange(q2, 0, 3, 3, 6)
            if len(q2) != 0:
                queue2 = True
                make_zero(0, 3, 3, 6)
            else:
                queue2 = False
        elif queue3:
            q3 = rand_num()
            arrange(q3, 0, 3, 6, 9)
            if len(q3) != 0:
                q3count += 1
                queue3 = True
                make_zero(0, 3, 6, 9)
                if q3count > 15:
                    q3count = 0
                    queue2 = True
                    queue1 = True
                    make_zero(0, 3, 3, 6)
                    make_zero(0, 3, 0, 3)
            else:
                queue3 = False
        elif queue4:
            q4 = rand_num()
            arrange(q4, 3, 6, 0, 3)
            if len(q4) != 0:
                queue4 = True
                make_zero(3, 6, 0, 3)
            else:
                queue4 = False
        elif queue5:
            q5 = rand_num()
            arrange(q5, 3, 6, 3, 6)
            if len(q5) != 0:
                q5count += 1
                queue5 = True
                make_zero(3, 6, 3, 6)
                if q5count > 15:
                    q5count = 0
                    queue4 = True
                    make_zero(3, 6, 0, 3)
            else:
                queue5 = False
        elif queue6:
            q6 = rand_num()
            arrange(q6, 3, 6, 6, 9)
            if len(q6) != 0:
                q6count += 1
                queue6 = True
                make_zero(3, 6, 6, 9)
                if q6count > 15:
                    q6count = 0
                    queue4 = True
                    queue5 = True
                    make_zero(3, 6, 0, 3)
                    make_zero(3, 6, 3, 6)
            else:
                queue6 = False
        elif queue7:
            q7 = rand_num()
            arrange(q7, 6, 9, 0, 3)
            if len(q7) != 0:
                q7count += 1
                queue7 = True
                make_zero(6, 9, 0, 3)
                if q7count > 20:
                    q7count = 0
                    queue4 = True
                    queue5 = True
                    queue6 = True
                    make_zero(3, 6, 0, 3)
                    make_zero(3, 6, 3, 6)
                    make_zero(3, 6, 6, 9)
            else:
                queue7 = False
        elif queue8:
            q8 = rand_num()
            arrange(q8, 6, 9, 3, 6)
            if len(q8) != 0:
                queue8 = True
                make_zero(6, 9, 3, 6)
                if q7count > 20:
                    q7count = 0
                    queue7 = True
                    make_zero(6, 9, 0, 3)
            else:
                queue8 = False
        elif queue9:
            q9 = rand_num()
            arrange(q9, 6, 9, 6, 9)
            if len(q9) != 0:
                q9count += 1
                queue9 = True
                make_zero(6, 9, 6, 9)
                if q9count > 30:
                    q9count = 0
                    queue7 = True
                    queue8 = True
                    make_zero(6, 9, 0, 3)
                    make_zero(6, 9, 3, 6)
            else:
                queue9 = False
        else:
            done = False

    return a

