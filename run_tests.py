from llm_orchestrator.verifier import Verifier


def test_verifier():
    verifier = Verifier(schema_dir="data/json_schemas")
