class DbError(Exception):
    pass


class ProjectNotFound(DbError):
    pass
