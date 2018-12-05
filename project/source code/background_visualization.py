import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
m = 60
objects = ('Google', 'Youtube', 'Facebook', 'Amazon', 'Wikipedia', 'Reddit')
y_pos = np.arange(len(objects))
performance = [7+(31/m),8+(38/m),9+(45/m),7+(48/m),4+(6/m),11+(28/m)]
plt.bar(y_pos, performance, color='b', align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Time (minutes)')
plt.title('Daily Time on Site')
plt.show()

plt.figure(2)
objects = ('Google', 'Youtube', 'Facebook', 'Amazon', 'Wikipedia', 'Reddit')
y_pos = np.arange(len(objects))
performance = [9.07,4.92,4.03,8.05,3.07,7.42]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('# of Pageviews')
plt.title('Daily Pageviews per Visitor')
plt.show()

plt.figure(3)
objects = ('Google', 'Youtube', 'Facebook', 'Amazon', 'Wikipedia', 'Reddit')
y_pos = np.arange(len(objects))
performance = [3.4, 12.8, 7.3, 23.1, 57.2, 17.8]
plt.bar(y_pos, performance, color = 'g', align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('% from Search')
plt.title('% of Traffic From Search')
plt.show()

plt.figure(4)
objects = ('Google', 'Youtube', 'Facebook', 'Amazon', 'Wikipedia', 'Reddit')
y_pos = np.arange(len(objects))
performance = [2765735, 2133008, 5669199, 626468, 1417597, 373841]
plt.bar(y_pos, performance, color = 'y', align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('# of sites')
plt.title('Total Sites Linking In')
plt.show()
