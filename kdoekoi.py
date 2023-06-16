#if l%3==0 and not l%5==0:
            #print( "fizz" )
        
        #if l%5==0 and not l%3==0:
            #print( "buzz" )

        #if l%3==0 and l%5==0:
            #print("fizzbuzz")

        
        



def jefry(konecnecislicko):
    pocatecnycislicko = 2
    for l in range (pocatecnycislicko, konecnecislicko+1):
        if l%3==0 and l%5==0:
            print( "fizzbuzz" )
        

        elif l%5==0:
            print( "buzz" )
        elif l%3==0:
            print( "fizz" )

        else:
            print(l)
# funkce

jefry(167)