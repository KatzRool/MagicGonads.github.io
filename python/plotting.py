import matplotlib.pyplot as plt
def plot(exp='x',start=0,end=200,scale=1):
    func = lambda x: eval(exp)
    plt.plot([x*scale for x in range(start,end+1)],[func(x*scale) for x in range(start,end+1)])
    plt.show()
