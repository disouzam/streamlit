# Copyright 2018-2021 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import contextlib
from typing import Iterator

from . import memo_decorator
from . import singleton_decorator


def maybe_show_cached_st_function_warning(dg, st_func_name: str) -> None:
    memo_decorator.maybe_show_cached_st_function_warning(dg, st_func_name)
    singleton_decorator.maybe_show_cached_st_function_warning(dg, st_func_name)


@contextlib.contextmanager
def suppress_cached_st_function_warning() -> Iterator[None]:
    with memo_decorator.suppress_cached_st_function_warning():
        with singleton_decorator.suppress_cached_st_function_warning():
            yield


# Explicitly export `memo` and `singleton`
from .memo_decorator import memo as memo
from .singleton_decorator import singleton as singleton