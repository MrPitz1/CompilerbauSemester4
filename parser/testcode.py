def example_function(x):
    result = 0
    if x > 10:
        result += x
        for i in range(x):
            if i % 2 == 0:
                result += i
            else:
                result -= i
    else:
        result -= x
        while x < 10:
            x += 1
            result += x
    return result
def main():
    values = [5, 15, 25]
    results = []
    for value in values:
        res = example_function(value)
        results.append(res)
        print("Result for {value} is {res}")
    print("All results computed.")
    a =:
        1:8,2:4if __name__ =="__main__":
    main()
