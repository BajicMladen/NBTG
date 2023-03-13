import functools

from django.conf import settings
from django.core.cache import cache

__all__ = ["cached", "clears_cache"]


DEFAULT_CACHE_TIMEOUT = getattr(settings, "CACHES")["default"]["TIMEOUT"]


def cached(cache_key: str, timeout: int = DEFAULT_CACHE_TIMEOUT):
    """
    A method decorator for caching the result on a specified key.

    :param cache_key: Cache key at which the value will be stored in the cache
    :param timeout: Cache timeout in seconds
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cached_data = cache.get(cache_key)
            if cached_data:
                return cached_data
            data = func(*args, **kwargs)
            cache.set(cache_key, data, timeout)
            return data

        return wrapper

    return decorator


def clears_cache(*cache_keys: str):
    """
    Clears the specified keys from cache when the decorated method is invoked.

    NOTE: This should be used sparsely, since it may reduce the cache efficiency.

    :param cache_keys: Cache keys to be removed from cache on method execution
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache.delete_many(cache_keys)
            return func(*args, **kwargs)

        return wrapper

    return decorator
