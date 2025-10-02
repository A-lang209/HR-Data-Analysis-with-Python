import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


df = pd.read_csv('HR_Data_MNC_Data Science Lovers.csv')

df
df.info()

df.drop( 'Unnamed: 0', axis = 1, inplace = True)

df['Hire_Date'] = pd.to_datetime( df['Hire_Date'] )

df.head()
df.info()

df['Performance_Rating'].unique()
df['Performance_Rating'].value_counts()

df['Performance_Rating'].mean()

df['Experience_Years'].nunique()
df['Experience_Years'].unique()
sns.countplot( x = 'Experience_Years', data = df)
plt.show()

df['Experience_Years'].value_counts()

df.select_dtypes( include = 'object')
df.select_dtypes( include = 'number')

status = df['Status'].value_counts()
status
status.plot(kind = 'pie', colors = 'mygr', autopct = '%1.1f%%', explode = (0.03, 0.03, 0.03, 0.03))
plt.show()

work  = df['Work_Mode'].value_counts()
work
work.plot(kind = 'pie', colors = 'cr', autopct = '%1.1f%%', shadow = True)
plt.show()

df['Department'].value_counts()
sns.countplot( x = 'Department', data = df)
plt.show()

df['Job_Title'].value_counts()
plt.figure(figsize=(10,6))
sns.countplot( x = 'Job_Title', data = df )
plt.xticks( rotation = 'vertical')
plt.show()

dept = df.groupby('Department')['Salary_INR'].mean()/1000
dept
dept.plot(x = dept.index, y = dept.values, kind = 'bar', color = 'c', legend = True, width = 0.3)
plt.grid(True)
plt.title('Average Salary per Department')
plt.ylabel('Salary')
plt.show()

salary = df.groupby('Job_Title')['Salary_INR'].mean()/1000
salary
plt.figure(figsize=(10,6))
salary.plot(x = salary.index, y = salary.values, kind = 'bar', color = 'g')
plt.grid(True)
plt.title('Average Salary wrt Job Title')
plt.ylabel('Salary')
plt.show()

dept_job = df.groupby(['Department', 'Job_Title'])['Salary_INR'].mean()/1000
dept_job
#for coloring
import random
num_bars = len(dept_job)
random_colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(num_bars)]
#The graph
dept_job.plot(kind = 'barh', figsize=(10,5), color = random_colors)
plt.title('Average Salary in Different Departments')
plt.xlabel('Salary')
plt.show()

df.Status.unique()
df_Res = df[df['Status'] == 'Resigned']
df_Res
Res_dep = df_Res.groupby('Department')['Status'].count()
Res_dep
Res_dep.plot(x = Res_dep.index, y = Res_dep.values, kind = 'bar', color = 'black', legend = True, label = 'Resigned')
plt.title('Number of Employees Resigned')
plt.ylabel('Number of Employees')
plt.show()

df_Ter = df[df['Status'] == 'Terminated']
df_Ter
Ter_dep = df_Ter.groupby('Department')['Status'].count()
Ter_dep
Ter_dep.plot(x = Ter_dep.index, y = Ter_dep.values, kind = 'bar', color = 'orange', legend = True, label = 'Terminated')
plt.title('Number of Employees Terminated')
plt.ylabel('Number of Employees')
plt.show()

Res_dep.plot(x = Res_dep.index, y = Res_dep.values, kind = 'bar', color = 'black', legend = True, label = 'Resigned')
Ter_dep.plot(x = Ter_dep.index, y = Ter_dep.values, kind = 'bar', color = 'orange', legend = True, label = 'Terminated')
plt.legend(title = 'Employee Status')
plt.title('Number of Employees Resigned and Terminated')
plt.ylabel('Number of Employees')
plt.grid()
plt.show()

df['Experience_Years'].nunique()
df.groupby('Experience_Years')['Salary_INR'].mean()

PR = df.groupby('Department')['Performance_Rating'].mean()
PR.plot(x = PR.index, y = PR.values, kind = 'bar', color = 'lightgreen')
plt.title('Average Performance Rating per Department')
plt.ylabel('Rating')
plt.show()

# Create column that contain only the country, handling non-string values and missing commas
df['Country'] = df['Location'].apply(lambda x: str(x).split(',')[1].strip() if isinstance(x, str) and ',' in str(x) else None)
df.head()
df.Country.nunique()
df.Country.value_counts()

#correlation between two numerical columns
#df['Performance_Rating'].corr(df['Salary_INR'])
df[['Performance_Rating', 'Salary_INR']].corr()
sns.heatmap(df.corr(numeric_only=True));
plt.show()

df.head()
df.Year.unique()
df.Year.nunique()

hire_rate = df.groupby('Year')['Employee_ID'].count()
hire_rate
plt.figure(figsize=(10,4))
hire_rate.plot(x = hire_rate.index, y = hire_rate.values, kind = 'bar', color = 'violet')
plt.grid(color = 'w')
plt.title("No. of Employees Hired in any Year")
plt.ylabel("Count")
plt.show()

df.groupby('Work_Mode')['Salary_INR'].mean()
top_10 = df.groupby('Department').apply(lambda x: x.nlargest(10, 'Salary_INR'))
top_10.head(40)
top_10.tail(30)

dept_counts = df.groupby('Department')['Status'].agg(total_emp = 'count', resigned = lambda x: (x == 'Resigned').sum())
dept_counts
# Calculate attrition rate
dept_counts['attrition_rate_%'] = (dept_counts['resigned'] / dept_counts['total_emp']) * 100
dept_counts
# Sort by attrition rate (highest first)
dept_counts.sort_values("attrition_rate_%", ascending = False)
