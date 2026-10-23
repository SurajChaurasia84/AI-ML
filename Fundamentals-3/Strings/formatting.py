a=5
b=10
sum=a+b

#normal formatting
print("language is {}".format("pyhton"))
print("sum of {} and {} is {}".format(a,b,sum))

#index based formatting
print("sum of {1} and {0} is {2}".format(a,b,sum))

#value based formatting
print("sum of {p} and {q} is {sum2}".format(p=10, q=15, sum2=25))