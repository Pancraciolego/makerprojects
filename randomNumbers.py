import random
import turtle as trt

t = trt.Turtle()
t.speed('fastest')
colors = ["red","orange","green","blue","purple","black","gray","pink","gold","cyan"]

def shapeOne():
    color = random.choice(colors)
    t.pencolor(color)
    t.setheading(0)
    t.forward(8)
    t.backward(4)
    t.left(90)
    t.forward(8)
    t.left(135)
    t.forward(6)

def shapeZero():
    color = random.choice(colors)
    t.pencolor("black")
    t.setheading(0)
    t.penup()
    t.forward(4)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(4)
    t.end_fill()

def squares():
    for i in range(4):
        t.forward(8)
        t.left(90)


def findPlacement(randomNumber,listed):     #Organizes a point into a list
    try:                        #for yrange type lists
        timesLooped = -1
        for i in listed:
            timesLooped += 1
            if i < randomNumber:
              continue
            elif i > randomNumber:
              listed.insert(timesLooped,randomNumber)
              break
    except TypeError:           
        timesLooped = -1        # for x,yrange type lists
        x, yrange = randomNumber
        for i in listed:
            timesLooped += 1
            otherx ,otheryrange = i
            if otherx < x:
              continue
            elif otherx > x:            #from least to greatest
              listed.insert(timesLooped,randomNumber)
              break

def checkInFront(y,index,listed):       #Checks for the x values infront of the coordinate, y
    try:
        timeslooped = 0
        difference = 0
        for i in range(11):
            difference += 1
            timeslooped +=1
            value1 = listed[index]
            onex, oneyrange = value1
            value2 = listed[index + timeslooped] # coordinate being checked
            twox, twoyrange = value2    
            if abs(onex - twox) == difference:  #checking if the x line exists
                try:
                    for i in range(10):
                        try:
                            indexof = twoyrange.index(y+i)  #checks if the y value exists inside the x line 
                            return True
                        except ValueError:
                            continue
                    indexof = twoyrange.index(y)    #if it never passes indexof, it will never return true leading to no points infront
                except ValueError:
                    continue
            else:
                timeslooped -= 1
                continue
        return False
    except IndexError:
        print("All good")
        return False


#lister =[1,2,3,4,5,6]
#isItBad = checkInFront(1,lister)       (testing)
#print(isItBad)

def create(number):     #creates a random number
    timeslooped = 0
    while True:
        if timeslooped > 30:
            return TypeError    #when no more lines can be created, it does findx
        randomcor = random.choice(number)
        indexcor = number.index(randomcor)      #choses random xline
        if indexcor == 0:
            indexcor += 1
        firstcor = number[indexcor]
        secondcor= number[indexcor-1]           #xline behind the original one
        firstx, firstyrange = firstcor
        secondx, secondyrange = secondcor
        if abs(firstx-secondx) < 4:         #checks that an xline can be created, if not redo the function
            timeslooped += 1
            continue
        upperbound = firstx -1 
        lowerbound = secondx +1
        randomx = random.randint(lowerbound,upperbound)         #creates the xline.
        if randomx >= 488:                                  #makes sure xline can be checked in the future
            continue
        randomy = random.randint(-500,500)
        while randomy >= 490:
            randomy = random.randint(-500,500)              #creates y value
        newRangey = [-500,500]
        findPlacement(randomy,newRangey)                
        findPlacement(randomy+10,newRangey)
        newcoordinate = [randomx,newRangey]                #makes new coordinate with [x,[-500,lowerbound-yvalue,upperbound-yvalue,500]]
        print(newcoordinate)
        findPlacement(newcoordinate,number)
        isItBad = checkInFront(randomy,number.index(newcoordinate),number)      #checks if it disturbs another one or zero(also for when no more xlines can be created)
        if isItBad:
            number.remove(newcoordinate)
            raise TypeError
        addToSide(randomy,randomy+10,newcoordinate,number)              #since here only one xline is created, addToside creates the other xlines that make the width of the one or zero
        print(number)   
        return randomx, randomy                 #returns coordinates for turtle

def findx(listed):      #Creates a coordinate from a existing x line
    finding = True
    while finding:
        randomx = random.choice(listed)         #chooses random xline
        indexofx = listed.index(randomx)
        x, yrange = randomx
        if x >= 488:
            continue
        randomy = random.choice(yrange)         #starts choosing value from yrange
        indexOf = yrange.index(randomy)
        if randomy >= 490:                      #makes it possible for the cor to fit -500 to 500
            continue
        elif indexOf%2 == 0:                #chooses an even if it is odd
            indexOf +=1                     #even upperbounds are possible
            print(randomy)                  #odd upperbound aren't
            print(yrange)
            randomy = yrange[indexOf]
        randomUpperBound = randomy
        if randomUpperBound >=490:                  #checks for new upperbound
            randomUpperBound-=10
        randomLowerBound = yrange[indexOf-1]
        if abs(randomUpperBound - randomLowerBound) < 11:             #checks for enough space to create cor
            continue
        randomNumber = random.randint(randomLowerBound,randomUpperBound-1)   #creates random y value
        findPlacement(randomNumber,yrange)                      #places it into the yrange
        indexRandom = yrange.index(randomNumber)
        if checkInFront(randomNumber,indexofx,listed):              #checks if it disturbs any infront
            yrange.remove(randomNumber)
            continue
        findPlacement(randomNumber+8,yrange)                #complestes upper bound
        lowerbound = randomNumber
        upperbound = lowerbound + 10
        coordinate = [x,yrange]
        addToSide(lowerbound,upperbound,coordinate,listed)          #completes width
        return x, randomNumber      

def addToSide(lowerbound,upperbound,coordinate,listed):     #adds the x line to 11 spaces, the width of zeros and ones
    for i in range(1,11):
        doIt = True
        xcor,yrange = coordinate
        for coordinates in listed:
            if xcor + i in coordinates:
                otherxcor, otheryrange = coordinates        #if the cor exists, just plug it in
                findPlacement(lowerbound,otheryrange)
                findPlacement(upperbound,otheryrange)
                doIt = False
                break
        if doIt:                                            # if the cor doesn't exist, create a new xline
            newx = xcor + i
            newyrange = [-500,500]
            findPlacement(lowerbound,newyrange)
            findPlacement(upperbound,newyrange)
            newcor = [newx,newyrange]
            findPlacement(newcor,listed)
            
def choose():         #picks random number 0 or 1
    randomer = random.randint(0,1)
    if randomer == 1:
        shapeOne()
    elif randomer == 0:
        shapeZero()


def getx(x,what):                            #moves the turtle and makes zeros and ones.
    print(what)
    interger = random.randint(0,3)
    if interger == 0 or interger == 1 or interger == 2:
        try:
            randomx, randomy = create(x)
            t.penup()
            t.goto(randomx,randomy)
            t.pendown()
            what()
        except TypeError:
            xcor, ycor = findx(x)
            t.penup()
            t.goto(xcor,ycor)
            t.pendown()
            what()
    else:
        axcor, aycor = findx(x)
        t.penup()
        t.goto(axcor,aycor)
        t.pendown()
        what()

def randomizer():   # For testing purposes
    randomnumber = random.randint(0,1)
    if randomnumber == 0:
        return ValueError
    if randomnumber == 1:
        return 1

def trying(): # For testing purposes
    try:
        x = randomizer() + 1
        print(x)
    except TypeError:
        print(0)


numbers = [[-500,[-500,500]],[500,[-500,500]]]

choices = ["square", "numbers","number","squares"]

choice = input("Do you want a square or numbers ")

while choice not in choices:
    print("Invalid, Try Again! ")           #while loop to accept only choices
    choice = str(input("Do you want a square or numbers "))

def what():         #function to return function
    if choice == "square" or choice == "squares":
        return squares
    elif choice == "number" or choice == "numbers":
        return choose



while True:                 #forever!!
    getx(numbers, what())


wn = trt.Screen()
wn.mainloop()
