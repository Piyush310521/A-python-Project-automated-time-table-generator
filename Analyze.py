import numpy as np 
import matplotlib.pyplot as plt
import seaborn as se
Customers = ['Tata Motors','Toyota','Suzuki','Hyundai']
Sales = [10,20,3,30]
 
Customer = np.array(Customers)
Sale = np.array(Sales)

print(Customer)
print(Sales)

se.lineplot(x = Customer,y=Sales)
plt.xlabel('Brands')
plt.ylabel('Sale')
plt.show()












