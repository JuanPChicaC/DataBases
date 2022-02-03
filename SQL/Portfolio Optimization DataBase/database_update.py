from database_model import *
import beggining_information
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def clients_update(clients):
    
    for client in clients:

        session.add(
            Client(
                username = client['username']
                )
            )

        session.commit()
    
    logger.info(
        "The client's information is already been uploaded into the CLient table"        
        )    
    
def periods_update(periods):

    for period in periods:

        session.add(
            Information_Period(
                code = period['code'],
                description = period['description'],
                minutes_equivalence = period['time_minutes']
                )
            )
    
        session.commit()
    
    logger.info(
        "The period's information is already been uploaded into the Information_Period table"        
        ) 

def intervals_update(intervals):
    
    for interval in intervals:
        
        session.add(
            Information_Interval(
                code = interval['code'],
                description = interval['description'],
                minutes_equivalence = interval['time_minutes']
                )
            )
        
        session.commit()

    logger.info(
        "The interval's information is already been uploaded into the Information_Period table"        
        )

def portfolios_update(portfolios):

    for portfolio in portfolios:
        
        period_required = session.query(
            Information_Period
            ).filter(
                Information_Period.code == portfolio['period code']
                ).first()
        
        interval_required = session.query(
            Information_Interval
            ).filter(
                Information_Interval.code == portfolio['interval code']
                ).first()
        
        client_required = session.query(
            Client
            ).filter(
                Client.username == portfolio['client']
                ).first()
        
        session.add(
            Portfolio(
                name  = portfolio['name'],
                description = portfolio['description'],
                client_id = client_required.id,
                interval_id = interval_required.id,
                period_id = period_required.id
                )
            )
        
        session.commit()
    
    logger.info(
        "The portfolio's information is already been uploaded into the Portfolio table"        
        )

if __name__ == '__main__':
    
    #insertion of the first clients records
    clients_update(
        beggining_information.clients
        )
    #insertion of the periods records
    periods_update(
        beggining_information.periods
        )
    
    #insertion of the interval records
    intervals_update(
        beggining_information.intervals
        )

    # insertion of portfolio rqcords
    portfolios_update(
        beggining_information.portfolios
        )
    
                           

