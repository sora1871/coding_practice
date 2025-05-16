class Solution:
    def calPoints(self, operations: List[str]) -> int:
        point = []

        for i in range(len(operations)):
            if operations[i] == "C":
                point.pop()
                print(point)

            elif operations[i] == "D":
                point.append(point[-1]*2)
                print(point)

            elif operations[i] == "+":
                point.append(point[-1]+point[-2])
                print(point)

            else:
                point.append(int(operations[i]))
                print(point)            

        return sum(point)        
