from app import app, db
from app.models import Parametros

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Parametros': Parametros}

if __name__ == "__main__":
    app.run(debug=True)

