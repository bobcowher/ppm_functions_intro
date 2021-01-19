def sum_eo(n, t):

    num_array = []
    if t == "e":
        number = 2
        while number <= int(n):
            num_array.append(number)
            number += 2
    elif t == "o":
        number = 1
        while number <= int(n):
            num_array.append(number)
            number += 2
    else:
        return -1

    final_value = 0
    for num in num_array:
        final_value += num
    return final_value


while True:
    evenodd = input("Please filter on even/odd by entering 'e' or 'o': ")
    number  = input("Please enter a number to count to: ")



    if(evenodd == "e"):
        print("The sum of all even numbers up to {0} is {1}".format(number, sum_eo(number, evenodd)))
    elif(evenodd == "o"):
        print("The sum of all odd numbers up to {0} is {1}".format(number, sum_eo(number, evenodd)))