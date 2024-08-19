class PlaybookEngineException(Exception):
    """Base exception for PlaybookEngine"""
    pass

class NLQEngineException(PlaybookEngineException):
    """Raised when there's an error with the NLQ engine"""
    pass

class QueryExecutionException(PlaybookEngineException):
    """Raised when there's an error executing a query"""
    pass

