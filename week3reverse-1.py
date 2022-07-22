def reverse(list):
    if not list:
        return []
    else:
        return list[-1:] + reverse(list[:-1])
    
    
  
print(reverse([1, 3, 5, 7, 9, 11]))