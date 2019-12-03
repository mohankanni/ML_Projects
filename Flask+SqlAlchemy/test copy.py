import sqlalchemy
from sqlalchemy import *
import ibm_db_dbi
# import ibm_db_sa 
db2 = sqlalchemy.create_engine('db2+ibm_db://')
# db2+ibm_db://cccuser:Ccc@p#999@49.205.69.22:50000/GPROD