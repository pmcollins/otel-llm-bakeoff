from _lib import run_langchain, OPENAI_API_KEY

if __name__ == '__main__':
    run_langchain()


class OtelTest:
    def environment_variables(self):
        return {
            "OPENAI_API_KEY": OPENAI_API_KEY,
            "OTEL_EXPORTER_OTLP_ENDPOINT": "http://127.0.0.1:4318",
            "LANGSMITH_OTEL_ENABLED": "true",
            "LANGCHAIN_TRACING_V2": "true",
            "LANGCHAIN_API_KEY": "dummy",
            "LANGCHAIN_PROJECT": "my-project",
        }

    def requirements(self):
        return ["urllib3<2.0", "langchain", "langchain-openai", "langchain-community",
                "opentelemetry-distro[otlp]", "langsmith[otel]"]

    def is_http(self) -> bool:
        return True

    def wrapper_command(self) -> str:
        return ""

    def on_start(self):
        return None

    def on_stop(self, tel, stdout: str, stderr: str, returncode: int) -> None:
        return None
