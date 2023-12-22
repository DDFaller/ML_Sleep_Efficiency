from models.sleep import Sleep
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.sleep import apresenta_sono

def get_sleeps(session):
  logger.warning("Realizando busca por doutores")
  doutores = session.query(Sleep).all()

  if not doutores:
      # se não há produtos cadastrados
      return {"doutores": []}, 200
  else:
      logger.debug(f"%d rodutos econtrados" % len(doutores))
      # retorna a representação de produto
      return apresenta_sono(doutores), 200