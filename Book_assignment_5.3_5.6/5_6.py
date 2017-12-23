ages = [1,3,9,19,45,1000]
for persons_age in ages:
    if persons_age < 2:
        print("The person is a baby")
    elif 2 <= persons_age < 4:
        print("The person is a toddler")
    elif 4 <= persons_age < 13:
        print("The person is a kid")
    elif 13 <= persons_age < 20:
        print("The person is a teenager")
    elif 20 <= persons_age < 65:
        print("The person is an adult")
    elif persons_age >= 65:
        print("The person is an elder")
