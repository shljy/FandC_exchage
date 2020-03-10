
#20200310
# output the average of several numbers

N=10
count=1
sum=0
while(count<N):
    cn=float(input('input a number:'))
    sum+=cn
    ave=sum/count
    count=count+1
    print('the curent count:{}\n,average:{}'.format(count-1,ave))
    
