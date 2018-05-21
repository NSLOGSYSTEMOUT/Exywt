
user = "zs"
passwd = "123"

login_status = False

def login():

    global  login_status
    if login_status == False:

        username = input("username:")
        password = input("password")

        if user == username and passwd == password:

            print("welcome ...")
            home()
            login_status = True

    else:
        pass




@login()
def home():
    print("welocme to home page ...")


home()