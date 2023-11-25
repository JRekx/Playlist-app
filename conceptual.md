### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
1. Also Known as Postgres, PSQL is a open source object related database. PostGres is used by developers to build web applications as well as data warehousing.

- What is the difference between SQL and PostgreSQL?
2. SQL stand for Structerd Query Language, its used for managing and manipulating relational databases. While PostgreSql is an open-source relational database mangment system (RDBMS) that uses SQL

- In `psql`, how do you connect to a database?
2. By going into the Terminal and using the following command:

psql -h hostname -d dbname -U username -W

Replace hostname with the name of the server you are using and same with dbname.

- What is the difference between `HAVING` and `WHERE`?
3. Where is used in SQL to filter rows before they are grouped and aggregated.
It filters rows bases on specifed criteria.

Having is used to filter rows after they have been grouped and aggerated.
It filters the results bassed on aggerated functions allowing you to specify conditions on the aggerated data.


- What is the difference between an `INNER` and `OUTER` join?
4. Inner Join retrieves only from rows that both tables have matiching values.
They are uses when you only want to retrive rows that have corresponding rows 

Outer join retrives all the rows from on table and the matching rows from the other table. If there is no match the result will only include rows from table.
They are used when you want to retrieve all rows from one table, including the unmatched rows and the matching rows.


- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
5.Left outer retrieves all rows from the left table and the matching rows from the right table same for RIGHT OUTER but using the all rows from the rigt table.

- What is an ORM? What do they do?
6. ORM = Object-Relational Mapping. A porgramming tech used to convert data between incomapatible type systems in oops languages. 


- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
7. AJAX is used for real time interactivity and dynamic updates as well as providing user experinces.
Http are used for servere to server comunication, Background task, as well as intergating external data into server side applications. 

- What is CSRF? What is the purpose of the CSRF token?
8. CSRF = Cross-site Request Forgery.
It is a type of security vulenerability that occures when malicouses website tricks a users browser into exectuing  actions on another website without the users knowledge or consent. 
A CRSF Token prevents that by creating a unique token for session and user that the server must validate.

- What is the purpose of `form.hidden_tag()`?
A function provided by the Flask-WTF extension that is used to generate a hidden input field for a form.
This works with CRF token that will be auto added to the from. 