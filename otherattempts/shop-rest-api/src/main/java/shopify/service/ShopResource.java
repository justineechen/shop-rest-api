package shopify.service;
import java.io.*;
import javax.json.JsonArray;
import javax.json.bind.Jsonb;
import javax.json.bind.JsonbBuilder;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.UriInfo;

import shopify.model.Shop;
import shopify.Consumer;

@Path("shops")
public class ShopResource {
    @Context
    UriInfo uriInfo;


    @GET    
    @Produces(MediaType.APPLICATION_JSON)
    public JsonArray getShops() {
    	return Reader.getShops();
    }

    @GET
    @Path("jsonString")
    @Produces(MediaType.TEXT_PLAIN)
    public String getJsonString() {
      Jsonb jsonb = JsonbBuilder.create();

      Shop[] shops = Consumer.consumeWithJsonb(uriInfo.getBaseUri().toString() +
        "shops");
      String result = jsonb.toJson(shops);

      return result;
    }

    @GET
    @Path("total/{shop}")
    @Produces(MediaType.TEXT_PLAIN)
    public int getTotalProducts(@PathParam("shop") String shop) {
      Shop[] shops = Consumer.consumeWithJsonb(uriInfo.getBaseUri().toString()
        + "shops");

      for (int i = 0; i < shops.length; i++) {
        if (shops[i].name.equals(shop)) {
          return shops[i].products.length;
        }
      }
      return -1;
    }

    // @GET
    // @Path("total/{shop}")
    // @Produces(MediaType.TEXT_PLAIN)
    // public int getTotalShops(@PathParam("shop") String shop) {
    //   Shop[] shops = Consumer.consumeWithJsonb(uriInfo.getBaseUri().toString()
    //     + "shops");
    // System.out.println(uriInfo.getBaseUri().toString() + "shops");
    // return 1;
    //   return shops.length;


    //   for (int i = 0; i < shops.length; i++) {
    //     if (products[i].name.equals(product)) {
    //       return products[i].shops.length;
    //     }
    //   }
    //   return -1;
    // }
}
