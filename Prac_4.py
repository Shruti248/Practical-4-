from collections import Counter 
if __name__ == '_main_': 
  n = int(input()) 
  arr = list(set(map(int, input().split()))) 
  arr.sort() 
  print (arr[-2])
