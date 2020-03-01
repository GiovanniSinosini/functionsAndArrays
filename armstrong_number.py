"""
calculate if it's armstrong
"""


def arms(n):

    calc_arms = n  # preserve to compare in the end
    calc_dig = n
    n_digts = 0   # count digits
    while calc_dig >= 1:
        n_digts += 1
        calc_dig = calc_dig // 10
    
    sum_arms = 0  # count armstrong
    while calc_arms >=1:  
        res = calc_arms % 10
        sum_arms += res**n_digts
        calc_arms = calc_arms // 10

    arms_res = "it's an armstrong number."
    no_arms = "it's NOT an armstrong number."
    
    if sum_arms == n:
        return arms_res
    else:
        return no_arms 

def main():

    start = "yes"
    while start == "yes":
        start = input("Want to check if it's armstrong number? ")

        if start == "yes":
            while True:
                n = input("Enter number: ")
                if n.isnumeric():
                    n = int(n)
                    break
                else:
                    print("Input ERROR. Try again.")
            
            print (n, arms(n))


        else:
            print ("Program sucessfully completed.")









main()

