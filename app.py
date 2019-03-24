from flask import Flask, jsonify, abort

app = Flask(__name__)

shops = [
      {
        "name": "Aritzia",
        "id": 23,
        "products": [
          {
            "name": "",
            "id": "",
            "shop":"Aritzia",
            "price": {},
            "lineitems": [
              {
                "name": "",
                "id": "",
                "productName": "",
                "quantity": "",
                "price": ""
              },
              {
                "name": "",
                "id": "",
                "productName": "",
                "quantity": "",
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
                "productName": "",
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
                "productName": "",
                "quantity": "",
                "price": ""
              },
              {
                "name": "",
                "id": "",
                "productName": "",
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
            "price": {},
            "lineitems": [
              {
                "name": "",
                "id": "",
                "shop":"Haven",
                "productName": "",
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
              "productName": "",
              "quantity": "",
              "price": ""
            },
            {
              "name": "",
              "id": "",
              "productName": "",
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
    products = []
    for shop in shops:
        products.append(shop['products'])
    return jsonify({'products': products})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
