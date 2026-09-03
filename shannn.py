products = []

for product_number in range(1, 6):
	print(f"\nEnter details for product {product_number}")
	product_id = input("Product ID: ")
	name = input("Product name: ")
	price = float(input("Price: "))
	quantity = int(input("Quantity: "))

	products.append({
		"id": product_id,
		"name": name,
		"price": price,
		"quantity": quantity,
		"amount": price * quantity,
	})

total = sum(product["amount"] for product in products)

if total > 5000:
	discount_rate = 0.10
elif total >= 3000:
	discount_rate = 0.05
else:
	discount_rate = 0

discount = total * discount_rate
final_amount = total - discount

print("\nProduct Details")
print(f"{'ID':<12}{'Name':<20}{'Price':>10}{'Quantity':>10}{'Amount':>12}")
print("-" * 64)

for product in products:
	print(
		f"{product['id']:<12}{product['name']:<20}"
		f"{product['price']:>10.2f}{product['quantity']:>10}"
		f"{product['amount']:>12.2f}"
	)

print("-" * 64)
print(f"Total amount:   {total:.2f}")
print(f"Discount ({discount_rate * 100:.0f}%): {discount:.2f}")
print(f"Final amount:    {final_amount:.2f}")
