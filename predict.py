import matplotlib.pyplot as plt

def pridict(xs, ys, value_for_pridiction):
    plt.plot(xs, ys, color='green', linestyle='dashed', linewidth=1,
             marker='.', markerfacecolor='blue', markersize=12)

    plt.show() # To show the graph of data provided.

    # Creating list for store slope of all points
    slope = []

    for x in range(1, len(xs)):  # Storing slopes
        slope.append((ys[x] - ys[x - 1]) / (xs[x] - xs[x - 1]))

    # Initially setting slope to first element of slope list and count to 1
    m, count = slope[0], 1

    for x in set(slope):
        if slope.count(x) > count:
            m = x
            count = slope.count(x)

    c = ys[0] - m * xs[0]

    return m * value_for_pridiction + c

def main():
    # Sample data
    xs = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    ys = [-2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]

    predicted_value = pridict(xs, ys, int(input('Enter the number to which value is to be pridicted = ')))

    print('The most likely value is =',predicted_value)


if __name__ == '__main__': main()
