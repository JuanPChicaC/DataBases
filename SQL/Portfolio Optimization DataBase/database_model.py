from sqlalchemy.ext.declarative import declarative_base
from configuration import Environment_Configuration, token_generator
from sqlalchemy import (
    Column,
    Integer, 
    Float, 
    Text, 
    String, 
    DateTime, 
    ForeignKey, 
    UniqueConstraint, 
    CheckConstraint, 
    create_engine, 
    )

from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime


environment_configuration = Environment_Configuration()

db_url = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
    environment_configuration.database['username'],
    environment_configuration.database['password'],
    environment_configuration.database['host'],
    environment_configuration.database['port'],
    environment_configuration.database['schema']
    )

engine = create_engine(
    db_url
    )
Session = sessionmaker(
    engine
    )
session = Session()

Base = declarative_base()


class Client(Base):
    
    __tablename__ = 'client'
    
    id = Column(
        Integer(),
        primary_key = True,
        nullable = False,
        unique = True,
        autoincrement=True
        )
    
    username = Column(
        String(50),
        nullable = False,
        unique = True,
        index = True
        )
    
    token = Column(
        String(25),
        nullable = False,
        default = token_generator(25)
        )
    
    created_at = Column(
        DateTime(),
        nullable = False,
        default = datetime.now()
        )
    
    portfolio_relation = relationship(
        'Portfolio',
        back_populates = 'client_relation'
        )
        
class Type_Asset(Base):
    
    __tablename__ = 'type_asset'
    
    id = Column(
        Integer(),
        primary_key = True,
        nullable = False,
        unique = True,
        autoincrement=True
        )
    
    description = Column(
        String(20),
        nullable = False,
        unique = True
        ) 
    
    asset_relation = relationship(
        'Asset',
        back_populates = 'type_asset_relation'
        )

class Exchange(Base):
    
    __tablename__ = 'exchange'
    
    id = Column(
        Integer(),
        primary_key = True,
        nullable = False,
        unique = True,
        autoincrement=True
        )
    
    description = Column(
        String(20),
        nullable = False,
        unique = True
        )
    
    asset_relation = relationship(
        'Asset',
        back_populates = 'exchange_relation'        
        )

class Information_Interval(Base):
    
    __tablename__ = 'information_interval'
    
    id = Column(
        Integer(),
        primary_key = True,
        nullable = False,
        unique = True,
        autoincrement=True
        )
    
    code = Column(
        String(5),
        nullable = False,
        unique = True,
        index = True
        )
    
    minutes_equivalence = Column(
        Integer()
        )
    
    description = Column(
        Text(100)
        )
    
    portfolio_relation = relationship(
        'Portfolio',
        back_populates = 'interval_relation'
        )

class Information_Period(Base):
    
    __tablename__ = 'information_period'
    
    id = Column(
        Integer(),
        primary_key = True,
        nullable = False,
        unique = True,
        autoincrement=True
        )
    
    code = Column(
        String(5),
        nullable = False,
        unique = True,
        index = True
        )

    minutes_equivalence = Column(
        Integer()
        )
    
    description = Column(
        Text(100)
        )

    portfolio_relation = relationship(
        'Portfolio',
        back_populates = 'period_relation'
        )


class Asset(Base):

    __tablename__ = 'asset'

    id = Column(
        Integer(),
        primary_key = True,
        nullable = False,
        unique = True,
        autoincrement=True
        )

    name = Column(
        String(50),
        nullable = False,
        unique = True
        ) 

    symbol = Column(
        String(10),
        nullable = False,
        unique = True,
        index = True
        ) 

    type_asset_id = Column(
        Integer(),
        ForeignKey('type_asset.id'),
        nullable = False
        )
    
    type_asset_relation = relationship(
        'Type_Asset',
        back_populates = 'asset_relation'
        )

    exchange_id = Column(
        Integer(),
        ForeignKey('exchange.id'),
        nullable = False
        )

    exchange_relation = relationship(
        'Exchange',
        back_populates= 'asset_relation'
        )

    portfolio_asset_relation = relationship(
        'Portfolio_Asset',
        back_populates = 'asset_relation'
        )


class Portfolio(Base):
    
    __tablename__ = 'portfolio'

    id = Column(
        Integer(),
        primary_key = True,
        nullable = False,
        unique = True,
        autoincrement=True
        )
    
    name = Column(
        String(50),
        nullable = False,
        index = True
        )
    
    description = Column(
        Text(500),
        )
    
    expected_return = Column(
        Float(),
        nullable = True,
        )

    expected_risk = Column(
        Float(),
        nullable = True,
        )

    created_at = Column(
        DateTime(),
        nullable = False,
        default = datetime.now()
        )
    
#    beginning_date = Column(
#        DateTime(),
#        nullable = False        
#        )

#    ending_date = Column(
#        DateTime(),
#        nullable = False        
#        )

    client_id = Column(
        Integer(),
        ForeignKey('client.id'),
        nullable = False,
        index = True
        )

    client_relation = relationship(
        'Client',
        back_populates = 'portfolio_relation'
        )

    interval_id = Column(
        Integer(),
        ForeignKey('information_interval.id'),
        nullable = False
        )    

    interval_relation = relationship(
        'Information_Interval',
        back_populates = 'portfolio_relation'
        )
    
    period_id = Column(
        Integer(),
        ForeignKey('information_period.id'),
        nullable = False
        )    
    
    period_relation = relationship(
        'Information_Period',
        back_populates = 'portfolio_relation'
        )
    
    
    portfolio_asset_relation = relationship(
        'Portfolio_Asset',
        back_populates = 'portfolio_relation'
        )
    

    __table_args__ =(
        UniqueConstraint(
            'name',
            'client_id'
            ),
        CheckConstraint(
            'expected_return >= 0',
            'expected_risk >= 0'
            )
        )
    


class Portfolio_Asset(Base):
    
    __tablename__ = 'portfolio_asset'
    
    id = Column(
        Integer(),
        primary_key = True,
        nullable = False,
        unique = True,
        autoincrement=True
        )
    
    portfolio_id = Column(
        Integer(),
        ForeignKey('portfolio.id'),
        nullable = False,
        index =  True
        )
    
    portfolio_relation = relationship(
        'Portfolio',
        back_populates = 'portfolio_asset_relation'
        )
    
    asset_id = Column(
        Integer(),
        ForeignKey('asset.id'),
        nullable = False,
        index = True
        )

    asset_relation = relationship(
        'Asset',
        back_populates = 'portfolio_asset_relation'
        )

    optimal_participation = Column(
        Float(precision = 4),
        )
    
    expected_return = Column(
        Float(),
        )

    expected_risk = Column(
        Float(),
        )
        
    __table_args__ = (
        UniqueConstraint(
            'portfolio_id',
            'asset_id'
            ),
        CheckConstraint(
            'optimal_participation BETWEEN -1 AND 1',
            ),
        CheckConstraint(
            'expected_risk >= 0'
            )
        )



    