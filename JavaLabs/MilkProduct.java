public class MilkProduct extends FoodProduct {

    private String producerCode;

    MilkProduct() {
      super();
      producerCode = "Unknown";  
    }

    MilkProduct(String name, int price, String expirationDate, String producerCode) {
        super();
        this.producerCode = producerCode;
    }

    public String getProducerCode() {
        return this.producerCode;
    }

    public void setProducerCode(String newCode) {
        this.producerCode = newCode;
    }

    @Override
    public void print() {
        System.out.println("Вывод информации о молочном продукте");
    }
    @Override
    public void getInfo() {
        System.out.println("Получение информации о молочном продукте");
    }
    
}
