#! /usr/bin/python3.3
from copy import copy
import numpy

class Polynom(object):
    def __init__(self, m):
        self.m = m
        pass
    #realisation is the same as in polynomal base
    def const_zero(self):
        res=m*[0]
        return res

    def const_one(self):
        res=m*[1]
        return res

    def to_array(self, a_str):
        res = [int(z) for z in a_str]

        return res

    def to_string(self, arr):
         
        k=''.join([str(e) for e in arr])
        return k    

    def addition(self,first, second):
        add_result = []

        if len(first)>len(second):
            for i in range(0,len(first)-len(second),1):
                second.insert(0,0)

        if len(second)>len(first):
            for i in range(0, len(second)-len(first),1):
                first.insert(0,0)


        for i in range(0,len(first),1):
            if(first[i]==second[i]):
                add_result.insert(i,0)
            else:
                add_result.insert(i,1)


        return add_result


    def cycle_shift_right(self, a, n):        
        res=copy(a)
        for i in range(0,n,1):
            res.insert(0,res.pop())
        return res

    def cycle_shift_left(self, a, n):
        res=copy(a)
        for i in range(0,n,1):
            res.insert(len(a)-1,res.pop(0))
        return res

    def square(self, a):
        result=self.cycle_shift_right(a,1)
        return result

    def Trace(self, a):
        trace=a[0]
        for i in range(1,len(a)):
            if trace==a[i]:
                trace=0
            else:
                trace=1
        return trace

  
    def lambda_elements(self, i, j):
        m=self.m

        a= ((2**i)+(2**j)) % (2*m+1)
        b= ((2**i)-(2**j)) % (2*m+1)
        c= (-(2**i)+(2**j)) % (2*m+1)
        d= (-(2**i)-(2**j)) % (2*m+1)

        if (a==1 or b==1 or c==1 or d==1):
            return 1
        else: 
            return 0

    def set_lambda(self):
        m=self.m
        array = [[0 for x in range(m)] for x in range(m)]

        for i in range(0,m):
            for j in range(0,m):
                array[i][j] = self.lambda_elements(i, j)
        return array


    def multiplication(self, arr, brr):
        m=self.m 

        if len(arr)>len(brr):
            for i in range(0,len(arr)-len(brr),1):
                brr.insert(0,0)

        if len(brr)>len(arr):
            for i in range(0, len(brr)-len(arr),1):
                arr.insert(0,0)

        mul_res=[0]*m
        c = numpy.matrix(self.set_lambda())

        for i in range(0,m):
            temp_brr=self.cycle_shift_left(brr, i)
            temp_arr = numpy.matrix(self.cycle_shift_left(arr, i))
            temp_brr = numpy.matrix(temp_brr).reshape(len(temp_brr),1)
            mul_res[i] = int(temp_arr * c * temp_brr) % 2

        return mul_res


    def Ito(self, a):               #reversed element
        inv = list()
        m_1 = self.to_array((bin(self.m-1)[2:]))
        t = len(m_1) - 1

        b = copy(a)
        k = 1

        for i in range(t-1,-1,-1):
            b_pow_2_in_k1 = self.cycle_shift_right(b, k)

            k = 2*k
            b = self.multiplication(b_pow_2_in_k1, b)
            if m_1[-1 - i] == 1:
                q=self.square(b)
                b=self.multiplication(q, a)
                k+=1 

        inv=self.square(b)
        return inv
