'''
Created on Apr 3, 2016

@author: bliu
'''

'''
Gets the runs for an input.  A run is a list of increasing numbers.
'''
def runs(alist):
    runs = []
    prev = None
    curRun = None
    for element in alist:
        if (prev == None or element < prev):
            if (curRun != None):
                runs.append(curRun)
            curRun = [element]
        else:
            curRun.append(element)
        prev = element
    runs.append(curRun)
    return runs
    
if __name__ == '__main__':
    print(runs([1, 2, 3, 2, 1, 3, 4, 5]))
    