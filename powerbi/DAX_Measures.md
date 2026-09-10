# Customer segmentation measures
```DAX
Customer Count = DISTINCTCOUNT(customers_segmented_powerbi[Customer_ID])
Average Spending = AVERAGE(customers_segmented_powerbi[Total_Spending])
Average Income = AVERAGE(customers_segmented_powerbi[Annual_Income])
Average Purchase Frequency = AVERAGE(customers_segmented_powerbi[Purchase_Frequency])
Total Customer Spending = SUM(customers_segmented_powerbi[Total_Spending])
```
