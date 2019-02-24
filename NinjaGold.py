from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'golds'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    if 'total' not in session:
        session['total'] = 0
    print("Session Count: ",session['count'])
    return render_template('index.html')

@app.route('/restart', methods=['GET'])
def startAgain():
    session.clear()
    return redirect('/')

@app.route('/farmRand', methods=['POST'])
def farmGuess():
    import random
    session['farmX'] = random.randrange(10, 21)
    print("You earned: ",session['farmX']," golds.")
    session['count'] = session['count'] + session['farmX']
    return redirect('/process_money')

@app.route('/caveRand', methods=['POST'])
def caveGuess():
    import random
    session['caveX'] = random.randrange(5, 11)
    print("You earned: ",session['caveX']," golds.")
    session['count'] = session['count'] + session['caveX']
    return redirect('/process_money')

@app.route('/houseRand', methods=['POST'])
def houseGuess():
    import random
    session['houseX'] = random.randrange(2, 6)
    print("You earned: ",session['houseX']," golds.")
    session['count'] = session['count'] + session['houseX']
    return redirect('/process_money')

@app.route('/casinoRand', methods=['POST'])
def casinoGuess():
    import random
    session['casinoX'] = random.randrange(-50, 51)
    print("You earned: ",session['casinoX']," golds.")
    session['count'] = session['count'] + session['casinoX']
    return redirect('/process_money')

@app.route('/process_money')
def processing():
    if 'farmX' not in session:
        session['farmX'] = 0
    if 'caveX' not in session:
        session['caveX'] = 0
    if 'houseX' not in session:
        session['houseX'] = 0
    if 'casinoX' not in session:
        session['casinoX'] = 0
    session['total'] = session['farmX'] + session['caveX'] + session['houseX'] + session['casinoX']
    if session['total'] > 0:
        session['color'] = 'green'
    if session['total'] < 0:
        session['color'] = 'red'
    session['y'] = ("You earned: ",session['total']," golds.")
    if 'activityList' not in session:
        session['activityList'] = []
    session['activityList'].append(session['y'])
    session['b'] = len(session['activityList'])
    if 'a' not in session:
        session['a'] = 0
    session['z'] = session['activityList'][session['a']]
    session['a'] = session['a'] + 1
    session['farmX'] = 0
    session['caveX'] = 0
    session['houseX'] = 0
    session['casinoX'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 