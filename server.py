from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
app =Flask(__name__)
CORS(app)
#file=template_rendered("index.html")
@app.route("/")
def home():
  return render_template("index.html")
@app.route("/run",methods=["POST"])
def run():
  try :
    data=request.get_json()
    if not data or "code" not in data:
      return jsonify({"error":"invalid request "}),400
    return jsonify({"response":f"data is required:{data['code']}"})
  except Exception as e:
    return jsonify({"error":str(e)})
if __name__=="__main__":
  app.run(host="0.0.0.0",port=5555,debug=True)