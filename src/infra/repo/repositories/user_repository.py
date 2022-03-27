from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.infra.repo.interfaces import UserRepositoryInterface
from src.domain.models.users import Users
from src.infra.config import DBConnectionHandler
from src.infra.repo.mapper.user_map import UsersMap

class UsersRepository(UserRepositoryInterface):

    @classmethod
    def insert(cls, name: str, password: str) -> Users:
        """Inset User
        :parm   - name: name of users
                - password: user password
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersMap(name=name, password=password)
                db_connection.session.add(new_user);
                db_connection.session.commit()

                return Users(
                    id = new_user.id,
                    name = new_user.name,
                    password = new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select(cls, user_id = None, name = None) -> List[Users]:
        """ 
        Select data in UserRepository
        :parm   - user_id: id of the user
                - password: password of the user
        """

        try:
            query_data = None

            if user_id and not name:
            
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersMap)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

            elif not user_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersMap)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif user_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersMap)
                        .filter_by(id=user_id, name=name)
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
            
    
    