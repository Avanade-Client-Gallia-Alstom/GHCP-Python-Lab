# Example sales data
sales_data = [
    {'category': 'Electronics', 'amount': 100},
    {'category': 'Clothing', 'amount': 50},
    {'category': 'Electronics', 'amount': 150},
    {'category': 'Books', 'amount': 30},
    {'category': 'Clothing', 'amount': 70},
    {'category': 'Books', 'amount': 20},
    {'category': 'Electronics', 'amount': 200},
    {'category': 'Books', 'amount': 40},
    {'category': 'Clothing', 'amount': 80}
]

#Original code
def process_sales_data(sales_data):
    # Step 1: Extract unique product categories
    categories = set(item['category'] for item in sales_data)
    
    # Step 2: Initialize dictionary to store total sales for each category
    category_totals = {category: 0 for category in categories}
    
    # Step 3: Calculate total sales for each category
    for item in sales_data:
        category_totals[item['category']] += item['amount']
    
    # Step 4: Format results
    results = [{'category': category, 'total_sales': total} for category, total in category_totals.items()]
    
    return results


#Optimized code
from collections import defaultdict
 
def process_sales_data(sales_data):
    # Step 1: Extract unique product categories and calculate total sales
    category_totals = defaultdict(int)
    for item in sales_data:
        category_totals[item['category']] += item['amount']
   
    # Step 2: Format results
    results = [{'category': category, 'total_sales': total} for category, total in category_totals.items()]
   
    return results
 


# Process sales data
results = process_sales_data(sales_data)
print(results)


 

 
