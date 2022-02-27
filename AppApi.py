from flask import  Flask , jsonify , request

app = Flask(__name__)

tasks = [
    {
        'id' : 1,
        'title' : u'learning',
        'description': u'Mathematics',
        'done' : False
    },
    {
        'id' : 2,
        'title' : u'Practice coding',
        'description': u'At Evening',
        'done' : False
    }
]

#---------------------------------------------------------------

@app.route("/add-data" , methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message": "Please provide the data!"
        }, 400)

    task = {
        'id' : tasks[-1]['id'] + 1,
        'title' : request.json['title'],
        'description': request.json.get('description' , ""),
        'done' : False
    }

    tasks.append(task)
    return jsonify({
        "status" : "Suceess" , 
        "message": "Task Added Successfully"
    })

#---------------------------------------------------------------

@app.route("/get_data")

def get_task():
    return jsonify({
        "data" : tasks
    })

#---------------------------------------------------------------

if(__name__ == "__main__"):
    app.run(debug=True)