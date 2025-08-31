# error handling using try and except

#without try except

# x = int(input('input an operator :')) 
# print(x)





# with  error try except
# try:
#     x = int(input('input an operator :'))
#     print(x)
# except:
#     print('something went wrong')



# try:
#     x = int(input('input an operator :'))
#     print(x)
# except ValueError:
#     print('value error')


try:
    x = int(input('input an operator :'))
    print(x)
except:
    print('something went erong')

finally:
    print('try except finished')

