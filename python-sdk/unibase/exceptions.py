class UnibaseError(Exception):
    pass

class AuthError(UnibaseError):
    pass

class QueryError(UnibaseError):
    pass

class CollectionError(UnibaseError):
    pass

class GraphError(UnibaseError):
    pass

class NetworkError(UnibaseError):
    pass
