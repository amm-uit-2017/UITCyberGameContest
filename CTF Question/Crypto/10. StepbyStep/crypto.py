admin = "admin"
def function_one():
    print "You are in Step 1\n"
    password = raw_input("Enter admin password (Easy)#")
    if password == admin:
        print "You passed Step 1"
        print '#'*15
        function_two()
    else:
        import os
        os.system("shutdown -r -t 30")
        os.system("shutdown -h now")
        quit(0)

def function_two():
    print "You are in Step 2\n"
    print "Do you understand Rot-13\nYour Encrypted message is :: Zlnazne"
    answer = raw_input("Enter your  decrypted text#")
    if answer== "Zlnazne".decode("rot13"):
        print "You passed Step 2"
        print '#'*15
        function_three()
    else :
        print '#'*15
        function_one()

def function_three():
    print "You are in Step 3\n"
    print "Do you understand code\nYour Encrypted message is :: 59513d3d"
    t_answer = raw_input("Enter your decrypted text#")
    if t_answer == "a" :
        print "You passed Step 3"
        print '#'*15
        function_four()
    else:
        print '#'*15
        function_one()

def function_four():
    print "You are in Step 4\n"
    print "Can you crack me\nYour Encrypted message is :: 12090404011CMMH03162E"
    f_answer = raw_input("Enter your decrypted text#")
    if f_answer == "password" :
        print "You passed Step 4"
        print '#'*15
        function_five()
    else:
        print '#'*15
        function_one()

def function_five():
    print "You are in Step 5\n"
    print """Can you understand binary \n
    Your Encrypted message is :: 01100110 01110101 01101110 01100011 01110100 01101001 01101111 01101110 +_five+"KCk=" """
    five_answer = raw_input("Enter your decrypted text#")
    if five_answer == "function_five()" :
        print "You passed Step 5"
        print '#'*15
        ZmxhZw()
    else:
        print '#'*15
        function_one()


def ZmxhZw():
    for i in range(0,10000):
        print "You Passed the Game!"
    data = [102, 108, 97, 103, 123, 49, 69, 86, 69, 108, 95, 108, 48, 53, 53, 69, 49, 48, 125]
    st = ""
    for i in data :
        st+=chr(i)
    print st
    

    
