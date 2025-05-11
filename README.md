# 🚀 OOP in Python: Superhero Class & Vehicle Polymorphism

This project demonstrates the use of **Object-Oriented Programming (OOP)** concepts in Python, including:

- **Class and Object Creation**
- **Constructors**
- **Inheritance**
- **Encapsulation**
- **Polymorphism**

---

## 🧱 Part 1: Superhero Class

The `Superhero` class represents a basic hero with a name, power, and health. It includes methods to display information and attack.

The `FlyingSuperhero` class **inherits** from `Superhero` and adds flight capability, overriding the `attack()` method to include flight speed.

### Example Features:

- Protected attribute `_power`
- Inheritance (`FlyingSuperhero` extends `Superhero`)
- Overriding methods (`attack`)
- Constructor overloading with `super()`

---

## 🎭 Part 2: Polymorphism Challenge - Vehicle Movement

This part showcases **polymorphism**, where different vehicle types implement a common `move()` method in their own unique way.

### Classes:

- `Vehicle` (base class)
- `Car` → `move()` prints `"Driving 🚗"`
- `Plane` → `move()` prints `"Flying ✈️"`
- `Boat` → `move()` prints `"Sailing ⛵"`

The vehicles are stored in a list and called in a loop to demonstrate polymorphism in action.

---

## 💻 How to Run

1. Make sure you have Python installed (`python --version`)
2. Clone the repo or copy the script
3. Run the script:


python main.py
