class Receipt {
    // Класс - квитанция

    private static int count = 0;
    private static final String UNKNOWN_INFORMATION = "Unknown";
    private static final int UNCOUNTED_SUM = 0;

    private String owner;
    private String date;
    private int sum;

    Receipt(String owner, String date, Integer sum) {
        this.owner = owner;
        this.date = date;
        this.sum = sum;
        count++;
    }

    Receipt() {
        this.owner = UNKNOWN_INFORMATION;
        this.date = UNKNOWN_INFORMATION;
        this.sum = UNCOUNTED_SUM;
        count++;
    }

    public String getOwner() {
        return owner;
    }

    public String getDate() {
        return date;
    }

    public int getSum() {
        return sum;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public void setSum(int sum) {
        this.sum = sum;
    }

    public void printInfo() {
        System.out.println("Получатель: " + this.owner);
        System.out.println("Дата выдачи: " + this.date);
        System.out.println("Сумма квитанции: " + this.sum);
    }

    public boolean checkIfSumGreater1000() {
        if (this.sum > 1000) {
            return true;
        }
        else {
            return false;
        }
    }

    public static void printCount() {
        System.out.println("Всего экземпляров: " + count);
    }

    }
