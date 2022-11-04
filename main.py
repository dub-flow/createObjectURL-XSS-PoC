from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/blob')
def return_files_tut():
	try:
		return send_file('blob-xss.html', mimetype="text/html", as_attachment=True)
	except Exception as e:
		return str(e)    
    
@app.route('/blob-string')
def return_files_tut2():
	try:
		return '<!DOCTYPE html><body><script>alert(\'xss via href\')</script></body>'
	except Exception as e:
		return str(e)    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
