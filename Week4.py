#Take two numbers N and K as an input. Create a list L of length N and initialize it with zeros. 
Change the value to 1 of even indexes if k is even, otherwise change the value of odd indexes. Print list L in the end.(Consider 0 as even)#

N=int(input())
K=int(input())

L= []

if K%2!=0:
  for i in range(N):
    if i%2==0:
      L.append(0)
    else:
      L.append(1)

else:
  for i in range(N):
    if i%2!=0:
      L.append(0)
    else:
      L.append(1)

print(L, end="")

#Write a program to take string S as an input and replace all vowels by *. Also print the modified string.#

S=input()
v=list('aeiou')
a=""
for i in S:
  if  i.lower() in v:
    a=a+'*'
  else:
    a=a+i
print(a,end="")

#Write a program to take an integer N as an input and display the pattern#
