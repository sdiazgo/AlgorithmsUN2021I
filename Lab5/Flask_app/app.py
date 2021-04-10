import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    message = ''
    if flask.request.method == 'POST':
        limite_inferior = flask.request.form['limite_inferior']
        limite_superior = flask.request.form['limite_superior']
        coeficiente = flask.request.form['coeficiente']
        n_subintervalos = flask.request.form['n_subintervalos']
        result = calc_rt(float(limite_inferior), float(limite_superior), float(coeficiente), float(n_subintervalos))
        message = 'La integral es: ' +  str(result)
    return flask.render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()


def calc_rt(li, ls, co, n):
    lim_i=li
    lim_s=ls
    coef=co
    subin=n
    dx=(lim_s-lim_i)/subin
    signo = 1
    if lim_i>lim_s:
        lim_i=ls
        lim_s=li
        dx=(lim_s-lim_i)/subin
        signo=-1
    resultado = 0
    i = lim_i
    while i < lim_s:
        resultado = resultado + dx*((((i+dx)**2)+(i**2))/2)
        i +=dx
    return coef*resultado*signo
