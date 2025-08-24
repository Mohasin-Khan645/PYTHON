std = ['Ashad','mohasin','sheraj','irshad','bibek']
marks= [[100,100,100],[12,34,54],[50,30,20],[23,43,12],[43,23,13]]
per = []
for i in marks:
    a = float(sum(i)//3)
    per.append(a)
for i in range(5):
    print("{}.{} : {}%".format(i+1,std[i],per[i]))
