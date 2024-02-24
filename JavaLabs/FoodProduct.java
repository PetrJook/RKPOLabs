public class FoodProduct extends Product {

    private String expirationDate;

    FoodProduct(String name, int price, String expirationDate) {
        super(name, price);
        this. expirationDate = expirationDate;
    }

    FoodProduct() {
        super();
        this.expirationDate = "Unknown";
    }
    
    public String getExpirationDate() {
        return this.expirationDate;
    }
    
    public void setExpirationDate(String newDate) {
        this.expirationDate = newDate;
    }
    
    @Override
    public void print() {
        System.out.println("Вывод информации о товаре");
    }
    @Override
    public void getInfo() {
        System.out.println("Получение информации о товаре");
    }
    
}
