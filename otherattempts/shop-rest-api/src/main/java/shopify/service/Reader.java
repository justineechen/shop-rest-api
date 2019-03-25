package shopify.service;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;

import javax.json.Json;
import javax.json.JsonArray;

public class Reader {

    public static JsonArray getShops() {
        final String PATH = "./../../../../../../src/resources/sad.json";
        try {
            InputStream fis;
            fis = new FileInputStream(PATH);
            return Json.createReader(fis).readArray();
        } catch (FileNotFoundException e) {
            System.err.println("File does not exist: " + PATH);
            return null;
        }
    }

}