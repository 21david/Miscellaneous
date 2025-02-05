# https://www.tryexponent.com/practice/prepare/debit-card-transactions
# SQLite
    
/*
2. Write a SQL query to list each cardholder and the number of times their transactions were rejected due to an incorrect PIN entry. 
Output columns: cardholder_id, name (cardholder), no_of_rejections
"Easy"
*/
select
    t.cardholder_id,
    c.name,
    count(*) as no_of_rejections
from 'transaction' t
left join debit_card d
    on d.debit_card_id = t.debit_card_id
left join cardholder c
    on c.cardholder_id = t.cardholder_id
where pin <> pin_entered and is_rejected
group by t.cardholder_id;


/*
3. Write a SQL query to list each cardholder and the number of times their transactions were rejected because 
they were double charged the same amount on the same day, and the transaction was rejected, within the last 
month. 
Output columns: cardholder_id, name (cardholder), no_of_rejections
"Medium"
*/

/*
Notes
1. Pin needs to be correct (pin_entered = pin)
2. is_rejected needs to be true 
3. There needs to be a transaction with the same charge on the same day with is_reject = false
4. Date must be in the last month
5. Group by cardholder_id and count rows that meet the criteria above
6. Join cardholder table to get the name
*/

select 
    t1.cardholder_id,
    c.name,
    count(*) as no_of_rejections  -- count the number of rejections for each cardholder (#5)
from 'transaction' t1
join 'transaction' t2
    on t1.transaction_date = t2.transaction_date  -- transactions occurred on the same day (#3)
    and t1.charged_amt = t2.charged_amt  -- double charge (#3)
    and t1.is_rejected = 0 and t2.is_rejected = 1  -- one of the double charges was rejected (#3)
left join debit_card d
    on d.debit_card_id = t1.debit_card_id  -- join to check that te rejection was not due to wrong pin (#1)
left join cardholder c
    on t1.cardholder_id = c.cardholder_id  -- join to get cardholder name (#6)
where t1.transaction_date >= date('now', '-1 month')  -- transaction was within the last month (#4)
    and t1.pin_entered = d.pin  -- pin needs to be correct (#1)
group by t1.cardholder_id  -- group by cardholder to get the count of rejections for each (#5)
