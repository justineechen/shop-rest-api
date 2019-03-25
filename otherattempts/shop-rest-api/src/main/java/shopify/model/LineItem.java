package shopify.model;

import javax.json.bind.annotation.JsonbCreator;
import javax.json.bind.annotation.JsonbProperty;
import javax.json.bind.annotation.JsonbTransient;

public class LineItem {
    @JsonbTransient
    public String name;

    public String productName;

    public int id;
    
    @JsonbTransient
    public int quantity;

    @JsonbTransient
    public float price;

    @JsonbCreator
    public LineItem (
        @JsonbProperty("productName") String productName,
        @JsonbProperty("id") int id){
        this.name = name;
        this.productName = productName;
        this.id = id;
        this.quantity = quantity;
        this.price = price;
    }

    public String getName(){
        return name;
    }

    public int getId(){
        return id;
    }

    public int getQuantity(){
        return quantity;
    }

    // public int getPrice(){
    //     return price;
    // }
}
