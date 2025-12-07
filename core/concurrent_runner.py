# threadpooler.py
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

_pool: Optional[ThreadPoolExecutor] = None

def get_pool(max_workers: int = 5) -> ThreadPoolExecutor:
    global _pool
    if _pool is None:
        _pool = ThreadPoolExecutor(max_workers=max_workers)
    return _pool

def shutdown_pool(wait: bool = True):
    global _pool
    if _pool:
        _pool.shutdown(wait=wait)
        _pool = None
        
# def run_with_pool(func: Callable) -> Callable:
#     """Pool with Executor Map"""
#     @functools.wraps(func)
#     def wrapper(iterable: Iterable, *, max_workers: int = 5) -> List[Any]:
#         pool = get_pool(max_workers=max_workers)
#         results = list(pool.map(func, iterable))
#         return results
#     return wrapper