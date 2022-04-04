# Portfolio Optimization DataBase
## Entity Relationship Diagram
![DataBase ERD](https://github.com/JuanPChicaC/DataBases/blob/main/SQL/Portfolio%20Optimization%20DataBase/DataBase_ERD.png)
### Entities Explanation
- **Client**\
This table conatins the information about clients, it includes username and the creation date as main attributes. The token attribute is just a result of a simplified implementation of the API, because in the architecture of the service an authentication layer wasn´t contemplated. Client table has a  zero to many relation with Portfolio entity, it means that clients could have none or many portfolios. 
- **Portfolio**\
This table contains the information about clients portfolios. the main atributes are: name and description, it allow the user save description and name for specific portfolios in order to maintin the control. It has relation with interval and period entities, the function of this relation is to maintain the normality about the period and the interval that the user will use to call the yahoo finance API (see the method ***generate information*** for [***Price_Array***](https://github.com/JuanPChicaC/Optimization/blob/main/Static%20Optimization/Portfolio%20Optimization%20Model/generalization.py)  for more information)
- **Interval**\
This entity containa all the possible options for intervals available in Yahoo Finance API. As outstanding it has a minutes_equivalence attribute, this attribute will be used to compare the time equivalence in relation with the selected period for an specific portfolio, it allow to control the data integrity to make a correct request to the Yahoo API
- **Period**\
This entity containa all the possible options for periods available in Yahoo Finance API
- **Portfolio_Asset**\
This table is used to broke the relation many to many that Portfolio and Asset entities has, It is just a normalization great practice.
- **Asset**\
This table contains all the symbol list that Yahoo Finance has, it will be filled by a [ETL Process](https://github.com/JuanPChicaC/DataBases/tree/main/ETL)
- **Type_Asset**\
This table contains the information about the type of asset options available for the symbols that are saved in the Asset table.
- **Exchange**\
This table contains the information about the Exchange options available for the symbols that are saved in the Asset table.
