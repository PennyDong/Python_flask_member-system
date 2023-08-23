import pymongo
from flask import *
client=pymongo.MongoClient(
    "mongodb+srv://milk:milk0000@milkteam.vyzjimd.mongodb.net/?retryWrites=true&w=majority"
)
db=client.member_system
print("資料連線成功")

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

app.secret_key="any string but sectet"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/err")
def err():
    message=request.args.get("msg","發生錯誤")
    return render_template("err.html",message=message)

@app.route("/signup", methods=["POST"])
def signup():
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]

    collection=db.member_system

    result=collection.find_one({
        "email":email
    })

    if result !=None:
        return redirect("/err?msg=信箱已被註冊過")

    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })
    
    return redirect("/index")

@app.route("/signin", methods=["POST"])
def signin():
    email=request.form["email"]
    password=request.form["password"]

    collection=db.member_system
    
    result=collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    if result==None:
        return redirect("/err?msg=帳號或密碼輸入錯誤")
app.run(port=3000)