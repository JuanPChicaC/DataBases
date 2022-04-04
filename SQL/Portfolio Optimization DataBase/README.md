# Portfolio Optimization DataBase
## Entity Relationship Diagram
![DataBase ERD](https://github.com/JuanPChicaC/DataBases/blob/main/SQL/Portfolio%20Optimization%20DataBase/DataBase_ERD.png)
### Entities Explanation
- **Client**\
This table conatins the information about clients, it includes username and the creation date as main attributes. The token attribute is just a result of a simplified implementation of the API, because in the architecture of the service an authentication layer wasn´t contemplated. Client table has a  zero to many relation with Portfolio entity, it means that clients could have none or many portfolios. 
- **Portfolio**\
- This table contains the information about clients portfolios. the main atributes are: name and description, it allow the user save description and name for specific portfolios in order to maintin the control. It has relation with interval and period entities, the function of this relation is to maintain the normality about the period and the interval that the user will use to call the yahoo finance API (see the method ***generate information*** for [***Price_Array***](https://github.com/JuanPChicaC/Optimization/blob/main/Static%20Optimization/Portfolio%20Optimization%20Model/generalization.py)  for more information)
- **Interval**\
- **Period**\
- **Portfolio_Asset**\
- **Asset**\
- **TYpe_Asset**\
- **Exchange**\
