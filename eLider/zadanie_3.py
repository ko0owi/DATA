def counting(l):
    negative_numbers = []
    sum_negative = 0
    positive_number = []
    product_positive = 1
    for number in l:
        if number > 0:
            positive_number.append(number)
            product_positive *= number
        else:
            negative_numbers.append(number)
            sum_negative += number

    average_of_negative_numbers = (sum_negative / len(negative_numbers))*-1
    print(average_of_negative_numbers)
    print(product_positive)




