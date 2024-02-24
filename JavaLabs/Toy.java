public class Toy extends Product {

    private String type;

    Toy() {
        super();
        this.type = "Unknown";
    }

    Toy(String name, int price, String type) {
        super();
        this.type = type;
    }

    public String getType() {
        return this.type;
    }

    public void setType(String newType) {
        this.type = newType;
    }

    @Override
    public void print() {
        System.out.println("Вывод информации об игрушке");
    }
    @Override
    public void getInfo() {
        System.out.println("Получение информации об игрушке");
    }
}
