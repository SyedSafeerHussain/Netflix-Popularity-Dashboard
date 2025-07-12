from flask import Flask,render_template
import pandas as pd
import os
BASE_DIR=os.path.abspath(os.path.dirname(__file__))
DATA_DIR=os.path.join(BASE_DIR,"..","data")

app=Flask(__name__)
@app.route("/")
def home():
    data_folder=DATA_DIR
    data=[]
    for file in os.listdir(data_folder):
        if file.endswith(".csv"):
            df=pd.read_csv(os.path.join(data_folder,file))
            category = file.replace(".csv", "").replace("_", " ").title()
            for _, row in df.iterrows():
                data.append({
                    "category": category,
                    "name": row.get("name", "N/A"),
                    "views": row.get("views", "N/A"),
                    "runtime": row.get("run_time", "N/A"),
                    "hours": row.get("hours_viewed", "N/A"),
                })
    return render_template("index.html", data=data)
if __name__=="__main__":
    print("🚀 Running Flask App...")
    app.run(debug=True)