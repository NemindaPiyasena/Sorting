class Search:

    def __init__(self,li):

        self.arr=list(li)
        self.length=len(self.arr)

    def search(self,item,init,end):

        revalue=None
        if init>end:
            revalue=None
            return revalue
        dev=(init+end)//2
        if self.arr[dev]==item:
            revalue=dev
            return revalue
        elif self.arr[dev]>item:
            revalue=self.search(item,init,dev-1)
        elif self.arr[dev]<item:
            revalue=self.search(item,dev+1,end)

        return revalue

li=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li+=[x for x in range(10000000)]
li.append(10000000)




print(li[100000001-1])
print(len(li))
s=Search(li)
#print(sorted([1,2,3,6,5,3,5,8,4,4]))
print(s.search(10000000,0,100000000))