import os
import subprocess

def test_api_key_exists():
    api_key = os.getenv("OPENAI_API_KEY")
    assert api_key is not None, "OPENAI_API_KEY is missing"

def test_docker_build():
    result = subprocess.run(
        ["docker", "build", "-t", "nasa-ai-test", "."],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Docker build failed:\n{result.stdout}\n{result.stderr}"

def test_docker_run():
    api_key = os.getenv("OPENAI_API_KEY")
    result = subprocess.run(
        ["docker", "run", "-e", f"OPENAI_API_KEY={api_key}", "nasa-ai-test"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Docker run failed:\n{result.stdout}\n{result.stderr}"
    assert "AI Response" in result.stdout, "Expected AI output not found"
