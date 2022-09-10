from ConnectionDB import Base,engine

# keterangan tabel

from schema.OauthAccessTokenMigration import Oauth
from schema.PrivilegesMigration import Privileges
from schema.UsersMigration import Users

# delete data

Oauth.metadata.drop_all(engine)
Privileges.metadata.drop_all(engine)
Users.metadata.drop_all(engine)