import sys
import math

def main():
    choice = input("Choose Arithmetic (A) or Geometric (G)")

    firstTerm = float(input("what's the first term?"))
    d = float(input("what's the diff or ratio?"))
    nTerms = int(input("what's the total number of terms?"))

    res = ""
    if (str.lower(choice) == 'a'):
        res = arith(firstTerm, d, nTerms)
    else:
        res = geom(firstTerm, d, nTerms)

    print(res)
    print(f"sum of sequence: {sum(res)}")
    print(f"product of sequence: {math.prod(res)}")


# arithmatic 
def arith(firstTerm, d, nTerms):
    result = []
    for n in range(1, nTerms + 1):
        result.append(firstTerm + (n - 1) * d)
    return result



# geometric
def geom(firstTerm, r, nTerms):
    result = []
    for n in range(1, nTerms + 1):
        result.append(firstTerm * (r ** (n-1)))
    return result

if __name__ == "__main__":
    main()