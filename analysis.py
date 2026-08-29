import pandas as pd
import matplotlib.pyplot as plt

#Read the file
df = pd.read_csv("customers_sales.csv.txt")

#Create total price column
df["total_price"] = df["price"] * df["quantity"]

#-------------------------------------
#Total sales
#-------------------------------------
total_sales = df["total_price"].sum()
print("Total Sales:")
print(total_sales)

#-------------------------------------
#Best customer
#-------------------------------------
customer_spending = df.groupby("customer")["total_price"].sum()
best_customer = customer_spending.idxmax()
print("\nBest Customer:")
print(best_customer)

#--------------------------------------
#Best City
#--------------------------------------
city_sales = df.groupby("city")["total_price"].sum()
best_city = city_sales.idxmax()
print("\nBest City:")
print(best_city)

#---------------------------------------
#Best selling product
#---------------------------------------
product_quantity = df.groupby("product")["quantity"].sum()
best_product = product_quantity.idxmax()
print("\nBest Selling Product:")
print(best_product)

#---------------------------------------
#Customers who spent more than 2000
#---------------------------------------
big_customers = customer_spending[customer_spending > 2000]
print("\nCustomers Spent > 2000:")
print(big_customers)

#------------------------------------------
#Average order value
#------------------------------------------
average_order = df["total_price"].mean()
print("\nAverage Order:")
print(average_order)

#------------------------------------------
#Bar Chart
#Sales by customer
#------------------------------------------
plt.figure()
plt.bar(customer_spending.index, customer_spending.values)
plt.title("Sales by Customer - Bar Chart")
plt.xlabel("Customer")
plt.ylabel("Total Spending")
plt.show()

#------------------------------------------
#Pie Chart
#Sales by City
#------------------------------------------
plt.figure()
plt.pie(city_sales.values, labels=city_sales.index, autopct="%1.1f%%")
plt.title("Sales by City - Pie Chart")
plt.show()

#------------------------------------------
#Line Chart
#Sales by transaction order
#------------------------------------------
plt.figure()
plt.plot(df.index, df["total_price"], marker="o")
plt.title("Sales per Transaction - Line Chart")
plt.xlabel("Transaction Order")
plt.ylabel("Total_price")
plt.show()

#-------------------------------------------
#Scatter Plot
#Price vs Quantity relationship
#-------------------------------------------
plt.figure()
plt.scatter(df["price"], df["quantity"])
plt.title("Price vs Quantity - Scatter Plot")
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.show()

#---------------------------------------------
#CSV report
#---------------------------------------------
report = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Best Customer",
        "Best City",
        "Best Product",
        "Average Order"
    ],
    "Value": [
        total_sales,
        best_customer,
        best_city,
        best_product,
        average_order
    ]
})
report.to_csv("customer_sales_report.csv", index=False)
print("\nReport saved successfully.")



