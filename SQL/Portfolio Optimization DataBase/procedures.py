# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:41:11 2022

@author: juanp
"""

from sqlalchemy import DDL


create_set_participation_null_procedure = DDL(
    '''
    CREATE PROCEDURE 
        set_null_portfolio_participation(
            IN portfolio__id int
            )
    BEGIN    
        UPDATE 
            portfolio_asset 
        SET    
            optimal_participation = NULL,
            expected_return = NULL,
            expected_risk = NULL
        WHERE
            portfolio_id = portfolio__id;
    END;
    '''
    )