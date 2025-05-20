from _lib import run_langchain, OPENAI_API_KEY

if __name__ == '__main__':
    import openlit

    openlit.init(otlp_endpoint="http://127.0.0.1:4318")
    run_langchain()


class OtelTest:
    def requirements(self):
        return ["urllib3<2.0", "langchain", "langchain-openai", "langchain-community",
                "opentelemetry-distro[otlp]", "openlit"]

    def environment_variables(self):
        return {"OPENAI_API_KEY": OPENAI_API_KEY}

    def is_http(self) -> bool:
        return True

    def wrapper_command(self):
        return ""

    def on_start(self):
        return None

    def on_stop(self, tel, stdout: str, stderr: str, returncode: int) -> None:
        return None
