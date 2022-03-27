from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.infra.repo.interfaces import ClientRepositoryInterface
from src.domain.models.clients import Clients
from src.infra.config.db_config import DBConnectionHandler
from src.infra.repo.mapper.client_map import ClientMap


class ClientRepository(ClientRepositoryInterface):

    @classmethod
    def insert(cls, name: str, user_id: int) -> Clients:
        """Inset Client
        :parm   - name: name of clients
                -user_id: id of owner (FK)
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_client = ClientMap(name=name, user_id=user_id)
                db_connection.session.add(new_client);
                db_connection.session.commit()

                return Clients(
                    id = new_client.id,
                    name = new_client.name,
                    user_id = new_client.user_id
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select(cls, client_id : int = None, name : str = None, user_id : int = None) -> List[Clients]:
        """ 
        Select data in ClientRepository
        :parm   - client_id: id of the client
                - user_id: id of the user
        """

        try:
            query_data = None

            if client_id and not name and not user_id:
            
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ClientMap)
                        .filter_by(id=client_id)
                        .one()
                    )
                    query_data = [data]

            elif not client_id and not name and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ClientMap)
                        .filter_by(user_id=user_id)
                        .one()
                    )
                    query_data = [data]
                    
            elif not client_id and name and not user_id:
    
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ClientMap)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]
            elif client_id and name and not user_id:
    
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ClientMap)
                        .filter_by(id=client_id, name=name)
                        .one()
                    )
                    query_data = [data]
                return query_data
            elif client_id and name and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ClientMap)
                        .filter_by(id=client_id, name=name, user_id=user_id)
                        .one()
                    )
                    query_data = [data]
            return query_data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
        return None
            
    
    