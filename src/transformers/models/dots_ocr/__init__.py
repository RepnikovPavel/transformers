from typing import TYPE_CHECKING
from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_torch_available

_import_structure = {
    "configuration_dots_ocr": ["DotsVisionConfig", "DotsOCRConfig"],
    "processing_dots_ocr": ["DotsVLProcessor"],
}

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_dots_ocr"] = ["DotsOCRForCausalLM"]
    _import_structure["modeling_dots_vision"] = ["DotsVisionTransformer"]

if TYPE_CHECKING:
    from .configuration_dots_ocr import DotsVisionConfig, DotsOCRConfig
    from .processing_dots_ocr import DotsVLProcessor
    if is_torch_available():
        from .modeling_dots_ocr import DotsOCRForCausalLM
        from .modeling_dots_vision import DotsVisionTransformer
else:
    import sys
    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)