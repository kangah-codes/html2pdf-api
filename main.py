from vars import *
from flask import Flask, send_file, redirect, jsonify, request, url_for
from pdf import *
import os


"""
logoUrl
invoiceNo
created
due
compAddr1
compAddr2
compAddr3
receiverName
receiverEmail
paymentMtd
paymentAcct
items
total
"""

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
	return "INDEX"

@app.route('/gen_pdf', methods=["POST"])
def gen_pdf():
	posted_data = request.get_json()
	rendered = PDFGen(posted_data)
	rendered.render_html()
	filename = posted_data['filename']
	rendered.save_to_pdf(True)
	return send_file(f'{filename}')

if __name__ == "__main__":
	app.run(debug=True)