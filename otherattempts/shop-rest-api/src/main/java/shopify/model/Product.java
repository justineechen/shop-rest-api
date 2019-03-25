package shopify.model;

import javax.json.bind.annotation.JsonbCreator;
import javax.json.bind.annotation.JsonbProperty;
import javax.json.bind.annotation.JsonbTransient;

public class Product {
    public String name;

    public int id;

    @JsonbProperty("shop")
    public String shopName;

    // @JsonbTransient
    public float price;

    public LineItem lineitems[];

    @JsonbCreator
    public Product(
        @JsonbProperty("shop") String shopName) {
            this.name = name;
            this.id = id;
            this.shopName = shopName;
            this.price = price;
            this.lineitems = lineitems;
        }
    

}