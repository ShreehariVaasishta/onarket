# onarket
Onarket - Online market for selling anything

## Postman Collection
https://www.postman.com/gold-equinox-645243/workspace/project-apis/collection/10764034-030b9ff3-83ce-4e59-8b09-e7d09914efdc?action=share&creator=10764034

## Usage
1. Clone this repository
```
git clone https://github.com/ShreehariVaasishta/onarket
```
2. Go to the root directory of this project
```
cd onarket
```
3. Install the dependencies using `pip`. Activate [virtual environment](https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html) if you use one.
```
pip3 install -r requirements.txt
```
4. Start the django server 
```
./manage.py runserver
```
OR
```
python3 manage.py runserver
```
Now you should be able to access the Django app running [locally](http://127.0.0.1:8000/) at port 8000. Additionally you can specifiy the port for the django app to run in local
```
./manage.py runserver 0.0.0.0:8080
```
Now the Django app will be accessible at port 8080

## Tech Stack (Programming Language, Framework(s))
* Python
* Django
* Django Rest Framework

## Features
- [x] Seller registeration/login
- [x] Post Product Variations
- [x] Add Product categoriies
- [x] Create/List/Update Products for sellers
- [x] List Orders
- [ ] Update order status
- [x] Buyer registeration/login
- [x] List Products for buyers
- [x] Order products for buyers
- [x] Check Order status updates
- [x] List Ordered products
- [ ] Filter on product categories for buyers and sellers
- [ ] Some more info in the product variation

.... More features to be included
