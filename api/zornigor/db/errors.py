class DbError(Exception):
    pass


class ProjectNotFound(DbError):
    pass


class InvalidState(DbError):
    pass
