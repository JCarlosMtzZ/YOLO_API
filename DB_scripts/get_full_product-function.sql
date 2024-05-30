CREATE OR REPLACE FUNCTION get_full_product(p_name VARCHAR)
RETURNS TABLE (
    pcode VARCHAR,
    pname VARCHAR,
    punitprice NUMERIC,
    dname VARCHAR,
    damount NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    WITH currentproduct AS (
        SELECT 
            code AS productcode, 
            name AS productname, 
            unitprice AS unitprice
        FROM 
            product
        WHERE 
            name = p_name
    ),
    pdiscount AS (
        SELECT 
            pd.productcode AS productcode, 
            d.name AS discountname, 
            d.amount AS discountamount
        FROM 
            discount AS d 
        INNER JOIN 
            productdiscount AS pd ON pd.discountid = d.id
        WHERE 
            pd.productcode = (SELECT productcode FROM currentproduct)
            AND current_timestamp > d.startdate 
            AND current_timestamp < d.enddate
    )
    SELECT  
        p.productcode, 
        p.productname, 
        p.unitprice,
        CASE 
            WHEN pd.productcode IS NULL THEN 'No discount'
            ELSE pd.discountname
        END AS discountname,
        CASE 
            WHEN pd.productcode IS NULL THEN 0
            ELSE pd.discountamount
        END AS discountamount
    FROM 
        currentproduct AS p 
    LEFT JOIN 
        pdiscount AS pd ON p.productcode = pd.productcode;

    RETURN;
END;
$$ LANGUAGE plpgsql;