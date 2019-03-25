package shopify.model;

import javax.json.bind.annotation.JsonbCreator;
import javax.json.bind.annotation.JsonbProperty;
import javax.json.bind.annotation.JsonbTransient;

public class Order {
    @JsonbTransient
    public String name;

    public int id;

    @JsonbTransient
    public float price;

    public LineItem lineitems[];

    @JsonbCreator
    public Order(
        @JsonbProperty("id") int id,
        @JsonbProperty("lineitems") LineItem lineitems[]) {
            this.name = name;
            this.id = id;
            this.price = price;
            this.lineitems = lineitems;
        }
    

}