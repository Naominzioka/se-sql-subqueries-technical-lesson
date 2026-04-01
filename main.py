import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

#step 1 - query to find employees from USA
# q = pd.read_sql("""
#                 SELECT firstName, lastName, officeCode
#                 FROM employees
#                 JOIN offices
#                 USING(officeCode)
#                 WHERE country = 'USA';
#                 """, conn)
# print(q)

#step 2 -using a subquery for step 1
#write the smaller query first(nested query/ subquery)
# subq = pd.read_sql("""
#                 SELECT officeCode 
#                 FROM offices
#                 WHERE country = 'USA';
#                 """)
# main_q = pd.read_sql("""
#                      SELECT firstName, lastName, officeCode
#                      FROM employees
#                      WHERE officeCode IN ( SELECT officeCode
#                             FROM offices
#                             WHERE country = 'USA');
#                                 """, conn)
# print(main_q)

# """step 3 finding employees from offices with atleast 5 employees
# GROUP by 1 in this case means group by officeCode which is the first column in the select statement
# -its the same as writing GROUP BY officeCode"""
# q = pd.read_sql("""
#                 SELECT lastName, firstName, officeCode
#                 FROM employees
#                 WHERE officeCode IN (
#                     SELECT officeCode
#                     FROM offices
#                     JOIN employees
#                     USING(officeCode)
#                     GROUP BY 1
#                     HAVING COUNT(employeeNumber) >= 5
#                 );
#                 """, conn)
# print(q)

#step 4 chaining aggregates to find the average payment per customer and then the average of those averages
# q = pd.read_sql(""" 
#                 SELECT AVG(customerAvgPayment) AS averagePayment
#                     FROM (
#                         SELECT AVG(amount) AS customerAvgPayment
#                         FROM payments
#                         JOIN customers
#                             USING(customerNumber)
#                         GROUP BY customerNumber
#                     )
#                 """, conn)
# print(q)

#step 5 - foreign key reference to find customers from USA and the employee who represents them in the USA
#we can use the employee number in employees table and the matching sales rep employee number in customers table.
#using subquery
q = pd.read_sql("""
                SELECT lastName, firstName, employeeNumber
                FROM employees
                WHERE employeeNumber IN (
                    SELECT salesRepEmployeeNumber
                    FROM customers
                    WHERE country = 'USA');
                """, conn)
print(q)

conn.close()
