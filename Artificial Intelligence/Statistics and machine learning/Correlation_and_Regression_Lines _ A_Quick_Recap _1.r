# Enter your code here. Read input from STDIN. Print output to STDOUT
p<-c(15,12,8,8,7,7,7,6,5,3)
h<-c(10,25,17,11,13,17,20,13,9,15)
ans<-cor(p,h)
ans<-round(ans,3)
cat(ans)