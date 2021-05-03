class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        self.stack.pop(0)

    def add(self, item):
        self.stack.append(item)
    
    def compare(self, item):
        return True if item <= self.stack[len(self.stack) -1] else False

    def is_empty(self):
        return True if self.stack == [] else False
  
        
def everybody_working(wookies, loads, count = 0):
    if count >= len(wookies) or loads == []:
        return wookies, loads
    if wookies[count].is_empty():
        wookies[count].add(loads.pop(0))
    return everybody_working(wookies, loads, count + 1)
    
   
def unloading(wookies, loads, rest, aux = 0):
    if loads == []:
        return wookies, rest
    for wookie in wookies:
        if wookie.compare(loads[0]):
            wookie.add(loads.pop(0))
            aux += 1
            break
    if aux == 0:
        rest.add(loads.pop(0))
    return unloading(wookies, loads, rest)
    


wookies = [Stack() for i in range(int(input()))]
loads, rest = [int(item) for item in input().split()], Stack()

if wookies == []:
    print("Os Wookies foram para o lado sombrio da força!")
    [print(item, end=" ") for item in loads]
else:
    workers, new_load = everybody_working(wookies, loads)
    after_job, rest_updated = unloading(workers, new_load, rest)
 
    printer = [laborer.stack for laborer in after_job]
    printer.sort(key= sum,reverse=True)
    [print(item, end=" ") for item in printer]
    if rest_updated.stack == []:
        print('\nA força está com os Wookies!')
    else:
        print()
        [print(item, end=" ") for item in rest_updated.stack]
        print()
