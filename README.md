# Pay-as-you-go Payment System
web platform using Python and Django that provides a pay-as-you-go payment model for users. Users will be charged based on the number of requests they make within a given period. The platform will track the count of requests for each user and calculate the total cost for the current month based on the number of requests made.

##  Software Requirements Specification Overview
- User Registration and Authentication
- Track User's Request
- Calculate Total Cost for each user based on their Request Count
- Retrieve User's Cost for Selected Period

## System Design
In this web platform developed using Django Rest framework, there are two base use cases, "Authentication" and "Billing". Each app has its own responsibilties and handles specific operations.

### Authentication
In the platform, Authentication is developed using the Djoser library and Simple JWT utilizes Django's pre-built User model.

By integrating Djoser with Simple JWT, authentication in the web platform utilizes Djoser's built-in functionalities for user registration and login while also leveraging Simple JWT's capabilities for token-based authentication. This combination enables secure authentication mechanisms for RESTful APIs, ensuring that users can authenticate and access the platform's resources using JWTs.

### Billing
The billing app consists of two main models: Price and Cost. These models are designed to handle pricing and cost-related data in a flexible and efficient manner. 

1. Price Model:
   - `unit_price`: This field is a DecimalField with `max_digits=10` and `decimal_places=4`. It represents the decimal price for each request. 
   - `service_name`: This field allows different prices to be set for different services. By associating a service name with each price, you can have varying pricing structures based on the type of service being provided. For example service "X" and "y", cost 1$ and 2$ per request respectively.
   - `created_at`: This field is a DateTimeField with `auto_now_add=True`. It automatically records the timestamp when a Price object is created. This allows you to track the history of price changes over time and retrieve the <ins>latest price</ins> based on the date.

2. Cost Model:
   - `request_cost`: This field represents the cost of each request made by a user. It can be of any appropriate numerical type (e.g., DecimalField, FloatField, etc.) depending on the precision needed for the cost value.
   - `created_at`: Similar to the Price model, this field is a DateTimeField with `auto_now_add=True`. It captures the timestamp when a Cost object is created, indicating the date of request delivery to the server. This is useful for tracking users' requests within specific time periods.
   - `service_name`: This field allows for filtering the request cost of a user for each service. By associating a service name with each cost entry, you can easily retrieve costs specific to a particular service.

Overall, the billing app's models provide a structure for managing pricing information with support for different services and tracking costs over time. Using the Price and Cost models, you can calculate the exact decimal cost based on the unit price and retrieve cost data for specific <ins>services</ins> and <ins>time periods</ins> as needed.


## Database and Indexing
The project is using PostgreSQL as the database. Although MySQL is reported to be slightly faster than PostgreSQL in write operations according to recent benchmarks, PostgreSQL was chosen for its high compatibility with the Django framework and better data compatibility.

Additionally, the decision has been made not to use indexing in the database. While indexing can improve performance in read operations and data retrieval, it can potentially slow down write operations. Since the majority of the platform's operations are write-type operations, the decision has been made to forgo indexing in favor of optimizing write performance.

This approach indicates a prioritization of efficient data writes and a willingness to trade off some read performance. 