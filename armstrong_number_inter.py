"""
calculate if it's armstrong
"""


def arms(n):

    calc_arms = n  # preserve to compare in the end
    calc_dig = n   # preserve to count digits
    n_digts = 0   # count digits
    while calc_dig >= 1:
        n_digts += 1
        calc_dig = calc_dig // 10
    
    sum_arms = 0  # count armstrong
    while calc_arms >=1:  
        res = calc_arms % 10
        sum_arms += res**n_digts
        calc_arms = calc_arms // 10

        
    if sum_arms == n:
        return n
    

def main():

    start = "yes"
    while start == "yes":
        start = input("Want to check if it's armstrong number? ")

        if start == "yes":
            while True:
                min_range = input("Enter minimum range value: ")
                max_range = input("Enter maximun range value: ")
                if min_range.isnumeric() and max_range.isnumeric():
                    min_range = int(min_range)
                    max_range = int(max_range)
                    if min_range > 0 and max_range > 0 and max_range > min_range:
                        break
                else:
                    print("Input ERROR. Try again.")
            res = []
            for x in range (min_range, max_range+1):
                if arms(x) == x:
                    res.append(arms(x))
            
            print ("It's armstrong number ", res)


        else:
            print ("Program sucessfully completed.")









main()

