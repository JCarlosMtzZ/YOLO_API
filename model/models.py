from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Float, String, DateTime

product_table = Table(
    'product',
    Column('id', Integer, primary_key=True),
    Column('code', String(20)),
    Column('name', String(30)),
    Column('unitprice', Float(10, 2))
)

discount_table = Table(
    'discount',
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('amount', Float(10, 2)),
    Column('startdate', DateTime),
    Column('enddate', DateTime)
)
    