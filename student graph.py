import matplotlib.pyplot as plt

# Defining my  lists
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
boys_marks = [70, 75, 80, 85, 90, 95]
girls_marks = [65, 70, 78, 82, 88, 92]
 

# Create the plot for each list
plt.plot(months, boys_marks, label='Boys Marks', marker='o', linestyle='-')
plt.plot(months, girls_marks, label='Girls Marks', marker='x', linestyle='--')
plt.plot(months, boys_marks, label="boys marks")

plt.xlabel('Months')
plt.ylabel('Marks')
plt.title('Student Marks Over Months')
plt.legend()

# Display the graph
plt.grid(True) 
plt.show()