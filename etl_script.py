import pandas as pd
import random
from faker import Faker
from sqlalchemy import create_engine
import datetime

# --- ΡΥΘΜΙΣΕΙΣ ΣΥΝΔΕΣΗΣ 
DB_USER = 'nikos'                  
DB_PASS = 'Nikos362514!'              
DB_HOST = 'bi-project-db.ck74k6q2oduy.us-east-1.rds.amazonaws.com'   
DB_NAME = 'cloud_bi_project'         
DB_PORT = '3306'                       
# Δημιουργία της "γέφυρας" σύνδεσης
connection_str = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

try:
    engine = create_engine(connection_str)
    print(" Η σύνδεση με τη βάση πέτυχε!")
except Exception as e:
    print(f" Σφάλμα σύνδεσης: {e}")
    exit()

# --- ΓΕΝΝΗΤΡΙΑ ΔΕΔΟΜΕΝΩΝ ---
fake = Faker()
orders_list = []

print(" Δημιουργία 50 νέων παραγγελιών...")

for i in range(50):
    # Φτιάχνουμε τυχαία IDs που ταιριάζουν με τους Customers (1-5) και Products (101-105)
    # Προσοχή: Το order_id το αφήνουμε να το βάλει η βάση αυτόματα αν είναι Auto Increment, 
    # αλλιώς εδώ φτιάχνουμε ένα τυχαίο μεγάλο νούμερο για να μην πέσουμε πάνω στα παλιά.
    cust_id = random.randint(1, 5)
    prod_id = random.randint(101, 105)
    
    # Τυχαία ημερομηνία μέσα στο 2024
    start_date = datetime.date(2024, 1, 1)
    random_date = fake.date_between(start_date=start_date, end_date=datetime.date.today())
    
    qty = random.randint(1, 10)
    
    # Τιμές (αντιστοιχούν χοντρικά στα προϊόντα μας για το παράδειγμα)
    price_map = {101: 699.99, 102: 1299.50, 103: 59.90, 104: 45.00, 105: 89.99}
    price = price_map.get(prod_id, 50.00) 
    
    total = round(qty * price, 2)
    
    # Προσθήκη στη λίστα
    orders_list.append({
        # Αν έχεις ορίσει το order_id ως Auto Increment στη βάση, αφαίρεσε την επόμενη γραμμή
        'order_id': random.randint(3000, 99999), 
        'customer_id': cust_id,
        'product_id': prod_id,
        'order_date': random_date,
        'quantity': qty,
        'total_sales': total
    })

# --- ΦΟΡΤΩΣΗ ΣΤΗ ΒΑΣΗ (LOAD) ---
df_new_orders = pd.DataFrame(orders_list)

try:
    # to_sql: Η μαγική εντολή που στέλνει τα δεδομένα
    df_new_orders.to_sql('Orders', con=engine, if_exists='append', index=False)
    print(f" Επιτυχία! Προστέθηκαν {len(df_new_orders)} νέες εγγραφές στη βάση.")
except Exception as e:
    print(f" Σφάλμα κατά την εγγραφή: {e}")