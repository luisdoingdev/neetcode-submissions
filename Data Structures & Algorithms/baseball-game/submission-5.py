class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] 
        for opt in operations:
            match opt:
                case "+":
                    record.append(record[-2] + record[-1])
                case "C":
                    record.pop()
                case "D":
                    record.append(2 * record[-1])
                case _:
                    record.append(int(opt))

        return sum(record)


             