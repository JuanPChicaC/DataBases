# Portfolio Optimization DataBase
## Entity Relationship Diagram
![DataBase ERD](https://github.com/JuanPChicaC/DataBases/blob/main/SQL/Portfolio%20Optimization%20DataBase/DataBase_ERD.png)
### Entities Explanation
- **client**\
This table will conatins the information about clients, it includes username and the creation date as main attributes. The token attribute is just a result of a simplified implementation of the API, because in the architecture of the service an authentication layer wasn´t contemplated. CLient table has a  zero to many relation with Portfolio entity, it means that clients could have none or many portfolios. 
- **Portfolio**\
- 
