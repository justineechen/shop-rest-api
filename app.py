from flask import Flask, jsonify, abort

app = Flask(__name__)

shops = [
      {
        "name": "Aritzia",
        "id": 23,
        "products": [
          {
            "name": "Shirt",
            "id": 1,
            "shop":"Aritzia",
            "price": 20.00,
            "lineitems": [
              {
                "name": "",
                "id": "",
                "quantity": "",
                "price": ""
              },
              {
                "name": "",
                "id": "",
                "quantity": 2,
                "price": ""
              }
            ]
          },
          {
            "name": "",
            "id": "",
            "shop":"Aritzia",
            "price": "",
            "lineitems": [
              {
                "name": "",
                "id": "",
                "quantity": "",
                "price": ""
              }
            ]
          }
        ],
        "orders": [
          {
            "name": "",
            "id": "",
            "price": "",
            "lineitems": [
              {
                "name": "",
                "id": "",
                "quantity": "",
                "price": ""
              },
              {
                "name": "",
                "id": "",
                "quantity": "",
                "price": ""
              }
            ]
          }
        ]
      },
      {
        "name": "Haven",
        "id": 22,
        "products": [
          {
            "name": "",
            "id": "",
            "price": "",
            "lineitems": [
              {
                "name": "",
                "id": "",
                "quantity": "",
                "price": ""
              }
            ]
          }
        ],
        "orders": [
          {
          "name": "",
          "id": "",
          "price": "",
          "lineitems": [
            {
                "name": "",
                "id": "",
                "quantity": "",
                "price": ""
            },
            {
                "name": "",
                "id": "",
                "quantity": "",
                "price": ""
            }
          ]
        }
      ]
    }
]

@app.route("/shopify/api/shops", methods=['GET'])
def get_shops():
    return jsonify({'shops':shops})

@app.route("/shopify/api/shops/<int:shop_id>", methods=['GET'])
def get_shop(shop_id):
    shop = [shop for shop in shops if shop['id'] == shop_id]
    if len(shop) == 0:
        abort(404)
    return jsonify({'shop': shop[0]})

@app.route("/shopify/api/products", methods=['GET'])
def get_all_products():
    products = helper_all_products()
    return jsonify({'products': products})

@app.route("/shopify/api/orders", methods=['GET'])
def get_all_orders():
    orders = helper_all_orders()
    print("ORDERS")
    print(orders)
    return jsonify({'orders': orders})

def helper_all_products():
    products = []
    for shop in shops:
      products = products + shop['products']
        # products.append(shop['products'])
    return products

def helper_all_orders():
    orders = []
    for shop in shops:
      orders = orders + shop['orders']
      # orders.append(shop['orders'])
    return orders



#Populate data 
def make_lineitem(name, id, quantity, price):
  lineitem = dict()
  lineitem["name"] = name
  lineitem["id"] = id
  lineitem["quantity"] = quantity
  lineitem["price"] = price

def make_order(name, id, price, lineitems):
  order = dict()
  order["name"] = name
  order["id"] = id
  order["price"] = price 
  lineitems["lineitems"] = lineitems

def make_product(name, id, price, lineitems):
  product = dict()
  product["name"] = name
  product["id"] = id
  product["price"] = price 
  lineitems["lineitems"] = lineitems

def make_shop():







if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
