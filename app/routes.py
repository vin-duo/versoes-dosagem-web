from flask import render_template, session, request, url_for, flash, redirect
from app import app, db
from app.forms import Dosagem, Piloto
from app.models import Parametros, Padrao

from app.MAIN_dosagem import Ensaio


#   TENTANDO REINICIAR O db:
#https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date



@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    welcome = 'Bem vindo à nossa página!!'
    return render_template('home.html', title='Home', welcome=welcome)



@app.route('/dosagem', methods = ['GET', 'POST'])
def dosagem():
    form = Dosagem()
    if form.validate_on_submit():

        add_no_db = Padrao(
            piloto = form.piloto.data,
            rico = form.rico.data,
            pobre = form.pobre.data,
            cp = form.cp.data,
            pesobrita = form.pesobrita.data,
            slump = form.slump.data)
        
        db.session.add(add_no_db)
        db.session.commit()
        print(add_no_db)

        m_piloto = form.piloto.data
        flash('Enviado!')
        return redirect('/piloto')
    padrao_salvos = Padrao.query.all()
    return render_template('dosagem.html', title='tela do ensaio', form=form, padrao_salvos=padrao_salvos)


@app.route('/dosagem/<int:id>')
def deletar(id):
    apagar = Padrao.query.get_or_404(id)

    try:
        db.session.delete(apagar)
        db.session.commit()
        return redirect('/dosagem')

    except:
        "DEU ERRADO"


@app.route('/piloto', methods = ['GET', 'POST'])
def traco_piloto():
    form = Piloto()
    valores_dosagem = Padrao.query.first()
    valores_alfa_salvos = Parametros.query.all()    
    print(valores_alfa_salvos)

    if form.validate_on_submit():
        linhas_do_db = Parametros.query.all()
        lista_de_alfas = [0]
        for i in linhas_do_db:
            lista_de_alfas.append(i.alfa)
        
        traco = Ensaio(
            m = valores_dosagem.piloto,
            cp = valores_dosagem.cp,
            alfa = form.argamassa.data, 
            pesobrita = valores_dosagem.pesobrita,
            alfaantigo = lista_de_alfas[-1])


        add_no_db = Parametros(
            alfa = form.argamassa.data,
            c_unitario = traco.massas_unitarias()[0],
            a_unitario = traco.massas_unitarias()[1],
            b_unitario = traco.massas_unitarias()[2],
            
            c_massa = traco.massas_iniciais()[0],
            a_massa = traco.massas_iniciais()[1],
            b_massa = traco.massas_iniciais()[2],
            
            c_acr = traco.quantidades_adicionar()[0],
            a_acr = traco.quantidades_adicionar()[1],
            
            agua = 0)


        db.session.add(add_no_db)
        db.session.commit()
        
        return redirect('/piloto')
        





#    alfa_ideal = float(request.form.get("alfa_ideal"))
    alfa_ideal = 0
    rico = Ensaio(
        m = valores_dosagem.rico,
        cp = valores_dosagem.cp,
        alfa = alfa_ideal,
        pesobrita = valores_dosagem.pesobrita,
        alfaantigo = 0)


    traco_rico = Parametros(
        alfa = alfa_ideal,
        c_unitario = rico.massas_unitarias()[0],
        a_unitario = rico.massas_unitarias()[1],
        b_unitario = rico.massas_unitarias()[2],
        
        c_massa = rico.massas_iniciais()[0],
        a_massa = rico.massas_iniciais()[1],
        b_massa = rico.massas_iniciais()[2],
        
        c_acr = rico.quantidades_adicionar()[0],
        a_acr = rico.quantidades_adicionar()[1],)




    pobre = Ensaio(
        m = valores_dosagem.pobre,
        cp = valores_dosagem.cp,
        alfa = alfa_ideal,
        pesobrita = valores_dosagem.pesobrita,
        alfaantigo = 0)


    traco_pobre = Parametros(
        alfa = alfa_ideal,
        c_unitario = pobre.massas_unitarias()[0],
        a_unitario = pobre.massas_unitarias()[1],
        b_unitario = pobre.massas_unitarias()[2],
        
        c_massa = pobre.massas_iniciais()[0],
        a_massa = pobre.massas_iniciais()[1],
        b_massa = pobre.massas_iniciais()[2],
        
        c_acr = pobre.quantidades_adicionar()[0],
        a_acr = pobre.quantidades_adicionar()[1],)        


    return render_template('piloto.html', title='tela do ensaio',traco_pobre=traco_pobre,traco_rico=traco_rico, alfa_ideal=alfa_ideal, form=form, valores_alfa_salvos=valores_alfa_salvos, valores_dosagem=valores_dosagem)


@app.route("/agua", methods=["POST"])
def update_agua():#o nome "valor_alfa" é o nome dado no html para um elemento na tabela do db. Quando cria uma linha no db, a tabela chama essa linha de "valor_alfa", que tem as propriedades "id", "alfa", "agua"......
    valor_alfa_id = request.form.get("valor_alfa_id")
    valor_agua_novo = request.form.get("valor_agua_novo")
    nova_agua = Parametros.query.filter_by(id=valor_alfa_id).first()
    nova_agua.agua = valor_agua_novo
    db.session.commit()
    return redirect("/piloto")



@app.route('/piloto/<int:id>')
def delete(id):
    alfa_delete = Parametros.query.get_or_404(id)

    try:
        db.session.delete(alfa_delete)
        db.session.commit()
        return redirect('/piloto')

    except:
        "DEU ERRADO"










'''

@app.route('/auxiliar', methods=["POST"])
def tracos_auxiliares():
    alfa_ideal = float(request.form.get("alfa_ideal"))
    print(alfa_ideal)
    #armazenar no db
    valores_dosagem = Padrao.query.first()
    print(valores_dosagem)
    
    rico = Ensaio(
        m = valores_dosagem.rico,
        cp = valores_dosagem.cp,
        alfa = alfa_ideal,
        pesobrita = valores_dosagem.pesobrita,
        alfaantigo = 0)


    traco_rico = Parametros(
        alfa = alfa_ideal,
        c_unitario = rico.massas_unitarias()[0],
        a_unitario = rico.massas_unitarias()[1],
        b_unitario = rico.massas_unitarias()[2],
        
        c_massa = rico.massas_iniciais()[0],
        a_massa = rico.massas_iniciais()[1],
        b_massa = rico.massas_iniciais()[2],
        
        c_acr = rico.quantidades_adicionar()[0],
        a_acr = rico.quantidades_adicionar()[1],)




    pobre = Ensaio(
        m = valores_dosagem.pobre,
        cp = valores_dosagem.cp,
        alfa = alfa_ideal,
        pesobrita = valores_dosagem.pesobrita,
        alfaantigo = 0)


    traco_pobre = Parametros(
        alfa = alfa_ideal,
        c_unitario = pobre.massas_unitarias()[0],
        a_unitario = pobre.massas_unitarias()[1],
        b_unitario = pobre.massas_unitarias()[2],
        
        c_massa = pobre.massas_iniciais()[0],
        a_massa = pobre.massas_iniciais()[1],
        b_massa = pobre.massas_iniciais()[2],
        
        c_acr = pobre.quantidades_adicionar()[0],
        a_acr = pobre.quantidades_adicionar()[1],)


    
    return render_template('auxiliar.html', title='tela do ensaio', alfa_ideal=alfa_ideal, valores_dosagem=valores_dosagem, traco_rico=traco_rico, traco_pobre=traco_pobre)

'''






@app.route('/resultados')
def results():
    welcome = 'Bem vindo à nossa página!!'
    return render_template('resultados.html', title='Home')










'''

@app.route('/rico', methods = ['GET', 'POST'])
def traco_rico():
    form = Piloto()
    return render_template('rico.html', title='tela do ensaio', form=form)

@app.route('/pobre', methods = ['GET', 'POST'])
def traco_pobre():
    form = Piloto()
    return render_template('pobre.html', title='tela do ensaio', form=form)

'''









#FORMULARIOS PARA ATUALIZAR OS VALORES DE AGUA
#https://stackoverflow.com/questions/60934135/python-editable-table-with-flask-and-jinja

@app.route('/controle', methods = ['GET', 'POST'])
def controle():
    titulo = "fodase o titulo"
    return render_template('controle.html',title='testes apenas', titulo=titulo)





