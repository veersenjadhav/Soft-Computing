from FuzzyOperation import *
import pandas as pd
import sys

class Operations:
    def __init__(self):
        self.dataset = pd.read_csv('dataMain.csv')
        self.x1 = self.dataset.iloc[:, 1].values
        self.x2 = self.dataset.iloc[:, 3].values

        self.so = SetOperations()
        return 

    def menu(self):
        while True:
            
            choice = int(input('\n 1 --> Union \n 2 --> Intersection \n 3 --> Compliment \n 4 --> Product \n 5 --> Bounded Product \n 6 --> Addition \n 7 --> Subtraction \n 8 --> Disjunctive Sum \n 9 --> Bounded Sum \n 10 --> Bounded Difference \n 11 --> Equality \n 12 --> Power \n 13 --> Cartesian Product \n 14 --> Exit \n Enter Your Choice : '))

            if choice == 1:
                ans = self.so.union(self.x1, self.x2)
                print('Union of two sets : ',ans)
            elif choice == 2:
                ans = self.so.intersection(self.x1, self.x2)
                print('Intersection of two sets : ',ans)
            elif choice == 3:
                ans = self.so.compliment(self.x1)
                print('Compliment of first set : ',ans)
            elif choice == 4:
                ans = self.so.product(self.x1, self.x2)
                print('Product of two sets : ',ans)
            elif choice == 5:
                ans = self.so.bounded_product(self.x1, self.x2)
                print('Bounded Product of two sets : ',ans)
            elif choice == 6:
                ans = self.so.addition(self.x1, self.x2)
                print('Addition of two sets : ',ans)
            elif choice == 7:
                ans = self.so.subtraction(self.x1, self.x2)
                print('Subtraction of two sets : ',ans)
            elif choice == 8:
                ans = self.so.disjunctiveSum(self.x1, self.x2)
                print('Disjunctive Sum of two sets : ',ans)
            elif choice == 9:
                ans = self.so.boundedSum(self.x1, self.x2)
                print('Bounded Sum of two sets : ',ans)
            elif choice == 10:
                ans = self.so.boundedDifference(self.x1, self.x2)
                print('Bounded Difference of two sets : ',ans)
            elif choice == 11:
                ans = self.so.equality(self.x1, self.x2)
                print('Equality of two sets : ',ans)
            elif choice == 12:
                ans = self.so.power(self.x1, float(input('Enter value of Alpha : ')))
                print('Power of first set : ',ans)
            elif choice == 13:
                ans = self.so.cartesianProduct(self.x1, self.x2)
                print('Cartesian Product of two sets : ',ans)
            elif choice == 14:
                sys.exit()

if __name__ == "__main__":
    op = Operations()
    op.menu()