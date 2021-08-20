for i in range(10):
    a = i+1
    for j in range(10):
        b = j+1
        ab = 10 * a + b      
        if(ab/(10*b+5) == a/5):
            print(f"a is {a}, b is {b}")

