WITH CategorizedAccounts AS (
    SELECT 
        account_id, 
        income,
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category
    FROM Accounts
),
AllCategories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
)
SELECT 
    c.category, 
    COUNT(a.category) AS accounts_count
FROM AllCategories c
LEFT JOIN CategorizedAccounts a
ON c.category = a.category
GROUP BY c.category
ORDER BY c.category;
