# End-to-End Cloud Data Analytics Pipeline

# Project Overview
This project demonstrates a full-stack data analysis solution, simulating a real-world e-commerce scenario. The goal was to build a cloud-based data architecture and extract business insights using modern BI tools.

Key Achievements:
* Designed a relational database schema for sales transactions.
* Provisioned and secured a Cloud Database on **AWS RDS**.
* Connected **Power BI** directly to the cloud instance for real-time reporting.

# Dashboard Preview
![Power BI Dashboard](dashboard_preview.png)
*(Visualization of sales performance by country, category, and time)*

#Tech Stack & Tools used
| Category | Tool/Service | Usage |
| :--- | :--- | :--- |
| **Cloud** | Amazon Web Services (AWS) | Hosted the MySQL Database (RDS) |
| **Database** | MySQL | Relational Data Storage & Management |
| **ETL/SQL** | SQL Scripts | Data Modeling, Schema Creation, Data Seeding |
| **Visualization** | Microsoft Power BI | Data Modeling, DAX Measures, Interactive Dashboards |
| **Security** | AWS VPC / Security Groups | Network Whitelisting & Firewall Configuration |

# Implementation Details

# 1. Database Architecture
Designed a Star Schema model consisting of three main tables to optimize for analytical queries:
* `Fact_Orders`: Transactional data (Sales, Quantity, Dates).
* `Dim_Customers`: Customer demographics.
* `Dim_Products`: Product details and categories.

#2. Cloud Setup (AWS RDS)
* Deployed a **MySQL** instance on AWS Relational Database Service.
* Configured **Security Groups** (Firewall) to allow traffic on port `3306` strictly from authorized IP addresses (Whitelisting).

#3. Data Visualization
Built an interactive report in Power BI with the following KPIs:
* **Total Sales & Order Volume**
* **Sales by Region (Map Visualization)**
* **Category Performance**
* **Monthly Sales Trend**

##How to Run
1. **Database:** Use the `db_setup_script.sql` file to recreate the database schema and insert dummy data into your local or cloud MySQL instance.
2. **Power BI:** Open `My_Cloud_BI_Project.pbix`. Note: You will need to update the Data Source settings to point to your own database instance if you want to refresh the data.
