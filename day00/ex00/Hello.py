ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

print()

#list change
ft_list[1] = 'World!'

#tuple change
ft_tuple = ("Hello", "France!")

#set change

ft_set.remove("tutu!")
ft_set.add("Paris!")

#dict change
ft_dict.update(Hello='42Paris!')

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)