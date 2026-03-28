def sumFloat(tuple1, tuple2, base):
    #@param tupleX (mantissaX,expX): tuple 
    #@param base: int=10
    #@return: tuple 
    #assert len(tuple1)==2 and type(tuple1[0])==float and 0<=tuple1[0]<=1 and type(tuple1[1])==int
    #assert len(tuple2)==2 and type(tuple2[0])==float and 0<=tuple2[0]<=1 and type(tuple2[1])==int
    #assert base == 10
    if tuple1[1] != tuple2[1]:
        m2 = tuple2[0]
        m2 = m2 * base**(tuple2[1]-tuple1[1])

    m = tuple1[0]+m2
    e = tuple1[1]

    if int(m) > 0:
        m /= base
        e += 1

    newTuple = (m, e)
    return newTuple


t1 = (0.932, 4)
t2 = (0.999, 3)

print(sumFloat(t1, t2, 10))

