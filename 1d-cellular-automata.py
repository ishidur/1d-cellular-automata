import numpy as np
import matplotlib.pyplot as plt

r = 1  # number of neighbors
timeLim = 100  # limit of time
# size = timeLim + 1 
size = timeLim * 2 + 1  # width odd number is ideal

ruleNo = 135

binaryRule = format(ruleNo, '0' + str(np.power(2, (2 * r + 1))) + 'b')
rules = list(binaryRule)  # split
print(ruleNo, binaryRule)


# [1,1,,,1] -> rules[0], [1,1,,,0] -> rules[1],,, [0,0,,,0] -> rules[2^(2*r+1)-1]
#     2^(2*r+1)          2^(2*r+1)-1                  0

# apply rule
def validate(neighbors):
    '''
    :param neighbors: array of neighbor cell state values
    :return: next step cell state value
    '''
    b = ''
    for num in neighbors:
        b += str(num)
    index = np.power(2, (2 * r + 1)) - 1 - int(b, 2)
    return int(rules[index])


# update row
def update(u):
    '''
    :param u: array of all cell state
    :return: array of next step all cell state
    '''
    u_next = []
    for num in range(size):
        nbs = []
        for i in range(num - r, num + r + 1):
            nbs.append(u[i % size])
        u_next.append(validate(nbs))
    return u_next


if __name__ == '__main__':
    # initial values
    # U = np.random.randint(2, size=size)  # random
    U = np.zeros(size, dtype=np.int)
    U[int((size - 1) / 2)] = 1

    W = np.array([U])
    for j in range(timeLim):
        U = update(U)
        W = np.vstack((W, U))

    fig = plt.figure(dpi=150, figsize=[10, 5])
    ax = fig.add_subplot(111)
    # ax.set_title("Rule No. {}, {}".format(ruleNo, binaryRule))
    ax.tick_params(labelcolor='white', color='white')
    img = ax.imshow(W, interpolation="nearest", cmap=plt.cm.Greys)
    rules = [5, 110, 126, 249]
    for rule in rules:
        print(format(rule, '0' + str(np.power(2, (2 * r + 1))) + 'b'))
    plt.show()
    # plt.savefig('rule'+str(ruleNo)+'.png', bbox_inches='tight', transparent=False)
