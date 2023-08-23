import pymongo
from flask import *
client=pymongo.MongoClient("mongodb+srv://milk:milk000000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority")
db=client.member_system
print("資料庫連線成功")

app=Flask(
	__name__,
	static_folder="public",
	static_url_path="/"
)

app.secret_key="any string but secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/err")
def err():
    message=request.args.get("msg","發生錯誤，請聯繫客服或回到上一頁")
    return render_template("err.html",message=message)


app.run(port=3000)

