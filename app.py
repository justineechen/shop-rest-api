from flask import Flask, jsonify, abort

app = Flask(__name__)

#SHOP 
@app.route("/shopify/api/shops", methods=['GET'])
def get_shops():
    return jsonify({'shops':shops})

@app.route("/shopify/api/shops/<int:shop_id>", methods=['GET'])
def get_shop(shop_id):
    shop = [shop for shop in shops if shop['id'] == shop_id]
    if len(shop) == 0:
        abort(404)
    return jsonify({'shop': shop[0]})


#PRODUCT
@app.route("/shopify/api/products", methods=['GET'])
def get_all_products():
    products = helper_all_products()
    return jsonify({'products': products})



#ORDER 
@app.route("/shopify/api/orders", methods=['GET'])
def get_all_orders():
    orders = helper_all_orders()
    print("ORDERS")
    print(orders)
    return jsonify({'orders': orders})

#UTIL
def helper_all_products():
    products = []
    for shop in shops:
      products = products + shop['products']
    return products

def helper_all_orders():
    orders = []
    for shop in shops:
      orders = orders + shop['orders']
    return orders

#Populate data 
def make_lineitem(name, id, quantity, price):
  lineitem = dict()
  lineitem['name'] = name
  lineitem['id'] = id
  lineitem['quantity'] = quantity
  lineitem['price'] = price
  return lineitem

def make_order(name, id, price, lineitems):
  order = dict()
  order['name'] = name
  order['id'] = id
  order['price'] = price 
  order['lineitems'] = lineitems
  return order

def make_product(name, id, price, lineitems):
  product = dict()
  product['name'] = name
  product['id'] = id
  product['price'] = price 
  product['lineitems'] = lineitems
  return product

def make_shop(name, id, products, orders):
  shop = dict()
  shop['name'] = name
  shop['id'] = id
  shop['products'] = products
  shop['orders'] = orders
  return shop

if __name__ == '__main__':
  shops = []
  lineitem_1 = make_lineitem('lineitem1', 1, 2, 2)
  lineitem_2 = make_lineitem('lineitem2', 2, 2, 2)
  lineitem_3 = make_lineitem('lineitem3', 3, 2, 2)
  lineitem_4 = make_lineitem('lineitem4', 4, 2, 2)
  lineitem_5 = make_lineitem('lineitem5', 5, 2, 2)

  lineitem_order_1 = [lineitem_1, lineitem_3, lineitem_5]
  lineitem_order_2 = [lineitem_2, lineitem_4]
  lineitem_product_1 = [lineitem_1, lineitem_2, lineitem_3]
  lineitem_product_2 = [lineitem_4, lineitem_5]

  order_1 = make_order('order1', 1, 3, lineitem_order_1)
  order_2 = make_order('order2', 2, 4, lineitem_order_2)

  product_1 = make_product('product1', 1, 4, lineitem_product_1)
  product_2 = make_product('product2', 2, 5, lineitem_product_2)

  products_1 = [product_1,product_2]
  products_2 = [product_2]

  orders_1 = [order_1, order_2]
  orders_2 = [order_1]

  shop_1 = make_shop('store1', 3, products_1, orders_1)
  shop_2 = make_shop('store2', 2, products_2, orders_2)

  shops.append(shop_1)
  shops.append(shop_2)

  app.run(debug=True,host='0.0.0.0')
