def string1():
    a=raw_input()
    b=raw_input()
    length1 = len(str(a))
    length2 = len(str(b))
    if length1 > length2:
        print 'String1 is longer'
    else:
        print 'String2 is longer'
    return;
string1()