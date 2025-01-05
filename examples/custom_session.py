"""
pip install kokoro-onnx soundfile

wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json
python examples/custom_session.py
"""

import soundfile as sf
from kokoro_onnx import Kokoro
from onnxruntime import InferenceSession

# See list of providers https://github.com/microsoft/onnxruntime/issues/22101#issuecomment-2357667377
session = InferenceSession("kokoro-v0_19.onnx", providers=["CPUExecutionProvider"])
kokoro = Kokoro.from_session(session, "voices.json")
samples, sample_rate = kokoro.create(
    "Hello. This audio generated by kokoro!", voice="af_sarah", speed=1.0, lang="en-us"
)
sf.write("audio.wav", samples, sample_rate)
print("Created audio.wav")
