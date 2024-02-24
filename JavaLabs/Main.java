public class Main {
    public static void main(String[] args) {
        FoodProduct grechka = new FoodProduct("Гречка", 60, "21.01.2019");
        MilkProduct yogurt = new MilkProduct("Йогурт", 75, "17.01.2019", "ax03210x0621b");
        
        if (grechka instanceof Product) {
            System.out.println("FoodProduct - подкласс Product");
        if (yogurt instanceof FoodProduct) {
            System.out.println("MilkProduct - подкласс FoodProduct");
        }
        }

    }
}