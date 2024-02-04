ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#list change
ft_list[1] = 'World!'

#tuple change
tuple_tmp = list(ft_tuple)
tuple_tmp[1] = 'France!'
ft_tuple = tuple_tmp

#set change
ft_set.clear()
ft_set.add('Paris!')
ft_set.add('Hello')
ft_set = sorted(ft_set)

#dict change
ft_dict.update(Hello='42Paris!')

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)