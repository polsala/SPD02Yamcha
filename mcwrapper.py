import time


class McWrapper:
    @staticmethod
    def generic_time_execution_check(func, *args, **kwargs):
        t0 = time.time()
        function_result = func(*args, **kwargs)
        tf = time.time()

        total_time = tf - t0

        return function_result, total_time
