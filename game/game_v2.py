from collections import Counter


def game(finger, matrix):
    count = Counter(matrix)
    score = sum(1 for i in range(10) if count[str(i)] and count[str(i)] <= finger * 2)
    return score


def main():
    finger = int(input())
    matrix = ''.join([input() for i in range(4)])
    print(game(finger, matrix))


if __name__ == "__main__":
    main()
