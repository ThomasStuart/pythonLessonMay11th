def adjacentElementsProduct(inputArray):
    # [9, 5, 10, 2, 24, -1, -48]
    # pair 1 -> (9,5)          =  45
    # pair 2 -> (5,10)         =  50
    # pair 3 -> (10,2)         =  20
    # pair 4 -> (2,24)         =  48
    # pair 5 -> (24,-1)        =  -24
    # pair 6 -> (-1,-48)       =  48


    history = []
    for index in range(0, len(inputArray)-1):
        print("(", inputArray[index], inputArray[index+1], ")", end="")
        print( inputArray[index]*inputArray[index+1] )
        history.append(  inputArray[index]*inputArray[index+1] )

    print(history)

    # [45, 50, 20, 48, -24, 48]


    max = history[0]  # 45 
    
    for i in range(0,len(history)):
        LHS = i
        RHS = i + 1
        
        #      45       >      50      tell me 50 is bigger. max is currently 45.  
        #                              max = 50
        #   
            # 45        >    50 
        if history[LHS] > history[RHS]:
                # 45       > 45 
            if history[LHS] > max:
                # max = 50 ??
                max   = history[LHS]
        else:
            print("RHS")



adjacentElementsProduct( [9, 5, 10, 2, 24, -1, -48] )
