import matplotlib.pyplot as pyt
pyt.style.use('fivethirtyeight')
l1 = [3,7,69,6,5,67,4,6,7,8,9,99,9,8,5]
l2 = [6,6,6,8,90,9999,76,6,6,6,6,8,99,4,5]

pyt.plot(l1,l2,'k--.')
l3 = [47,7,8,8,85,3,47,8,8,8,8,93,4,1,0]

pyt.plot(l3,l2, color='#4facfe', linestyle='--',marker='.', linewidth=3)

pyt.title('my first graph')
pyt.xlabel('first')
pyt.ylabel('second')
pyt.legend('djdj','jdidi')
#pyt.grid(True)
pyt.savefig('graph.png')
pyt.show()