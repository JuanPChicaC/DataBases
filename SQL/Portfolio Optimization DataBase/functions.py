# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:18:26 2022

@author: juanp
"""

from sqlalchemy import DDL


create_sum_validation_function = DDL(
    '''
    CREATE FUNCTION CheckPercentage(id_portfolio int) 
    RETURNS int 
    DETERMINISTIC
    
    BEGIN 
        
        DECLARE Suma float ;
        DECLARE Return_value int ;
          
        SELECT 
            SUM (optimal_participation) into Suma 
            FROM portfolio_asset 
            WHERE portfolio_id = id_portfolio; 
    
        IF (Suma >= 0)  AND (Suma < 1.0001) THEN
            SET Return_value = 0; 
    
        ELSE 
            SET Return_value = 1; 
        
        END IF;
        
        RETURN Return_value;  
    END;
    '''
    )
