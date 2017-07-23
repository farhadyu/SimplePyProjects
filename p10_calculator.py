

# First pass. Looks and forms the numbers.
def fpass(statement):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    a = []
    is_num = False
    was_num = False
    new_statement = []
    for count, i in enumerate(statement):
        if i in nums:
            is_num = True
            a.append(i)
            # LAST ELEMENT CONDITION
            if count == len(statement) - 1:
                new_statement = former(a, new_statement)
                a = []
        else:
            is_num = False
            if is_num == was_num:
                new_statement.append(i)
            else:                               # =======
                new_statement = former(a, new_statement)
                a = []
                new_statement.append(i)
        was_num = is_num
    return new_statement


# Will create and add the number, given the string. Also checks "." count.
def former(a, ns):
    a = "".join(a)
    if a.count(".") > 1:
        print "WRONG FORMAT"
        exit()
    else:
        a = float(a)
        ns.append(a)
        return ns


def spass(statement):
    new_statement = []
    old_str = ""
    was_str = ""
    for i in statement:
        if isinstance(i, float) and was_str == "-":
            i = -i
            del new_statement[-1]
            if isinstance(old_str, float):
                new_statement.append("+")
            new_statement.append(i)
        else:
            new_statement.append(i)
        old_str = was_str
        was_str = i
    return new_statement


def tpass(statement):
    new_statement = []
    for i in statement:
        if i == "^":
            new_statement.append("**")
        else:
            new_statement.append(i)
    statement = new_statement
    new_statement = []
    for i in statement:
        if isinstance(i, str):
            new_statement.append(i)
        else:
            new_statement.append(str(i))
    new_statement = "".join(new_statement)
    return new_statement


def main():
    statement = raw_input("Enter statement:\n>").strip()
    statement = "".join(statement.split(" "))
    statement = fpass(statement)
    statement = spass(statement)
    statement = tpass(statement)
    print statement
    statement = "print " + statement
    exec statement


main()
