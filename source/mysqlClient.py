
y=0
z=0
list1=[]

def callFunctions(logger,x,list):
    global list1
    list1=list
    logger.info(list1)
    fun1(logger,x)
    fun2(logger)
    return fun3(logger)
    #return ret

def fun1(logger,x):
    logger.info('fun1')
    global y
    y = x + 1
    logger.info("fun1 %i", x)

def fun2(logger):
    global y
    global z
    logger.info('fun2')
    logger.info("fun2 %i",y)
    z = y + 1

def fun3(logger):
    logger.info('fun3')
    global z
    logger.info("fun3 %i",z)
    return z