# shop-rest-api

## Python
```
python app.py
```

## Docker

```
docker build -t shop-app .
```

```
docker run -d -p 5000:5000 shop-app
```

Teardown
Get the container id of shop-app
```
docker container ls
```

```
docker stop [container-id]
```

```
docker rm [container-id]
```


## Endpoints

- `http://0.0.0.0:5000/shopify/api/shops` : gets all shops 
- `http://0.0.0.0:5000/shopify/api/shops/<int:shop_id>` : gets shop by shop id
- `http://0.0.0.0:5000/shopify/api/products` : gets all products
- `http://0.0.0.0:5000/shopify/api/orders` : gets all orders 

## Note

I tried going backwards from setting up kubernetes and wanted to go back to refine the api but didn't end up deploying on 
kubernetes and was unable to refine api in time. There are some other attempts in the other attempts dir. 
