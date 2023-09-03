### Context
In a few years, we plan to launch our ecommerce application on a global scale. To prepare for this scenario, we have envisioned several challenges that lie ahead. At Jeevee, we anticipate that our engineers should be well-prepared to handle real-world problems by focusing on the scalability and optimization of both infrastructure and code.

### Challenge
Our Analytics team will need a report that includes the following:
1. The top 50 products purchased in each respective country.
2. The top 50 products most frequently purchased by each respective user.
3. The Analytics app will consider the logs from the past 7 days for reporting.


For the purpose of the challenge, consider that we are receiving data each day in a
folder, a text file named purchased-YYYYMMDD.log that contains the logs of all
purchased made on Jeevee on that date. These logs are formatted as
follows:
- There is a row per purchase.
- Each row is in the following format: product_id|user_id|country


**product_id**: Unique product identifier, an integer. For your information, Jeevee
catalog will contains more than 1M products, a number that is constantly
increasing.

**user_id**: Unique user identifier, an integer. Jeevee currently has millions of
users, a number that is constantly increasing.

**country**: 2 characters string upper case that matches the country ISO
code (Ex: NP, CHN, IND, ...). There are 249 existing country codes.
In the context of the exercise, we are considering that the daily number of
purchase is around 30M. We should expect that the file contains occasionally
corrupted rows that do not respect the format given above. Therefore, having
some corrupted rows as input should not have an impact on the proper
functioning of the script.

You can find sample data in directory called **input** of your assignment.

### Objective

The objective of this challenge is to propose a system that computes, on a daily basis, the top 50 products that were most purchased in each country during the last 7 days. Additionally, you may also suggest computing the top 50 products (optional) that were most purchased by each user during the last 7 days.

To achieve this goal, you are required to suggest a set of scripts that will produce one text file each day.

1) [Must have] country_top50_YYYYMMDD.txt on which each row contains
the top 50 products purchased in a specific country, on the specified format:
country|product_id1:n1,product_id2:n2,product_id3:n3,...,product_id50:n50

2) [Optional] users_top50_YYYYMMDD.txt on which each row contains the top 50 products purchased by a specific user, on the specified format:
user_id|product_id1:n1,product_id2:n2,product_id3:n3,...,product_id50:n50

where country is the country ISO code (2 characters long)
product_id1:n1 the product_id1 is most purchased product id and n1 is number of times product purchased

### Suggestion
You can choose any programming language of your choice; however, you are restricted from using third-party systems that would require running a service (e.g., MongoDB, PostgreSQL, MapReduce, Hadoop, etc.).

Your solution should preferably use minimal RAM (less than 1 GB), and you have the ability to write intermediate information to the disk if necessary. The suggested system can save intermediate information on the disk, which will be reused on the following day.


### Expected Delivery
Please provide the code along with a readme that explains the reasons for choosing a particular approach to solve the problem. You can be creative by designing a high-level architectural diagram of your approach.
We highly value developers who have the skills to write clean, testable, reusable, and production-ready code. We strongly encourage such individuals to join our team and contribute to building a global-scale product.

### FYI
We don't enforce you to use the technologies we use on a daily basis. However, we want to let you know that we utilize these cool technologies to build our large-scale distributed system.
- Programming Languages: Python, JavaScript, Dart, ShellScript
- Containerization: Docker
- CI/CD: Gitlab, Bamboo Pipeline, AWS Code Pipeline
- Framework: Flask, FastAPI, Django, Odoo, Next.js, Flutter, Android, iOS, React
- Database: Postgres, Redis, MySQL
- Testing: Unit Testing
- Others: ECS, RabbitMQ, Microservices, Serverless Function, Elastic Container Service, Nginx, Load Balancers, API Gateway, SQS, S3, CDK

### Submission
We assume that you can run ```main.py``` to get information to sumbit your work.