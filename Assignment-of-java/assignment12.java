// Assignment Number 12

class A {

    void show1() {
        System.out.println("It's a Super class.");
    }
}

class B extends A {

    void show2() {
        System.out.println("It's a sub class.");
    }
}

class C extends B {

    void show3() {
        System.out.println("It's a multilevel class.");
    }
}

public class Multilevel {

    public static void main(String[] args) {
        C ob = new C();
        ob.show1();
        ob.show2();
        ob.show3();
    }

}
