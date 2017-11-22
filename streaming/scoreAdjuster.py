import pickle, os
import sys
sys.path.append("../")
import settings

def housemateScoreAdjuster(p_xCat, p_sentiment):
    
    if os.path.isfile('./xScores.pkl') == False: #check if pickle file exists & create if false
        createScores = open('xScores.pkl', 'wb')
        print('creating pkl file with: ', settings.X_CATEGORIES)
        pickle.dump([settings.NEG_COUNTS, settings.POS_COUNTS], createScores)
        createScores.close()
        
    if p_sentiment == 'neg':

        #retreive current scores
        currentScores = open('xScores.pkl', 'rb')
        negScores, posScores = pickle.load(currentScores)
        currentScores.close()

        #adjust values
        negScores[p_xCat] += 1

        #save new scores
        newScores = open('xScores.pkl', 'wb')
        pickle.dump([negScores, posScores], newScores)
        newScores.close()
    else:
        #retreive current scores
        currentScores = open('xScores.pkl', 'rb')
        negScores, posScores = pickle.load(currentScores)
        currentScores.close()

        #adjust values
        scores[p_xCat] += 1

        #save new scores
        newScores = open('xScores.pkl', 'wb')
        pickle.dump([negScores, posScores], newScores)
        newScores.close()