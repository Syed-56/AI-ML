from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def get_result():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4

        return redirect(url_for('success_res', score=total_score))
    return render_template('get_result.html')

@app.route('/success_res/<int:score>')
def success_res(score):
    result = "Passed" if score >= 50 else "Failed"
    exp = {'score': score, 'result': result}
    return render_template('result1.html', results=exp)

if __name__ == '__main__':
    app.run(debug=True)