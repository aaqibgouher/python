i=0
while i<5:
    print(i)
    i+=1

i=0
while i<5:
    print(i)
    i+=1
else:
    print("while loop end")

print("end again")

# range(n) -> n is the total no of loop
# it starts from 0 to 4
for i in range(5):
    print(i)

# range(start, end) -> start is included, end is not included
for i in range(10, 15):
    print(i)

# range(start, end, incr) -> incr is increment value, by default is 1
for i in range(0, 10, 2):
    print(i)