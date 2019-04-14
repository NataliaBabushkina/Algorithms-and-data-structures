# -*- coding: utf-8 -*-
#"""
#Бабушкина Н. В., 05-703, Возведение в степень
#"""
def FindPow(a,n):#рекурсивная функция, которая возводит а в степень n
    if n>=0:
        if n==0: return 1
        if n%2==0: return FindPow(a*a, n/2)#если степень четная, то 
        #сначала берем квадрат от а, потом возводим в степень n/2
        if n%2==1: return FindPow(a, n-1)*a
    else: 
        return 1/FindPow(a, -n)#если степень отрицательная    
    
print ("Введите основание степени:")
a=int(input())#ввод целого числа
print ("Введите показатель степени:")
n=int(input())
print("Ответ: ", FindPow(a, n))