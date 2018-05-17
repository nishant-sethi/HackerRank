# Enter your code here. Read input from STDIN. Print output to STDOUT
x=c(15 , 12,  8,   8,   7,   7,   7,   6,   5,  3)
y=c(10,  25,  17,  11,  13,  17,  20,  13,  9,   15)
model=lm(y~x)
result=predict(model,data.frame(x=10))
cat(round(result,1))