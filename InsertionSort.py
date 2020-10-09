class ilist(list):

    def __init__(self,li):
        super().__init__(li)

    def sort(self, *, key = None, reverse: bool = None) -> None:

        if key is None:
            key=lambda x:x

        for i in range(1,len(self)):
            #inner=i
            subject=self[i]
            decosubject=key(subject)
            while i>0 and decosubject<key(self[i-1]):
                self[i]=self[i-1]
                i-=1
            self[i]=subject

if __name__=='__main__':
    f=ilist(['peach','straw','spork','apple0','apple'])
    print(f)
    f.sort(key=lambda x:x[0])
    print(f)