# Copyright 2021-2025 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
.. autosummary::
    :toctree: _autosummary

    ModelFactory
    Model
    NamedModel
    TorchScriptModel
    TritonModel
"""

from .factory import ModelFactory
from .model import Model
from .named_model import NamedModel
from .torch_model import TorchScriptModel
from .triton_model import TritonModel, TritonRemoteModel

Model.register([TritonModel, NamedModel, TorchScriptModel, Model])
