from models import Pizza, Topping

t1 = Topping(name='Pepperoni')
t2 = Topping(name='Spinach')
t3 = Topping(name='Mushrooms')
t4 = Topping(name='Pineapple')
t5 = Topping(name='Olives')

t1.save()
t2.save()
t3.save()
t4.save()
t5.save()

p1 = Pizza(name="Pizza 1", size="small", quantity=3)
p1.save()
p1.toppings.add(t1, t4)