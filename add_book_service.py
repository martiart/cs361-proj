import json
import time


USER_DATA = 'data.json'
REQUEST_FILE = 'book_requests.json'


def load_accounts():
	try:
		with open(USER_DATA, 'r') as file:
			return json.load(file)
	except FileNotFoundError:
		return {'accounts': []}


def save_accounts(accounts):
	with open(USER_DATA, 'w') as file:
		json.dump(accounts, file, indent=4)


def load_request():
	try:
		with open(REQUEST_FILE, 'r') as file:
			return json.load(file)
	except FileNotFoundError:
		return {'accounts': []}


def save_requests(requests):
	with open(REQUEST_FILE, 'w') as file:
		json.dump(requests, file, indent=4)


def add_book_to_account(username, title, author, is_read_status):
	accounts = load_accounts()

	for account in accounts['accounts']:
		if account['username'] == username:
			account['books'].append({
				"title": title,
				"author": author,
				"isRead": is_read_status
			})
		else:
			account['books'] = []

		save_accounts(accounts)
		print(f"The following book was added to {username}'s account: ")
		print(f"{title} by {author} and with a read status of {is_read_status}")
	pass


def run_add_book_service():
	while True:
		print("Checking for book requests...")
		time.sleep(1)
		requests = load_request()

		if requests:
			for request in requests:
				username = request['username']
				title = request['title']
				author = request['author']
				is_read_status = request['isRead']

				add_book_to_account(username, title, author, is_read_status)

			save_requests([])


if __name__ == '__main__':
	run_add_book_service()

