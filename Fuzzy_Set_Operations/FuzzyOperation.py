import numpy as np

class SetOperations:

    def __init__(self):
        self.set = []
        return

    def union(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            if array_a[i] > array_b[i]:
                self.set.append(array_a[i])
            else:
                self.set.append(array_b[i])

        return self.set

    def intersection(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            if array_a[i] < array_b[i]:
                self.set.append(array_a[i])
            else:
                self.set.append(array_b[i])

        return self.set

    def compliment(self, array_a):
        self.__init__()

        for i in range(len(array_a)):
            self.set.append(1 - array_a[i])

        return self.set

    def product(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            self.set.append(array_a[i] * array_b[i])

        return self.set

    def bounded_product(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            self.set.append( max(0, ( array_a[i] + array_b[i] - 1 )) )

        return self.set

    def addition(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            self.set.append( ( array_a[i] + array_b[i] ) - ( array_a[i] * array_b[i] ) )

        return self.set

    def subtraction(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            self.set.append( min(array_a[i], ( 1 - array_b[i] )) )

        return self.set

    def disjunctiveSum(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            temp1 = min(( 1 - array_a[i] ), array_b[i])
            temp2 = min(array_a[i], ( 1 - array_b[i] ))
            self.set.append( max(temp1, temp2) )

        return self.set

    def boundedSum(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            self.set.append( min( 1, ( array_a[i] + array_b[i] ) ) )

        return self.set

    def boundedDifference(self, array_a, array_b):
        self.__init__()

        for i in range(len(array_a)):
            self.set.append( max( 0, ( array_a[i] + array_b[i] - 1 ) ) )

        return self.set

    def equality(self, array_a, array_b):
        self.__init__()

        flag = False

        for i in range(len(array_a)):
            if not array_a[i] == array_b[i]:
                flag = False

        self.set.append(flag)
        return self.set

    def power(self, array_a, alpha):
        self.__init__()

        for i in range(len(array_a)):
            self.set.append( array_a[i] ** alpha )

        return self.set

    def cartesianProduct(self, array_a, array_b):
        self.__init__()

        for j in range(len(array_b)):
            for i in range(len(array_a)):
                self.set.append( min(array_a[i], array_b[j]) )

        self.set = np.matrix(self.set)
        self.set = self.set.reshape(len(array_b), len(array_a))
        
        return self.set