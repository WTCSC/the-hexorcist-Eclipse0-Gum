import time
import sys

def dramatic_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def to_decimal(number_string, original_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()
    total_value = 0
    power = 0
    
    for char in number_string[::-1]:
        char_value = digits.index(char)
        total_value += char_value * (original_base ** power)
        power += 1
        
    return total_value

def from_decimal(decimal_number, target_base):
      digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      if decimal_number == 0:
          return "0"
      
      result_string = ""
      while decimal_number > 0:
          remainder = decimal_number % target_base
          decimal_number = decimal_number // target_base
          result_string = digits[remainder] + result_string
          
      return result_string
      
def main():
    dramatic_print("Hello hello, welcome to the Hexorcist. The power where amth should compel you to do better.")
    
    num_str = input("Enter the number you want to convert: ")
    original_base = int(input("Enter the number's current base (2-36): "))
    target_base = int(input("Enter the new base you wanna (2-36): "))
    
    dramatic_print("\n Alrighty! Will take a second...\n")
    decimal_value = to_decimal(num_str, original_base)
    converted_value = from_decimal(decimal_value, target_base)
    
    dramatic_print(f"'{num_str}' (Base-{original_base}) is '{converted_value}' (Base-{target_base}).")
    
if __name__ == "__main__":
    main()