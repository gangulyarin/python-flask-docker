from flask import Flask 
app = Flask(__name__) 

@app.route('/') 
def hello(): 
	return "welcome to the flask tutorials"


if __name__ == "__main__": 
	#port = process.env.OPENSHIFT_NODEJS_PORT || 8080,
    	#ip   = process.env.IP   || process.env.OPENSHIFT_NODEJS_IP || '0.0.0.0';
	app.run(host ='0.0.0.0', port = 6020, debug = True) 

