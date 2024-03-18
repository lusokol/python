from ft_package.utils import count_in_list
from colorama import Fore, Style

print(Fore.GREEN)
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
print(Style.RESET_ALL)
