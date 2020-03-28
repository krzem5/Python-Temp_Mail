import hashlib
import random
import requests



class TempMail:
	def __init__(self,d=None):
		print(requests.get(f"http://api4.temp-mail.org/request/domains/format/json/").json())
		if (d is None):
			d=random.choice(requests.get(f"http://api4.temp-mail.org/request/domains/format/json/").json())
		self.email=u"{0}{1}".format("".join([random.choice(list("abcdefghijklmnopqrstuvwxyz1234567890")) for _ in range(0,8,1)]),d)
		self.hash=hashlib.md5(self.email.encode("utf-8")).hexdigest()



	def get(self):
		return requests.get(f"https://api4.temp-mail.org/request/mail/id/{self.hash}/format/json").text



m=TempMail()
print(m.email)
print(m.get())