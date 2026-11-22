from crud import (
    add_pairs,
    buy_shoes,
    create_user,
    delete_shoe_size,
    login,
    setup_default_data,
    show_all_shoes,
    show_sales,
    show_stock_logs,
    update_price,
)

setup_default_data()

while True:
  print("\n--- Shoes Shop Login ---")
  print("('exit' likh kar band karein)")
  username = input("Username: ")
  if username == "exit":
    break
  password = input("Password: ")

  user = login(username, password)

  if not user:
    print("Galat username ya password")

  elif user.role == "buyer":
    while True:
      print("\n[BUYER MENU]")
      print("1. Shoes Dekhein")
      print("2. Shoes Buy Karein")
      print("3. Logout")
      ch = input("Option: ")

      if ch == "1":
        show_all_shoes()
      elif ch == "2":
        size = int(input("Size (1-10): "))
        pairs = int(input("Pairs: "))
        buy_shoes(size, pairs, user.username)
      elif ch == "3":
        break

  elif user.role == "staff":
    while True:
      print("\n[STAFF MENU]")
      print("1. Shoes Dekhein")
      print("2. Stock Add Karein")
      print("3. Stock Logs Dekhein")
      print("4. Logout")
      ch = input("Option: ")

      if ch == "1":
        show_all_shoes()
      elif ch == "2":
        size = int(input("Size (1-10): "))
        pairs = int(input("Pairs: "))
        add_pairs(size, pairs, user.username)
      elif ch == "3":
        show_stock_logs()
      elif ch == "4":
        break

  elif user.role == "admin":
    while True:
      print("\n[ADMIN MENU]")
      print("1. Shoes Dekhein")
      print("2. Stock Add Karein")
      print("3. Shoes Buy")
      print("4. Price Update Karein")
      print("5. Size Delete Karein")
      print("6. Sales Dekhein")
      print("7. Stock Logs Dekhein")
      print("8. Naya User Banayein")
      print("9. Logout")
      ch = input("Option: ")

      if ch == "1":
        show_all_shoes()
      elif ch == "2":
        size = int(input("Size (1-10): "))
        pairs = int(input("Pairs: "))
        add_pairs(size, pairs, user.username)
      elif ch == "3":
        size = int(input("Size (1-10): "))
        pairs = int(input("Pairs: "))
        name = input("Buyer naam: ")
        buy_shoes(size, pairs, name)
      elif ch == "4":
        size = int(input("Size (1-10): "))
        price = int(input("Nayi price: "))
        update_price(size, price)
      elif ch == "5":
        size = int(input("Konsa size delete karna hai: "))
        delete_shoe_size(size)
      elif ch == "6":
        show_sales()
      elif ch == "7":
        show_stock_logs()
      elif ch == "8":
        uname = input("Naya username: ")
        pwd = input("Password: ")
        role = input("Role (admin/staff/buyer): ")
        create_user(uname, pwd, role)
      elif ch == "9":
        break