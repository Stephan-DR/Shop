from flask import Flask, render_template

name = None
price = None

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/nike')
def index():
    return render_template('nike.html')

@app.route('/nike/Nike Tiempo Emerald Legend 10 Pro')
def NikeTiempoEmeraldLegend10Pro():
    global name, price
    name = 'Nike Tiempo Emerald Legend 10 Pro'
    price = 16999
    return render_template('Nike Tiempo Emerald Legend 10 Pro.html')

@app.route('/nike/Nike Phantom Luna 2 Elite SE')
def NikePhantomLuna2EliteSE():
    global name, price
    name = 'Nike Phantom Luna 2 Elite SE'
    price = 29999
    return render_template('Nike Phantom Luna 2 Elite SE.html')

@app.route('/nike/Nike Superfly 9 Academy Mercurial Dream Speed')
def NikeSuperfly9AcademyMercurialDreamSpeed():
    global name, price
    name = 'Nike Superfly 9 Academy Mercurial Dream Speed'
    price = 13999
    return render_template('Nike Superfly 9 Academy Mercurial Dream Speed.html')

@app.route('/nike/Nike Phantom Luna Elite')
def NikePhantomLunaElite():
    global name, price
    name = 'Nike Phantom Luna Elite'
    price = 35999
    return render_template('Nike Phantom Luna Elite.html')

@app.route('/nike/Nike Mercurial Superfly 9')
def NikeMercurialSuperfly9():
    global name, price
    name = 'Nike Mercurial Superfly 9'
    price = 12999
    return render_template('Nike Mercurial Superfly 9.html')

@app.route('/nike/Nike Tiempo Legend 10 Pro')
def NikeTiempoLegend10Pro():
    global name, price
    name = 'Nike Tiempo Legend 10 Pro'
    price = 17999
    return render_template('Nike Tiempo Legend 10 Pro.html')


@app.route('/adidas')
def adidas():
    return render_template('adidas.html')

@app.route('/adidas/X CRAZYFAST+ FIRM GROUND CLEATS')
def XCRAZYFASTFIRMGROUNDCLEATS():
    global name, price
    name = 'X CRAZYFAST+ FIRM GROUND CLEATS'
    price = 28999
    return render_template('X CRAZYFAST+ FIRM GROUND CLEATS.html')

@app.route('/adidas/PREDATOR 24 ELITE TURF CLEATS')
def PREDATOR24ELITETURFCLEATS():
    global name, price
    name = 'PREDATOR 24 ELITE TURF CLEATS'
    price = 13999
    return render_template('PREDATOR 24 ELITE TURF CLEATS.html')

@app.route('/adidas/SAMBA CLASSIC')
def SAMBACLASSIC():
    global name, price
    name = 'SAMBA CLASSIC'
    price = 8999
    return render_template('SAMBA CLASSIC.html')

@app.route('/adidas/PREDATOR 24 LEAGUE INDOOR SHOES')
def PREDATOR24LEAGUEINDOORSHOES():
    global name, price
    name = 'PREDATOR 24 LEAGUE INDOOR SHOES'
    price = 9999
    return render_template('PREDATOR 24 LEAGUE INDOOR SHOES.html')

@app.route('/adidas/X CRAZYFAST LEAGUE FIRM GROUND CLEATS')
def XCRAZYFASTLEAGUEFIRMGROUNDCLEATS():
    global name, price
    name = 'X CRAZYFAST LEAGUE FIRM GROUND CLEATS'
    price = 7999
    return render_template('X CRAZYFAST LEAGUE FIRM GROUND CLEATS.html')

@app.route('/adidas/TOP SALA COMPETITION INDOOR SHOES')
def TOPSALACOMPETITIONINDOORSHOES():
    global name, price
    name = 'TOP SALA COMPETITION INDOOR SHOES'
    price = 7999
    return render_template('TOP SALA COMPETITION INDOOR SHOES.html')



@app.route('/puma')
def puma():
    return render_template('puma.html')

@app.route('/puma/FUTURE 7 ULTIMATE FGAG FOOTBALL BOOTS')
def FUTURE7ULTIMATEFGAGFOOTBALLBOOTS():
    global name, price
    name = 'FUTURE 7 ULTIMATE FG/AG FOOTBALL BOOTS'
    price = 23999
    return render_template('FUTURE 7 ULTIMATE FGAG FOOTBALL BOOTS.html')

@app.route('/puma/ULTRA PLAY FGAG FOOTBALL BOOTS')
def ULTRAPLAYFGAGFOOTBALLBOOTS():
    global name, price
    name = 'ULTRA PLAY FG/AG FOOTBALL BOOTS'
    price = 5999
    return render_template('ULTRA PLAY FGAG FOOTBALL BOOTS.html')

@app.route('/puma/ULTRA MATCH MXSG FOOTBALL BOOTS')
def ULTRAMATCHMXSGFOOTBALLBOOTS():
    global name, price
    name = 'ULTRA MATCH MXSG FOOTBALL BOOTS'
    price = 4999
    return render_template('ULTRA MATCH MXSG FOOTBALL BOOTS.html')

@app.route('/puma/FUTURE 7 MATCH TT FOOTBALL BOOTS')
def FUTURE7MATCHTTFOOTBALLBOOTS():
    global name, price
    name = 'FUTURE 7 MATCH TT FOOTBALL BOOTS'
    price = 8999
    return render_template('FUTURE 7 MATCH TT FOOTBALL BOOTS.html')

@app.route('/puma/ULTRA ULTIMATE FGAG FOOTBALL BOOTS')
def ULTRAULTIMATEFGAGFOOTBALLBOOTS():
    global name, price
    name = 'ULTRA ULTIMATE FGAG FOOTBALL BOOTS'
    price = 21999
    return render_template('ULTRA ULTIMATE FGAG FOOTBALL BOOTS.html')

@app.route('/puma/VITORIA TT FOOTBALL BOOTS')
def VITORIATTFOOTBALLBOOTS():
    global name, price
    name = 'VITORIA TT FOOTBALL BOOTS'
    price = 3999
    return render_template('VITORIA TT FOOTBALL BOOTS.html')


@app.route('/buy')
def buy():
    global name, price
    return render_template('buy.html', name=name, price=price)

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()