from inference_sdk import InferenceHTTPClient


def run_model(file):
  CLIENT = InferenceHTTPClient(
      api_url="https://detect.roboflow.com",
      api_key=""
  )

  result = CLIENT.infer(file, model_id="weapon-detection-bpm40/3")

  return result