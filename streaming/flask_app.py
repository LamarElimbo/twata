from flask import Flask, request, render_template, make_response
from io import StringIO
import urllib
import pickle, os, getGraphScript
import sys
sys.path.append("../")
import settings
import datetime

app = Flask(__name__)
requiredInfo=[]

@app.route('/')
def graphIt():
    if os.path.isfile('../sentimentClassifier/housemateScores.pkl') == False: #check if pickle file exists & create if false
        createScores = open('housemateScores.pkl', 'wb')
        print('creating pkl file with: ', settings.CONTESTANTS)
        pickle.dump(settings.CONTESTANTS, createScores)
        createScores.close()
        
    graphNegScript = getGraphScript.getNegScript()
    graphPosScript = getGraphScript.getPosScript()

    currentDate = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    return render_template('graph.html', 
                           css_source='static/app.css',
                           date=currentDate, 
                           graph_neg_script=graphNegScript, 
                           graph_pos_script=graphPosScript)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)