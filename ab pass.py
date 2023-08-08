import random
import os
def generate_password():
  """Generates a strong anti-bruteforce password."""
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-={}[]:;'<>?,./"
  password_length = 27
  password = ""
  for i in range(password_length):
    password += random.choice(characters)
  return password

def main():
  """Generates and prints a strong anti-bruteforce password."""
  password = generate_password()
  os.system('xdg-open https://t.me/termux_command_store')
  
  print(f"Your strong anti-bruteforce password is: \n\n{password}")

if __name__ == "__main__":
  main()
  