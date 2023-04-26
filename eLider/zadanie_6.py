def delete_numbers(lancuch):
    number = ["0","1","2","3","4","5","6","7","9"]
    word = ""
    numbers = []

    for i in lancuch:
        if i in number:
            numbers.append(i)
        else:
            word += i

    return print(f"lancuch = {word}, ilość cyfr w lancuchu = {len(numbers)}")

#przykład
delete_numbers("asdf23tsdcs3cz2")