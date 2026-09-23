from app.database import engine, Base
from app import models # importar para registrar os modelos na Base

# create_all: cria as tabelas que não existem ainda
# se a tabela já existe: ela não apaga e não muda nada

Base.metadata.create_all(bind=engine)
print('Tabelas criadas')