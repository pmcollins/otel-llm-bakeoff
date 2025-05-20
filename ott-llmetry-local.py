from _lib import run_langchain, OPENAI_API_KEY

if __name__ == '__main__':
    run_langchain()


class OtelTest:
    def environment_variables(self):
        return {
            "OPENAI_API_KEY": OPENAI_API_KEY
        }

    def requirements(self):
        return [
            "urllib3<2.0", "langchain", "langchain-openai", "langchain-community",
            "opentelemetry-distro[otlp]", "./openllmetry/opentelemetry-instrumentation-langchain"
        ]

    def is_http(self) -> bool:
        return False

    def wrapper_command(self) -> str:
        return "opentelemetry-instrument"

    def on_start(self):
        return None

    def on_stop(self, tel, stdout: str, stderr: str, returncode: int) -> None:
        return None
