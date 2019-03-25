package shopify.model;

import javax.json.bind.annotation.JsonbCreator;
import javax.json.bind.annotation.JsonbProperty;
import javax.json.bind.annotation.JsonbTransient;

public class Shop {
    public String name;

    public int id;

    @JsonbTransient
    public boolean legendary = true;

    public Product products[];
    public Order orders[];
    
    @JsonbCreator
    public Shop(
        @JsonbProperty("name") String name,
        @JsonbProperty("products") Product products[],
        @JsonbProperty("orders") Order orders[]) {

        this.name = name;
        this.products = products;
        this.orders = orders;
        this.id = id;        
    }

    @Override
    public String toString() {
        return name;
    }

}
