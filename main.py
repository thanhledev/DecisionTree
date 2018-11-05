from pkg.ID3 import decision_tree_id3
import decimal

def main():
    # initialize filename
    filename = "credit.csv"

    # edit decimal context
    decimal.getcontext().prec = 5

    # using decision tree with ID3
    decision_tree_id3(filename, "worthy")


if __name__ == '__main__':
    main()
