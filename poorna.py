from flask import Flask,render_template

FAI=Flask(__name__)


@FAI.route('/wish')
def wish():
    return 'hai how r u'


@FAI.route('/first')
def first():
    return render_template('first.html',name='poorna',age=21)



if __name__=='__main__':
    FAI.run(debug=True)

    