public class Animal {
	String sound = "Animal sound";

}


public class Cat extends Animal {

	String sound = "Meow";

	public static void main(String[] args){
		Animal a = new Cat();
		Cat c = new Cat();

		System.out.println(a.sound);
		System.out.println(c.sound);
	}
}


