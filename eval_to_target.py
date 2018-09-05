class Evaluator:

    def __init__(self):
        self.results = []

    def eval_to_target(self, num, target, idx):
        if (idx == 0):
            if (len(num) == 1 and int(num) == target):
                self.results.append(num)
        print(num)
        print( "".join(set(num)) != "0")
        print(str(eval(num) == target))
        print("\n===\n")
        if (eval(num) == target and "".join(set(num)) != "0"):
            self.results.append(num)
        elif (idx >= len(num)):
            return
        else:
            if (idx != 0):                
                self.eval_to_target(num[0:idx] + "+" + num[idx:], target, idx+2)
                self.eval_to_target(num[0:idx] + "-" + num[idx:], target, idx+2)
                self.eval_to_target(num[0:idx] + "*" + num[idx:], target, idx+2)
            self.eval_to_target(num, target, idx+1)
                

    def get_results(self):
        return self.results


e = Evaluator()
e.eval_to_target("00", 0, 0)
print(e.get_results())
