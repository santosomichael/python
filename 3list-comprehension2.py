lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [ii+i+j+jj for j in digits for jj in digits for ii in lowercase for i in lowercase]

print(answer)