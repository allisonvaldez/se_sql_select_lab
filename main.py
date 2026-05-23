# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("data.sqlite")

# 1. View data from the employee table
employee_data = pd.read_sql(""" SELECT * FROM employees """, conn)
print("\n\n--- Employee Data ---")
print(employee_data)

# 2. Assign the variable df_first_five to the employee number and last name
df_first_five = pd.read_sql(""" SELECT employeeNumber, lastName FROM employees""", conn)
print("\n\nResults of df_first_five:")
print(df_first_five)

# 3. Repeat Step 2, but have the last name come before the employee number
df_five_reverse = pd.read_sql(""" SELECT lastName, employeeNumber FROM employees """, conn )
print("\n\nResults of df_five_reverse:")
print(df_five_reverse)

# 4. Repeat step 3, but use an alias to rename the employee number column as 'ID' 
df_alias = pd.read_sql(""" SELECT lastName, employeeNumber AS ID FROM employees""", conn)
print("\n\nResults of df_alias:")
print(df_alias)

# 5. Use CASE to bin where the jobTitles of President, VP Sales, or VP Marketing have the 'role' of "Executive", and the rest of the employees are "Not Executive".
df_executive = pd.read_sql(""" SELECT *,
                           CASE
                            WHEN jobTitle = "President" OR jobTitle = "VP Sales" OR jobTitle = "VP Marketing"
                            THEN "Executive"
                            ELSE "Not Executive"
                           END AS role
                           FROM employees
                           """, conn)
print("\n\nResults of df_executive:")
print(df_executive)

# 6.Find the length of the last name for all employees, and return only this data as a new column called name_length
df_name_length = pd.read_sql(""" SELECT LENGTH(lastName) AS name_length FROM employees """, conn)
print("\n\nResults of df_name_length:")
print(df_name_length)

# 7. Return only one new column called short_title that has the first two letters of each person's job title.
df_short_title = pd.read_sql(""" SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees """, conn)
print("\n\nResults of df_short_title:")
print(df_short_title)

# 8. Bring in new table from another database and view it.
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("\n\n--- Order Details Data ---")
print(order_details)

# 9. Find the total amount for all orders, calculated as the sum of rounded total prices. The total price for each order is the priceEach multiplied by the quantityOrdered.
sum_total_price = None
print("\n\nResults of sum_total_price:")
print(sum_total_price)

# 9. Replace None with your code
df_day_month_year = None
print("\n\nResults of df_day_month_year:")
print(df_day_month_year)