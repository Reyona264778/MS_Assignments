


def get_values():
    elements = int(input("Enter the limit of elements : "))
    values = []

    for i in range(elements):
        val = input(f"Enter value {i} : ")
        values.append(val)
    return values
print(get_values())
