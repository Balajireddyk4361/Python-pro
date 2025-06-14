# def add():
#     print('Addition')

# id(add)

# print(type(add()))



#
# innerfunction

def outer():
    print('outer function')

    def inner():
        print('inner function ')
    inner()
    inner()

    def login():
        print('login functon ')

    login()
    login()

outer()

#---------------------------------------------------------
# 2)
#how to invoke inner function into outer function

def out():
    print('print outer logo')

    def inn():
        print('print inner logo')
    return inn
reload=out()
reload()
