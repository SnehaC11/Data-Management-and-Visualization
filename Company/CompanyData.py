import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_dataset.csv")
# print(df.head())

#Pie chart
employee_count = df['employees'].value_counts()
plt.figure()
plt.pie(employee_count, labels=employee_count.index, autopct='%1.1f%%')

plt.title('Company Employee Distribution')
plt.show()

#Headquarter names
random_10 = df[['name', 'hq']].drop_duplicates().sample(n=10, random_state=42)
print(random_10)

#bar chart
data = df[['name', 'ratings']].drop_duplicates()
plt.figure(figsize=(10,6))
plt.bar(data['name'], data['ratings'])
plt.xlabel('Company Name')
plt.ylabel('rating')
plt.title('Company Rating Distribution')
plt.xticks(rotation=45)
plt.show()

#line chart
data = df[['name', 'years']].drop_duplicates()
data = data.sort_values('years')
plt.figure()
plt.plot(data['name'], data['years'], marker ='o')
plt.xlabel('Company Name')
plt.ylabel('years')
plt.title('Company-Year Distribution')
plt.xticks(rotation=45)
plt.show()

#funnel chart
df_sorted = df.sort_values(by='review_count', ascending=False)

plt.figure(figsize=(10,8))
plt.barh(df_sorted['name'], df_sorted['review_count'])
plt.title("Funnel Chart: Companies Review Wise")
plt.xlabel("Reviews")
plt.ylabel("Company")
plt.tight_layout()
plt.show()
