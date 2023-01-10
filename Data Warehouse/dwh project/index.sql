CREATE INDEX customer_id_index ON core.sales
(
    customer_id ASC
)


DROP INDEX core.customer_id_index


SELECT * FROM core.sales
WHERE customer_id = 4