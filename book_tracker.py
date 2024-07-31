import json
import time


"""Main Book Tracker Logic"""

REQUESTS_FILE = 'book_requests.json'


class BookTracker:
	def __init__(self, file_name='data.json'):
		"""
		Initialize Booktracker instance with specified json file
		:param file_name: name of json file to load
		"""
		self._filename = file_name
		self._data = self.load_data()

	def get_data(self):
		"""
		retrieve current data loaded from json file
		:return: data dictionary containing accounts and books
		"""
		return self._data

	def get_file_name(self):
		"""
		retrieve json file name
		:return: json file name as string
		"""
		return self._filename

	def load_data(self):
		"""
		load data from the specified json file. if file not found, return empty account list
		:return: dictionary containing acoutn data
		"""
		try:
			with open(self.get_file_name(), 'r') as file:
				return json.load(file)
		except FileNotFoundError:
			return {'accounts': []}

	def save_data(self):
		"""
		Saves current data back to json file
		"""
		with open(self.get_file_name(), 'w') as file:
			json.dump(self.get_data(), file, indent=4)

	def validate_user(self):
		"""
		Validates if user exists in json file.
		If name does not exist prompts user with a few options to proceed
		:return: the username if found or created, else -1
		"""
		while True:
			user_name = input("Enter your user name: ")

			# if already exists
			for account in self.get_data()['accounts']:
				if account['username'] == user_name:
					return user_name

			# else does not exist
			print("Invalid user name!")
			print()
			print("1. Enter name again")
			print("2. Create Account")
			print("3. Quit Application")

			user_choice = int(input("Enter number choice: "))
			print()
			if user_choice == 1:  # try to enter name again
				continue
			elif user_choice == 2:  # create an account
				user_name = self.create_account()
				return user_name
			elif user_choice == 3:  # quit application
				return -1

	def create_account(self):
		"""
		Prompts user to create new account. checks for existing usernames and ensure name entered correctly
		:return: name
		"""
		while True:
			user_name = input("Enter your username: ")
			retype_name = input("Re-type your username: ")

			if user_name == retype_name:
				for account in self.get_data()['accounts']:
					# user name already exists try a different name
					if account['username'] == user_name:
						print("Try a different name. Account with this name already exists.")
						continue

				new_account = {
					"username": user_name,
					"books": []
				}

				# add user to json
				self.get_data()['accounts'].append(new_account)
				self.save_data()
				print(f"Account for {user_name} has been created!")
				return user_name

	def account_management(self, user_name):
		"""
		provide account management options for user to edit user name or delete account
		:param user_name: username
		:return: updated username or -1 if deleted
		"""
		# menu prompts for account management
		print()
		print("Welcome to account management. Select from the choices below!")
		print("1. Edit username")
		print("2. Delete Account")
		print("3. Return to Main Menu")
		user_choice = int(input("Enter number option: "))

		while True:
			try:
				if user_choice == 1:  # edit name
					user_name = self.edit_user_name(user_name)
					return user_name
				elif user_choice == 2:  # delete account
					user_name = self.delete_account(user_name)
					return -1
				elif user_choice == 3:  # return to main menu
					pass
			except TypeError as e:
				print("You entered an invalid option. Try again!")

	def edit_user_name(self, user_name):
		"""
		allows user to edit usrname
		:param user_name: current username
		:return: new username if succesfully changed
		"""
		#iterate through json
		for account in self.get_data()['accounts']:
			if account['username'] == user_name:
				print()
				new_name = input("Enter your new username: ")
				retype_name = input("Re-type your new username: ")
				# make sure they type name correctly twice to avoid errors in json file
				if new_name == retype_name:
					account['username'] = new_name
					self.save_data()
					print(f"User name was changed from [{user_name}] to [{new_name}]!")
					return new_name

	def delete_account(self, user_name):
		"""
		allows user to delete their account
		:param user_name: name of user requesting delete account
		:return: -1 if the account was deleted
		"""
		print()
		# iterate through json with enumerate for index
		for i, account in enumerate(self.get_data()['accounts']):
			if account['username'] == user_name:
				while True:
					print("You are attempting to delete your account.")
					print("This will PERMANENTLY delete the account and any books associated with the account!")
					print("To delete you will be prompted to enter user name twice!")
					while True:
						choice = input("Enter 1 for DELETE prompts\n Enter 2 to return to Menu")
						if choice == str(1):
							while True:
								del_name = input("Enter your user name: ")
								retype_del_name = input("Retype your user name: ")
								if del_name == retype_del_name:
									del self.get_data()['accounts'][i]
									self.save_data()
									print("Your account was successfully deleted!")
									return -1
						elif choice == str(2):
							return
						else:
							print("Invalid option! Try again")

	def add_book(self, username):
		"""
		prompts the user to add a new book to their account. stored in seperatae json file for requests
		:param username: username of requesting add book
		"""
		# get book details
		title = input("Enter book title: ")
		author = input("Enter the books author: ")
		is_read_status = input("Have you read the book yet (yes/no)? ").strip().lower() == 'yes'

		# set up request prompt
		request = {
			"username": username,
			"title": title,
			"author": author,
			"isRead": is_read_status
		}

		# open, clear and write request to file
		try:
			with open(REQUESTS_FILE, 'r') as file:
				requests = json.load(file)
		except FileNotFoundError:
			requests = []

		requests.append(request)

		with open(REQUESTS_FILE, 'w') as file:
			json.dump(requests, file, indent=4)

		print("Request to add book has been sent!")
		print("Please wait...")
		time.sleep(5)
		return




