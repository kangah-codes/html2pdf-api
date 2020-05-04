import json
import jinja2
import pdfkit
from vars import *
import os

class PDFGen():
	def __init__(self, data):
		"""
		{
			"variables": {
				"logoUrl":"https://duckduckgo.com/assets/logo_social-media.png",
				"invoiceNo": "stf627536",
				"created":"2/2/20",
				"due":"2/122/20",
				"compAddr1": "Accra Tech",
				"compAddr2": "Osu Strees",
				"compAddr3": "Ghana",
				"receiverName": "Joshua Akangah",
				"receiverEmail": "akangah89@gmail.com",
				"paymentMtd": None,
				"paymentAcct": "0550120156",
				"items": [["Phone", "500"], ["Yess", '350']],
				"total": "850"
			},
			"filename": "yp.pdf" 	
		}
		"""
		self.data = data
		self.html = jinja2.Template(html)
		self.vars = self.data['variables']
		self.filename = self.data['filename']
		self.rendered = None

	def render_html(self):
		self.rendered = self.html.render(**self.vars)

	def save_to_pdf(self, save=False):
		try:
			if save:
				pdfkit.from_string(self.rendered, f"{self.filename}")
			else:
				return pdfkit.from_string(self.rendered, False)
		except Exception as e:
			print(e)

# b = {
# 	"variables": {
# 		"logoUrl":"https://jakangah.pythonanywhere.com/static/img/profile1.png",
# 		"invoiceNo": "stf627536",
# 		"created":"2/2/20",
# 		"due":"2/122/20",
# 		"compAddr1": "Accra Tech",
# 		"compAddr2": "Osu Strees",
# 		"compAddr3": "Ghana",
# 		"receiverName": "Joshua Akangah",
# 		"receiverEmail": "akangah89@gmail.com",
# 		"paymentMtd": "None",
# 		"paymentAcct": "0550120156",
# 		"items": [["Phone", "500"], ["Yess", "350"], ["Another one", "5000"]],"total": "850"
# 		},
# 		"filename": "ss.pdf" 
# 	}

# a = PDFGen(b)

# a.render_html()
# a.save_to_pdf(True)