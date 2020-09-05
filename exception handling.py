def division(a,b):
    try:
        print (a/b)
    except(ZeroDivisionError):
        print("you cannpt devide by 0")
    except (TypeError):
        print("please check you input")
    finally:#executed for each reading
        print("finally executed")

division(45,12)
division(99,33)
division(32,0)
division(2,"t")
