from sqlalchemy import create_engine
from sqlalchemy.orm import backref, sessionmaker, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Sequence,
    Float
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserMaster(Base):
    __tablename__ = 'user_master'
    __table_args__ = {'schema': 'common_user'}

    id = Column(String, primary_key=True)
    login_id = Column(String)
    PASSWORD = Column(String)
    # office = Column(String)

    def __init__(self, login_id,PASSWORD):
        self.login_id = login_id
        self.PASSWORD = PASSWORD

    def check_password(self, PASSWORD):
        return self.PASSWORD
        

class UserRole(Base):
    __tablename__ = 'rbac_user_role'
    __table_args__ = {'schema': 'common_user'}
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('UserMaster.id'))
    office_id = Column(String)
    
    def __init__(self,user_id,office_id):
        self.user_id = user_id
        self.office_id = office_id
          

# class OfficeMaster(Base):
#     __tablename__ = 'office_master'
#     __table_args__ = {'schema': 'common_user'}
#     id = Column(String, primary_key=True)
#     name = Column(String)
    
#     def __init__(self, name):
#         self.name = name

# class TreeNode(Base):
#     __tablename__ = 'office_master'
#     __table_args__ = {'schema': 'common_user'}
#     id = Column(String,primary_key=True) 
#     parentoffice_id = Column(String,ForeignKey('common_user.office_master.id'))
#     name = Column(String(200))

#     children = relationship("TreeNode",
#                 backref=backref('parentoffice', remote_side=[id])
#             )

# create an engine
# engine = create_engine('postgresql://')
# engine = create_engine('db2+ibm_db://')
# create a configured "Session" class
# Session = sessionmaker(bind=engine)

# # create a Session
# session = Session()



# #3 - extract all movies
# UserRole = session.query(UserMaster).filter(UserMaster.login_id == str('sysadmin'),UserMaster.PASSWORD == str('{SHA}Yh/8ezG8WuKVAKIWUQO3CKTy4hE='))
# #4 - print movies' details
# print('\n### All UserMaster:')
# for logins in UserRole:
#     print(f' For Users {logins.login_id} Password is : {logins.PASSWORD}')
# print('')
# print(str(logins.PASSWORD) for logins in UserRole)

# if UserRole:
#     abc = 1
# else:
#     abc=0

# print(abc)

