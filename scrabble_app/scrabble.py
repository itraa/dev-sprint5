import flask, flask.views
import os
import utils

class Scrabble(flask.views.MethodView):
    
    def make_word_dict(self,l):
        scrabble_dict = {}
        for letter in l:
            if letter in scrabble_dict:
                scrabble_dict[letter] = scrabble_dict[letter] + 1
            else:
                scrabble_dict[letter] = 1
        return scrabble_dict

    def signature(self,s):
        t = list(s)
        scrabble_dict = self.make_word_dict(t)
        print scrabble_dict
        return scrabble_dict


    def all_possibilities(self,filename, scrabble_letters, min_num_letters, total_word_length):
        """
        Takes in a filename, the letters you have in your tray, the minimum number of 
        letters in your tray that you need to include in your word, and the maximum length
        of word you want.
        """
        d = []            
        for line in open(filename):
            word = line.strip().lower()
            list_word = list(word)
            word_dict = self.make_word_dict(list_word)
            for i in scrabble_letters.keys():
                if i in word_dict:
                    if word_dict[i] > 1:
                        word_dict[i] = word_dict[i]-1
                    else:
                        word_dict.pop(i)
            nums_list = word_dict.values()
            ct = 0
            for x in nums_list:
                ct = ct + x
            if (len(list_word) - ct) > min_num_letters and len(list_word) < total_word_length:
                d.append(word)
        print d
        return d


    @utils.login_required
    def get(self):
#        scrabble_letters = eval(flask.request.form['expression'])
        return flask.render_template('scrabble.html')

    @utils.login_required
    def post(self):        
        scrabble_sig = self.signature(flask.request.form['expression'])
        result = self.all_possibilities('words.txt', scrabble_sig, 5, 9)
        flask.flash("The word options are:")
        flask.flash(result)
        return flask.redirect(flask.url_for('scrabble'))