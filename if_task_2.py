def str_comparison(str1, str2):
    if type(str1) is str and type(str2) is str:
        if str1 == str2:
            return 1
        elif str1 > str2:
            return 2
        elif str1 != str2 and str2 == "learn":
            return 3
    else:
        raise ValueError("Your variables are not string")

test_var = [
    {"str1": "Hello world", "str2": "Hello world"},
    {"str1": "Hello my beautiful world!", "str2": "Hello world"},
    {"str1": "Hello my beautiful world!", "str2": "learn"},
    {"str1": 11111, "str2": "learn"},
]


for i in test_var:
     result = str_comparison(i["str1"], i["str2"])
     print(" The result is {result} \n".format(result = result))