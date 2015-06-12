# Noodle code challenge(Shopify)

Shopify is a JSON API that returns data in Active Record JSON Format and a small database for products

#API documentation
API root: http://localhost:8000/

You can search for a product, supplier and customer by their names.
You can also search for an order by its order id.

Example: http://localhost:8000/products/?search=Omo

For the rest of the documentation, including URL's for updating all aspects of the api objects, go to localhost:8000/docs/

#Test
Run 'python manage.py test'.
The written test so far covers the following:

* PRODUCT CATEGORY: 'get all categories', 'get category when no data is available', 'create a category', 'create category with empty field', 'delete a category', 'to edit a category'.
* PRODUCT: 'get all products', 'get products when no data is available', 'get product with primary key that does not exist', 'create a product', 'delete a product', 'delete a product with primary key that does not exist', 'edit a product',
* ORDERS: 'get all orders', 'create an order', 'delete an order'

More tests would have been written if I had more time. Although, I tested the api routes manually using the documentation endpoint 'localhost:8000/docs/' and also the following endpoints:
*  http://localhost:8000/products/
* http://localhost:8000/categories/
* http://localhost:8000/suppliers/
* http://localhost:8000/customers/
* http://localhost:8000/orders/

I tested the api results on 'http://jsonlint.com/', a site that validates json data to be sure the data is returned in correct json format.
