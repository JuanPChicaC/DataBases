from sqlalchemy import  event
import database_model as dm
from triggers import (
    update_portfolio_time_validator_trigger,
    insert_portfolio_time_validator_trigger,    
    insert_portfolo_asset_validator_trigger,
    update_portfolo_asset_validator_trigger
    )
from functions import create_sum_validation_function
from procedures import create_set_participation_null_procedure

__events = {
    'Set sum validation funtion' : {
        'target': dm.Base.metadata,
        'identifier': 'after_create',
        'action' : create_sum_validation_function
        },
    'set procedure to null participation' : {
        'target': dm.Base.metadata,
        'identifier': 'after_create',
        'action' : create_set_participation_null_procedure
        },
    'set insert trigger to validate period and interval of the portfolio' :{
        'target': dm.Portfolio.__table__,
        'identifier': 'after_create',
        'action' : insert_portfolio_time_validator_trigger      
        },
    'set update trigger to validate period and interval of the portfolio' :{
        'target': dm.Portfolio.__table__,
        'identifier': 'after_create',
        'action' : update_portfolio_time_validator_trigger    
        },
    'set insert trigger to validate participation of assets in the portfolio' :{
        'target': dm.Portfolio_Asset.__table__,
        'identifier': 'after_create',
        'action' : insert_portfolo_asset_validator_trigger
        },
    'set update trigger to validate participation of assets in the portfolio' :{
        'target': dm.Portfolio_Asset.__table__,
        'identifier': 'after_create',
        'action' : update_portfolo_asset_validator_trigger    
        }    
    }


def events_insertion(events_dictionary):
    
    for event_name in events_dictionary.keys():
        
        event.listen(
            events_dictionary[event_name]['target'],
            events_dictionary[event_name]['identifier'],
            events_dictionary[event_name]['action']
            )


def creation():
    
    dm.Base.metadata.drop_all(
        dm.engine
        )
    
    events_insertion(
        __events
        )

    dm.Base.metadata.create_all(
        dm.engine
        )
    
if __name__ == '__main__':
    
    creation()

