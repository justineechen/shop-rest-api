package shopify;

import java.util.List;
import java.util.stream.Collectors;

import javax.json.JsonArray;
import javax.json.JsonObject;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.core.Response;

import shopify.model.Shop;

public class Consumer {
    
    public static Shop[] consumeWithJsonb(String targetUrl) {
      Client client = ClientBuilder.newClient();

      Response response = client.target(targetUrl).request().get();
      Shop[] shops = response.readEntity(Shop[].class);

      response.close();
      client.close();

      return shops;
    }
}