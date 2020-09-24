def pattern(length,height) :
    for i in range(0, height) :
        for j in range(0, length) :

            if (i == 0) :

                if (j == 0 or j == height or
                              j == length - 1) :
                    print ("*", end = "")

                else :
                    print (" ", end = "")

            elif (i == height - 1) :
                print ("*", end = "")

            elif ((j < i or j > height - i) and
                  (j < height + i or
                   j >= length - i)) :
                print ("*", end = "")

            else :
                print (" ", end = "")

        print ()

len = input("Enter the Width: ")
length = int(len)
#height = input("Enter the Height")
height = int((length-1)/2)

pattern(length,height)
