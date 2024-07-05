from flask import request


def pagination(query, schema):
    """
    Utility function to paginate SQLAlchemy queries.

    Args:
    - query: SQLAlchemy query object to paginate.
    - schema: Marshmallow schema to serialize query results.
    """

    # Parse query parameters
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)

    # Query for the specific page of data
    items = query.offset(offset).limit(limit).all()

    # Serialize data using provided schema
    serialized_data = schema.dump(items)
    total = query.count()

    return {'total': total, 'items': serialized_data}
