# public instrumentation interface for 'internally instrumented'
# implementations
def collection_adapter(collection):
    """Fetch the :class:`.CollectionAdapter` for a collection."""
    return getattr(collection, '_sa_adapter', None)
