emp = {"girish":7000,"raj":20000,"ayush":22000,"aryan":21000,"sumit":23000,"ronny":24000,"urvish":25000,"utsav":26000,"devarsh":27000,"samyak":28000}


def converter(dict):

    names = list(dict.keys())
    income = list(dict.values())

    return names,income

def smaller(emp):
    names,income = converter(emp)

    salary = min(income)

    p = 0

    for i in income:

        if i == salary:
            print(names[p],salary)

        else:
            p = p + 1

smaller(emp)