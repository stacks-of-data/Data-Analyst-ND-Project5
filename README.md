# Exploring The Fraud Detection Dataset
## by Ammar Saleh

## Dataset

> In this project we are going to perform exploratory and explanatory analysis on the <ins>[Fraud Detection Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection)</ins> which is a simulated dataset that includes legitimate and fraud transactions from 2019 - 2020 from <ins>[Kaggle](https://www.kaggle.com/)</ins>.  
The clean dataset includes `21` columns and `1296675` rows which doesn't include any duplicated or NULL rows, here is the details about each column in this dataset:

Reference: https://www.kaggle.com/datasets/kartik2112/fraud-detection
* `trans_datetime`: Transaction DateTime.
* `cc_num`: Credit Card Number of Customer.
* `merchant`: Merchant Name.
* `category`: Category of Merchant.
* `amt`: Amount of Transaction.
* `first_name`: First Name of Credit Card Holder.
* `last_name`: Last Name of Credit Card Holder.
* `gender`: Gender of Credit Card Holder.
* `street`: Street Address of Credit Card Holder.
* `city`: City of Credit Card Holder.
* `state`: State of Credit Card Holder.
* `zip`: Zip Code of Credit Card Holder.
* `lat`: Latitude Location of Credit Card Holder.
* `long`: Longitude Location of Credit Card Holder.
* `city_pop`: Credit Card Holder's City Population.
* `job`: Job of Credit Card Holder.
* `dob`: Date of Birth of Credit Card Holder.
* `trans_id`: Transaction ID.
* `merch_lat`: Latitude Location of Merchant.
* `merch_long`: Longitude Location of Merchant.
* `is_fraud`: Fraud Flag.


## Summary of Findings
1. `gas_transport` merchant category has the highest transactions count.
2. Most of transactions cost ranges from 1-10 and there are decent amount of transactions from 10-100.
3. The ZIP code with the highest count of transactions is **73754**.
4. The job with the highest count of transactions is Film/video editor.
5. The merchant with the highest count of transactions is **Kilback LLC**.
6. The month and day with the highest count of transactions is May and Day 1 and the month and day with the lowest count of transactions is Oct and Day 31.
7. The city and state with the highest count of transactions is Birmingham and Texas.
8. The marchant category with the highest count of fraud is grocery point of sales.
9. Cities with low count of population has higher fraud transactions.
10. Some ZIP codes with higher count of transactions has higher count of fraud.
11. Similarly to ZIP codes we can see that some jobs with high transactions count has higher fraud transactions.
12. Most states with higher count of transactions has higher count of fraud but for cities only some of them with higher count of transactions has higher count of fraud.
13. Some merchants with higher count of transactions has higher count of fraud.
14. The month and day with the highest count of fraud transactions is Mar and Day 20 and the month and day with the least count of fraud transactions is Jul and Day 6.
15. Transactions with cost that ranges from 200-1000 has the highest count of fraud transactions.
16. The travel category has the lowest fraud transactions count/cost while shopping point of sale has the has the highest fraud transactions cost.


## Key Insights for Presentation
Insight 1: Which category is associated with the highest count of frauds transactions?
Insight 2: What are the top 15 ZIP codes that has the highest fraud transactions?
Insight 3: What job is associated with the highest fraud transactions?
Insight 4: What are the top 15 cities and states with the highest frauds transactions count?
Insight 5: Which Month And Day Has The Highest And Lowsest Count Of Fraud Transactions?
Insight 6: What Transactions Cost Range Has the Highest Precentage Of Fraud Transactions?
Insight 7: What Is The Difference Between Fraud And Normal Transactions For Each Category?
