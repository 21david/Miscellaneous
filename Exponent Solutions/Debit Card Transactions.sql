# https://www.tryexponent.com/practice/prepare/debit-card-transactions
# 2. Write a SQL query to list each cardholder and the number of times their transactions were rejected due to an incorrect PIN entry. 
# Output columns: cardholder_id, name (cardholder), no_of_rejections
# SQLite
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
