import itertools, time
import string

# if char already exists in string, move to end of guess possibility
def guess_password(real):
	start_time = time.time()
	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
	attempts = 0
	for password_length in range(4, 20):
		for guess in itertools.product(chars, repeat=password_length):
			attempts += 1
			guess = ''.join(guess)
			if guess == real:
				end_time = time.time()
				diff = end_time - start_time
				return 'password is {}. found in {} guesses. took {} seconds.'.format(guess, attempts, diff)
			print(guess, end='\r')

print(guess_password('admin'))
