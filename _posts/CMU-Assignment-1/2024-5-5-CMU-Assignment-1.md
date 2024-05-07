---
title: CMU Assignment 1
date: 2024-5-5 16:15:14 -19800
tags: [CMU, DB]
description: Assignemnt 1 on basic and advanced Database queries
---

### Setup

The websites instructions are very clear and easy to follow. I just had to spin up WSL and setup `sqlite3` and I was ready to go.

### Tables

```Text
Category              EmployeeTerritory     Region
Customer              Order                 Shipper
CustomerCustomerDemo  OrderDetail           Supplier
CustomerDemographic   Product               Territory
Employee              ProductDetails_V
```

### Checking the schema

1. Category

```SQL
CREATE TABLE IF NOT EXISTS "Category"
(
  "Id" INTEGER PRIMARY KEY,
  "CategoryName" VARCHAR(8000) NULL,
  "Description" VARCHAR(8000) NULL
);
```

2. Category

```SQL
CREATE TABLE IF NOT EXISTS "Category"
(
  "Id" INTEGER PRIMARY KEY,
  "CategoryName" VARCHAR(8000) NULL,
  "Description" VARCHAR(8000) NULL
);
```

3. CustomerCustomerDemo

```SQL
CREATE TABLE IF NOT EXISTS "CustomerCustomerDemo" 
(
  "Id" VARCHAR(8000) PRIMARY KEY, 
  "CustomerTypeId" VARCHAR(8000) NULL 
);
```

4. CustomerDemographic

```SQL
CREATE TABLE IF NOT EXISTS "CustomerDemographic"
(
  "Id" VARCHAR(8000) PRIMARY KEY,
  "CustomerDesc" VARCHAR(8000) NULL
);
```

5. Employee

```SQL
CREATE TABLE IF NOT EXISTS "Employee"
(
  "Id" INTEGER PRIMARY KEY,
  "LastName" VARCHAR(8000) NULL,
  "FirstName" VARCHAR(8000) NULL,
  "Title" VARCHAR(8000) NULL,
  "TitleOfCourtesy" VARCHAR(8000) NULL,
  "BirthDate" VARCHAR(8000) NULL,
  "HireDate" VARCHAR(8000) NULL,
  "Address" VARCHAR(8000) NULL,
  "City" VARCHAR(8000) NULL,
  "Region" VARCHAR(8000) NULL,
  "PostalCode" VARCHAR(8000) NULL,
  "Country" VARCHAR(8000) NULL,
  "HomePhone" VARCHAR(8000) NULL,
  "Extension" VARCHAR(8000) NULL,
  "Photo" BLOB NULL,
  "Notes" VARCHAR(8000) NULL,
  "ReportsTo" INTEGER NULL,
  "PhotoPath" VARCHAR(8000) NULL
);
```

6. EmployeeTerritory

```SQL
CREATE TABLE IF NOT EXISTS "EmployeeTerritory"
(
  "Id" VARCHAR(8000) PRIMARY KEY,
  "EmployeeId" INTEGER NOT NULL,
  "TerritoryId" VARCHAR(8000) NULL
);
```

7. Order

```SQL
CREATE TABLE IF NOT EXISTS "Order"
(
  "Id" INTEGER PRIMARY KEY,
  "CustomerId" VARCHAR(8000) NULL,
  "EmployeeId" INTEGER NOT NULL,
  "OrderDate" VARCHAR(8000) NULL,
  "RequiredDate" VARCHAR(8000) NULL,
  "ShippedDate" VARCHAR(8000) NULL,
  "ShipVia" INTEGER NULL,
  "Freight" DECIMAL NOT NULL,
  "ShipName" VARCHAR(8000) NULL,
  "ShipAddress" VARCHAR(8000) NULL,
  "ShipCity" VARCHAR(8000) NULL,
  "ShipRegion" VARCHAR(8000) NULL,
  "ShipPostalCode" VARCHAR(8000) NULL,
  "ShipCountry" VARCHAR(8000) NULL
);
```

8. OrderDetail

```SQL
CREATE TABLE IF NOT EXISTS "OrderDetail" 
(
  "Id" VARCHAR(8000) PRIMARY KEY, 
  "OrderId" INTEGER NOT NULL, 
  "ProductId" INTEGER NOT NULL, 
  "UnitPrice" DECIMAL NOT NULL, 
  "Quantity" INTEGER NOT NULL, 
  "Discount" DOUBLE NOT NULL 
);
```

9. Product

```SQL
CREATE TABLE IF NOT EXISTS "Product" 
(
  "Id" INTEGER PRIMARY KEY, 
  "ProductName" VARCHAR(8000) NULL, 
  "SupplierId" INTEGER NOT NULL, 
  "CategoryId" INTEGER NOT NULL, 
  "QuantityPerUnit" VARCHAR(8000) NULL,
  "UnitPrice" DECIMAL NOT NULL,
  "UnitsInStock" INTEGER NOT NULL,
  "UnitsOnOrder" INTEGER NOT NULL,
  "ReorderLevel" INTEGER NOT NULL,
  "Discontinued" INTEGER NOT NULL
);
```

10. ProductDetails_V

```SQL
CREATE VIEW [ProductDetails_V] as
select
p.*,
c.CategoryName, c.Description as [CategoryDescription],
s.CompanyName as [SupplierName], s.Region as [SupplierRegion]
from [Product] p
join [Category] c on p.CategoryId = c.id
join [Supplier] s on s.id = p.SupplierId
/* ProductDetails_V(Id,ProductName,SupplierId,CategoryId,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued,CategoryName,CategoryDescription,SupplierName,SupplierRegion) */;
```

11. Region

```SQL
CREATE TABLE IF NOT EXISTS "Region"
(
  "Id" INTEGER PRIMARY KEY,
  "RegionDescription" VARCHAR(8000) NULL
);
```

12. Shipper

```SQL
CREATE TABLE IF NOT EXISTS "Shipper"
(
  "Id" INTEGER PRIMARY KEY,
  "CompanyName" VARCHAR(8000) NULL,
  "Phone" VARCHAR(8000) NULL
);
```

13. Supplier

```SQL
CREATE TABLE IF NOT EXISTS "Supplier"
(
  "Id" INTEGER PRIMARY KEY,
  "CompanyName" VARCHAR(8000) NULL,
  "ContactName" VARCHAR(8000) NULL,
  "ContactTitle" VARCHAR(8000) NULL,
  "Address" VARCHAR(8000) NULL,
  "City" VARCHAR(8000) NULL,
  "Region" VARCHAR(8000) NULL,
  "PostalCode" VARCHAR(8000) NULL,
  "Country" VARCHAR(8000) NULL,
  "Phone" VARCHAR(8000) NULL,
  "Fax" VARCHAR(8000) NULL,
  "HomePage" VARCHAR(8000) NULL
);
```

14. Territory

```SQL
CREATE TABLE IF NOT EXISTS "Territory"
(
  "Id" VARCHAR(8000) PRIMARY KEY,
  "TerritoryDescription" VARCHAR(8000) NULL,
  "RegionId" INTEGER NOT NULL
);
```

### Sanity Check

> Count the number of rows in the Order table
  
  ```SQL
  SELECT COUNT(*) FROM 'Order';
  ```

  ```Text
  16818
  ```

That is a lot of tuples.

### Database Schema

> ![Database Schema](https://15445.courses.cs.cmu.edu/fall2021/files/schema2021.png)
> Source CMU [src](https://15445.courses.cs.cmu.edu/fall2021/homework1/)

### Assignment Starts

> Q1. List all Category Names ordered alphabetically

```SQL
SELECT CategoryName from Category ORDER BY CategoryName;
```

```Text
Beverages
Condiments
Confections
Dairy Products
Grains/Cereals
Meat/Poultry
Produce
Seafood
```

---
> Q2. Get all unique ShipNames from the Order table that contain a hyphen '-'.
Details: In addition, get all the characters preceding the (first) hyphen. Return ship names alphabetically.

Let's see how many tuples do we have that have ShipNames containing hyphen

```SQL
SELECT COUNT(*) FROM 'Order' WHERE ShipName LIKE '%-%'
```

Running this gave me 1731. I'm sure there are duplicated. Let's remove the duplicates and count the number of distinct ShipNames having hyphen in their name. Okay cool, we are down to only 9 ShipNames.

After digging around, I found `instr()` and `substr()` functions. Now the question is fairly easy.

```SQL
SELECT DISTINCT ShipName, SUBSTR(ShipName, 0, INSTR(ShipName, '-')) 
FROM 'Order' 
WHERE ShipName LIKE '%-%' 
ORDER BY ShipName;
```

```Text
Bottom-Dollar Markets|Bottom
Chop-suey Chinese|Chop
GROSELLA-Restaurante|GROSELLA
HILARION-Abastos|HILARION
Hungry Owl All-Night Grocers|Hungry Owl All
LILA-Supermercado|LILA
LINO-Delicateses|LINO
QUICK-Stop|QUICK
Save-a-lot Markets|Save
```

The result checks out with the hint given in the question.

---
> Q3. Indicate if an order's ShipCountry is in North America. For our purposes, this is 'USA', 'Mexico', 'Canada'
Details: You should print the Order Id, ShipCountry, and another column that is either 'NorthAmerica' or 'OtherPlace' depending on the Ship Country.
Order by the primary key (Id) ascending and return 20 rows starting from Order Id 15445

Select out 20 rows ordered by primary key starting from id 15445. To do this, first I selected out 20 rows ordered by id.

```SQL
SELECT * from 'Order' ORDER BY Id LIMIT 20;
```

Now, we have to offset our results such that it starts from id 15445. Let's find the row value of tuple with id 15445 and offset our query by the row number. I used nesting queries to count the number of tuples that are less than id 15445. Then the result is used to offset my range so now We can see the first 20 queries ordered by id starting from id 15445.

```SQL
SELECT * from 'Order' ORDER BY Id LIMIT 20 OFFSET (SELECT COUNT(Id) FROM 'Order' WHERE Id < 15445);
```

Now, We have to extract only the required data. For conditional output, I used CASES and here's the solution for the question.

```SQL
SELECT Id, ShipCountry, 
    (CASE WHEN ShipCountry IN ('USA', 'Mexico', 'Canada') THEN 'NorthAmerica' ELSE 'OtherPlace' END) 
FROM 'Order' 
ORDER BY Id 
LIMIT 20 OFFSET (SELECT COUNT(Id) FROM 'Order' WHERE Id < 15445);
```

```Text
15445|France|OtherPlace
15446|Italy|OtherPlace
15447|Portugal|OtherPlace
15448|Argentina|OtherPlace
15449|Portugal|OtherPlace
15450|Venezuela|OtherPlace
15451|Brazil|OtherPlace
15452|France|OtherPlace
15453|France|OtherPlace
15454|Canada|NorthAmerica
15455|USA|NorthAmerica
15456|France|OtherPlace
15457|Mexico|NorthAmerica
15458|USA|NorthAmerica
15459|Germany|OtherPlace
15460|Argentina|OtherPlace
15461|Austria|OtherPlace
15462|Austria|OtherPlace
15463|Finland|OtherPlace
15464|Brazil|OtherPlace
```

---
> Q4. For each Shipper, find the percentage of orders which are late.
Details: An order is considered late if ShippedDate > RequiredDate. Print the following format, order by descending precentage, rounded to the nearest hundredths, like `United Package|23.44`

First Let's group each Shipper by ShipVia field. So we have roughly 5500 tuples. Now we have to Compare the ShippedDate and RequiredDate. Well I got side tracked and finished the question. It took a lot more tries though. And every query felt like. Ohh this should be the answer and then the very next second Ohh no that's impossible. There must be many better solutions but hey, I get the result. We can always optimize later.

```SQL
SELECT Shipper.CompanyName, 
       printf("%.2f", CAST(COUNT(*) * 100 AS FLOAT) / 
       (SELECT COUNT(*) FROM 'Order' AS InnerOrder WHERE InnerOrder.ShipVia = OuterOrder.ShipVia)) AS percentDelay 
FROM 'Order' AS OuterOrder, 
     Shipper 
WHERE ShippedDate > RequiredDate 
  AND OuterOrder.ShipVia = Shipper.Id 
GROUP BY ShipVia 
ORDER BY percentDelay DESC;
```

```Text
Federal Shipping|23.61
Speedy Express|23.46
United Package|23.44
```

---
> Q5. Compute some statistics about categories of products
Details: Get the number of products, average unit price (rounded to 2 decimal places), minimum unit price, maximum unit price, and total units on order for categories containing greater than 10 products. Order by Category Id.

This is slightly overwhelming, we are required to calculate a lot of statistics. Let's go through them one by one. For each category, we have to find categories having > 10 products and then perform statistics on them. Let's first print out all categories and their corresponding product count.

Well it turned out better than the previous one. Just had to remember Where to use `WHERE` and `HAVING` and we are good to go.

```SQL
SELECT 
    Category.CategoryName, 
    COUNT(*), 
    printf("%.2f", AVG(P.UnitPrice)), 
    MIN(P.UnitPrice), 
    MAX(P.UnitPrice), 
    SUM(P.UnitsOnOrder) 
FROM 
    'Product' AS P 
INNER JOIN 
    Category ON Category.Id = P.CategoryId 
GROUP BY 
    Category.Id 
HAVING 
    COUNT(*) > 10 
ORDER BY 
    Category.Id;
```

```Text
Beverages|12|37.98|4.5|263.5|60
Condiments|12|23.06|10|43.9|170
Confections|13|25.16|9.2|81|180
Seafood|12|20.68|6|62.5|120
```

---

#### Exposé

We are halfway through the assignment and I think it's better to check our results first. Let me first download the answers into my directory and copy my solutions to the placeholder directory. Then I can run both commands and compare the results.

```bash
diff <(echo $(sqlite3 northwind-cmudb2021.db "$(cat ./my_sol/question.sql)")) <(echo $(sqlite3 northwind-cmudb2021.db "$(cat ./sol/question.sql)")) && echo "All Good"
```

This will do the job. Now I have to give the file names to it one by one. I would have automated this as well but that will be slower than writing filenames manually.

> Q1. All Good [0]
> Q2. All Good [5]
> Q3. All Good [5]
> Q4. All Good [10]
> Q5. All Good [10]

Cool, we are on the right track and if my tally is correct, I'm standing at 30 points. Which, honestly, is slightly discouraging to me.😅

Anyways, Let's continue answering.

---
> Q6. For each of the 8 discontinued products in the database, which customer made the first ever order for the product? Output the customer's CompanyName and ContactName
Details: Print the following format, order by ProductName alphabetically.

I tried a few options but I couldn't get the hang of it for a few minutes. I'm going to try a little bit more. Let's break it down, Can I count the number of orders for each discontinued Product?

```SQL
select count(*) from OrderDetail as OD inner join Product as P on P.Id = OD.ProductId where P.Discontinued = 1;
```

This gave me a nice small number of 64598. Let's find the number of orders for each product. 

```SQL
select P.Id, P.ProductName, count(*) from OrderDetail as OD inner join Product as P on P.Id = OD.ProductId where P.Discontinued = 1 group by P.Id;
```

Seems to be the right direction tbh. I also thought of another way to do the above query and I feel better about this. 

```SQL
select DP.Id, DP.ProductName, count(1) from OrderDetail as OD join (select Id, ProductName from Product where Discontinued = 1) as DP on OD.ProductId = DP.Id group by DP.Id;
```

Basically, I nested a query to create a temp table and join that into the first table. I think with one more level of inception, we can achieve our answer.

After some painstaking 20 minutes, I have come up with this, 

```SQL
Select O.Id as DiscOrderId from 'Order' as O join (Select MIN(O.OrderDate) as OrderDate from 'Order' as O join (select OrderId, ProductId from OrderDetail join Product on Product.Id = OrderDetail.ProductId where Product.Discontinued = 1) as DP on O.Id = DP.OrderId  group by DP.ProductId) as ODates on O.OrderDate = ODates.OrderDate;
```

It returns all the OrderIds where the Discontinued products were ordered for the first time. Now I just have to join this table to the Customer table to fetch the required answer. But first let me modify a little bit more so I am displaying the ProductName as well.
Done. Here's the code,

```SQL
SELECT 
    O.Id AS DiscOrderId, 
    ODates.ProductName 
FROM 
    'Order' AS O
JOIN (
    SELECT 
        MIN(O.OrderDate) AS OrderDate, 
        DP.ProductName
    FROM 
        'Order' AS O
    JOIN (
        SELECT 
            OrderId, 
            ProductId, 
            P.ProductName
        FROM 
            OrderDetail
        JOIN 
            Product AS P ON P.Id = OrderDetail.ProductId
        WHERE 
            P.Discontinued = 1
    ) AS DP ON O.Id = DP.OrderId
    GROUP BY 
        DP.ProductId
) AS ODates ON O.OrderDate = ODates.OrderDate;
```

Now we join the Customer table and we have our answer.

Solution

```SQL
SELECT 
    ConcernedOrders.ProductName, 
    Customer.CompanyName, 
    Customer.ContactName 
FROM 
    Customer
JOIN 
    (SELECT 
        O.CustomerId AS CustomerId, 
        ODates.ProductName
    FROM 
        'Order' AS O
    JOIN 
        (SELECT 
            MIN(O.OrderDate) AS OrderDate, 
            DP.ProductName
        FROM 
            'Order' AS O
        JOIN 
            (SELECT 
                OrderId, 
                ProductId, 
                P.ProductName
            FROM 
                OrderDetail
            JOIN 
                Product AS P ON P.Id = OrderDetail.ProductId
            WHERE 
                P.Discontinued = 1
            ) AS DP ON O.Id = DP.OrderId
        GROUP BY 
            DP.ProductId
        ) AS ODates ON O.OrderDate = ODates.OrderDate
    ) AS ConcernedOrders ON Customer.Id = ConcernedOrders.CustomerId
ORDER BY 
    ConcernedOrders.ProductName;
```

Phew, that was a lot for me. Now, I'm excited if 10 pointers could make me sweat, what will 15 pointers do. I'm ready. First let me satiate my anxiety by checking my solution. And it's correct. Moving on to the next question.

---
> Q7. For the first 10 orders by CutomerId BLONP: get the Order's Id, OrderDate, previous OrderDate, and difference between the previous and current. Return results ordered by OrderDate (ascending)
Details: The "previous" OrderDate for the first order should default to itself (lag time = 0). Use the julianday() function for date arithmetic (example).
Use lag(expr, offset, default) for grabbing previous dates.
Please round the lag time to the nearest hundredth, formatted like 17361|2012-09-19 12:13:21|2012-09-18 22:37:15|0.57

On querying, we have 150 orders from the Customer ID BLONP. We have to find the first 10 orders ordered by OrderDate (ascending).

After reviewing sliding functions, this exercise felt a bit on the easier side.
Here's the solution.

```SQL
SELECT 
    O.Id, 
    O.OrderDate AS OrderDate, 
    LAG(OrderDate, 1, OrderDate) OVER(ORDER BY OrderDate) AS PrevOrderDate, 
    ROUND(julianday(OrderDate) - julianday(LAG(OrderDate, 1, OrderDate) OVER(ORDER BY OrderDate)), 2) 
FROM 
    'Order' AS O 
JOIN 
    Customer AS C ON O.CustomerId = C.Id 
WHERE 
    C.Id = "BLONP"
ORDER BY 
    O.OrderDate
LIMIT 10;
```

I have checked my answer and it is correct! Currently I stand at 55 points. I am yet to pass the assignment.

---
> Q8. For each Customer, get the CompanyName, CustomerId, and "total expenditures". Output the bottom quartile of Customers, as measured by total expenditures.
Details: Calculate expenditure using UnitPrice and Quantity (ignore Discount). Compute the quartiles for each company's total expenditures using NTILE. The bottom quartile is the 1st quartile, order them by increasing expenditure.
Make sure your output is formatted as follows (round expenditure to nearest hundredths): Bon app|BONAP|4485708.49\
**Note:** There are orders for CustomerIds that don't appear in the Customer table. You should still consider these "Customers" and output them. If the CompanyName is missing, override the NULL to 'MISSING_NAME' using IFNULL.

We have 91 customers and each customer has roughly 184 orders. We have to print the Customer's CompanyName, CustomerId and a total expenditure column. We have to print the bottom quartile of the customers.

Here's the CustomerIds with their expenditure,

```SQL
WITH expenditure AS (
    SELECT 
        O.CustomerId AS CustomerId, 
        ROUND(SUM(UnitPrice * Quantity), 2) AS exp 
    FROM 
        OrderDetail 
    LEFT JOIN 
        'Order' AS O ON O.Id = OrderDetail.OrderId 
    GROUP BY 
        O.CustomerId
)
SELECT 
    CustomerId, 
    exp 
FROM 
    expenditure;
```

Now we have to also include the customer Company Name, we can join this table with Customer table and get the CompanyName.

```SQL
WITH expenseInfo AS (
    WITH expenditure AS (
        SELECT 
            O.CustomerId AS CustomerId, 
            ROUND(SUM(UnitPrice * Quantity), 2) AS exp 
        FROM 
            OrderDetail 
        LEFT JOIN 
            'Order' AS O ON O.Id = OrderDetail.OrderId 
        GROUP BY 
            O.CustomerId
    )
    SELECT 
        Customer.CompanyName AS CompanyName,
        CustomerId, 
        exp 
    FROM 
        expenditure
    JOIN
        Customer ON Customer.Id = CustomerId
)
SELECT 
    * 
FROM 
    expenseInfo;
```

Now, we are left with limiting the output to the bottom quartile ordered by increasing expenditure

```SQL
WITH OP AS (
    WITH expenseInfo AS (
        WITH expenditure AS (
            SELECT 
                O.CustomerId AS CustomerId, 
                ROUND(SUM(UnitPrice * Quantity), 2) AS exp 
            FROM 
                OrderDetail 
            JOIN 
                'Order' AS O ON O.Id = OrderDetail.OrderId 
            GROUP BY 
                O.CustomerId
        )
        SELECT 
            IFNULL(Customer.CompanyName, "MISSING_NAME") AS CompanyName,
            CustomerId, 
            exp 
        FROM 
            expenditure
        LEFT JOIN
            Customer ON Customer.Id = CustomerId
    )
    SELECT 
        *, 
        NTILE(4) OVER(ORDER BY exp) AS qtile
    FROM 
        expenseInfo
)
SELECT 
    CompanyName, 
    CustomerId, 
    exp 
FROM 
    OP 
WHERE 
    qtile = 1 
ORDER BY 
    exp;
```

Maybe a bit too much of WITH clause but I like this approach better. Let's check if I'm correct in this approach. And upon checking, it's correct.

Finally I'm at 70 points! I have passed the assignment. Now let's get an A.

---
> Q9. Find the youngest employee serving each Region. If a Region is not served by an employee, ignore it.
Details: Print the Region Description, First Name, Last Name, and Birth Date. Order by Region Id.

First let's print all the EmployeeIds and RegionIds.
We only have 9 Employees and here's the employee ids with their region ids.

```SQL
SELECT 
    EmployeeId, 
    Territory.RegionId 
FROM 
    EmployeeTerritory
JOIN 
    Territory ON EmployeeTerritory.TerritoryId = Territory.Id;
```

And here's my solution

```SQL
WITH FINALOUTPUT AS (
    WITH EmployeeTerritoryRegion AS (
        SELECT 
            EmployeeId, 
            Territory.RegionId 
        FROM 
            EmployeeTerritory
        JOIN 
            Territory ON EmployeeTerritory.TerritoryId = Territory.Id
    )
    SELECT 
        Employee.Id AS EmployeeId, 
        Employee.FirstName AS FirstName, 
        Employee.LastName AS LastName, 
        Employee.BirthDate AS BirthDate, 
        EmployeeTerritoryRegion.RegionId AS RegionId, 
        ROW_NUMBER() OVER (PARTITION BY EmployeeTerritoryRegion.RegionId ORDER BY Employee.BirthDate DESC) AS RowNumber
    FROM
        Employee
    JOIN
        EmployeeTerritoryRegion ON EmployeeTerritoryRegion.EmployeeId = Employee.Id
    GROUP BY
        Employee.Id, Employee.FirstName, Employee.LastName, Employee.BirthDate, EmployeeTerritoryRegion.RegionId
    ORDER BY 
        Employee.BirthDate
)
SELECT
    Region.RegionDescription,
    FirstName,
    LastName,
    BirthDate
FROM 
    FINALOUTPUT
JOIN
    Region ON Region.Id = FINALOUTPUT.RegionId
WHERE
    RowNumber = 1
ORDER BY
    RegionId;
```

I used `ROW_NUMBER()` to get the youngest employee for each region. And the answer is correct. 85 points to me pushing me to a grade B. One final question remain. Let's finish this exercise.

---
> Q10. Concatenate the ProductNames ordered by the Company 'Queen Cozinha' on 2014-12-25.
Details: Order the products by Id (ascending). Print a single string containing all the dup names separated by commas like Mishi Kobe Niku, NuNuCa Nuß-Nougat-Creme...

I came up with this query that concatenates ProductNames with The previous ProductName

```SQL
WITH ProductNames AS (
    SELECT 
        Product.ProductName AS ProductName, 
        ROW_NUMBER() OVER(ORDER BY ProductId) AS Id,
        LAG(ProductName) OVER(ORDER BY ProductId) as PrevProductName
    FROM 
        OrderDetail 
    JOIN 
        Product ON Product.Id = OrderDetail.ProductId 
    WHERE 
        OrderId = 18491 
    ORDER BY 
        ProductId)
SELECT PrevProductName || ", " || ProductName from ProductNames;
```

And this is the final query. I admit I had to look around a lot for this to work but it does finally. I am not super confident about it's efficiency and I'd like to see how the official answer compares to mine.

```SQL
WITH RECURSIVE ProductNames AS (
    SELECT 
        Product.ProductName AS ProductName, 
        ROW_NUMBER() OVER(ORDER BY ProductId) AS Id
    FROM 
        OrderDetail 
    JOIN 
        Product ON Product.Id = OrderDetail.ProductId 
    WHERE 
        OrderId = 18491 
),
cnct AS (
    SELECT ProductName, Id FROM ProductNames WHERE Id = 1 
    UNION ALL
    SELECT cnct.ProductName || ', ' || ProductNames.ProductName, ProductNames.Id 
    FROM ProductNames 
    JOIN cnct ON ProductNames.Id = cnct.Id + 1
)
SELECT ProductName FROM cnct ORDER BY ID DESC LIMIT 1;
```

And Upon checking, This is correct. That is a perfect score!!!

Next blog will be comparing my solutions with the official solution and see where I could have done better. See y'all there.
