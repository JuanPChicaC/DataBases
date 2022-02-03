# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 18:53:16 2022

@author: juanp
"""

from sqlalchemy import DDL

insert_portfolio_time_validator_trigger = DDL(
    '''
    CREATE TRIGGER portfolio_time_validator_bi
    BEFORE INSERT ON portfolio
    FOR EACH ROW 
        BEGIN
            IF NOT EXISTS (
                SELECT 
                    1
                FROM 
                    information_period ip
                
                WHERE 
                    ip.id = new.period_id
                AND 
                    ip.minutes_equivalence > (
                        SELECT
                            ii.minutes_equivalence
                        FROM
                            information_interval ii
                        WHERE ii.id = new.interval_id
                    )
            ) THEN
                SIGNAL SQLSTATE '45000'   
                SET MESSAGE_TEXT = 'the period selected can\´t be less or equal to the selected interval';
            END IF;
        END;
    '''        
    )

update_portfolio_time_validator_trigger = DDL(
    '''
    CREATE TRIGGER portfolio_time_validator_bu
    BEFORE UPDATE ON portfolio
    FOR EACH ROW 
        BEGIN
            IF NOT EXISTS (
                SELECT 
                    1
                FROM 
                    information_period ip
                
                WHERE 
                    ip.id = new.period_id
                AND 
                    ip.minutes_equivalence > (
                        SELECT
                            ii.minutes_equivalence
                        FROM
                            information_interval ii
                        WHERE ii.id = new.interval_id
                    )
            ) THEN
                SIGNAL SQLSTATE '45000'   
                SET MESSAGE_TEXT = 'the period selected can\´t be less or equal to the selected interval';
            END IF;
        END;
    '''        
    )

insert_portfolo_asset_validator_trigger = DDL(
    '''
    CREATE TRIGGER assets_porticipation_portfolio_validator_ai
    AFTER INSERT ON portfolio_asset
    FOR EACH ROW
        BEGIN        
            IF CheckPercentage(new.portfolio_id) = 1
                THEN
                    CALL set_null_portfolio_participation(
                        new.portfolio_id
                        ); 
                    SIGNAL SQLSTATE '45000'   
                    SET MESSAGE_TEXT = 'the sum of all assets participation can\´t be better from one or less than cero';
            END IF;
        END;
    '''
    )

update_portfolo_asset_validator_trigger = DDL(
    '''
    CREATE TRIGGER assets_porticipation_portfolio_validator_au
    AFTER UPDATE ON portfolio_asset
    FOR EACH ROW
        BEGIN        
            IF CheckPercentage(new.portfolio_id) = 1
                THEN
                    CALL set_null_portfolio_participation(
                        new.portfolio_id
                        ); 
                    SIGNAL SQLSTATE '45000'   
                    SET MESSAGE_TEXT = 'the sum of all assets participation can\´t be different from one or less than cero';
            END IF;
        END;
    '''
    )



