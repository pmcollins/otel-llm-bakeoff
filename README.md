# LangChain Instrumentation Bakeoff 🥮🍰🧁🍥

This repository compares four different approaches to instrumenting LangChain applications.

Each scenario runs the same LangChain application, but instrumented uniquely, defined and run via an
[oteltest](https://github.com/pmcollins/oteltest) script. These scripts have been run and their output committed to the
[json](json) directory.

## Instrumentation Approaches

- **🥮 LangSmith** ([`ott-langsmith.py`](ott-langsmith.py)): LangChain's included observability tooling, which appears to
  be derived from OpenLLMetry's instrumentor.
- **🍰 OpenLit** ([`ott-lit.py`](ott-lit.py)): an observability platform and instrumentation library for LLM applications.
- **🧁 OpenLLMetry** ([`ott-llmetry.py`](ott-llmetry.py)): an instrumentation library for LLM applications.
- **🍥 OpenLLMetry (Local Copy)** ([`ott-llmetry-local.py`](ott-llmetry-local.py)): a [local copy](openllmetry) of
  the `opentelemetry-instrumentation-langchain` package and its local dependencies with vendor-specific strings removed.

## Operation

To run the example scripts and see their telemetry:

1. `pip install oteltest`
2. `oteltest ott-example-name.py`
3. Check the `json/` directory for telemetry output

## Observations

* 🥮 LangSmith:
    * Telemetry looks like OpenLLMetry's.
    * No metrics, just spans (the original OpenLLMetry instrumentor sends metrics + spans).
* 🍰 OpenLit:
    * An observability platform, of which instrumentation is just a part.
    * OpenLit's packaging is monolithic, so if you `pip install openlit` you get several instrumentors and capabilities
      that are not relevant.
    * Emits vendor-neutral telemetry
* 🧁 OpenLLMetry
    * Repo contains many separate Python packages, so you can `pip install opentelemetry-instrumentation-langchain`
      separately.
    * Emits telemetry with attribute keys containing the word "traceloop".
    * OpenLLMetry has claimed the package names of upstream OTel.
* 🍥 Local copy of OpenLLMetry package(s)
    * Not many changes required to locally build a vendor-neutral package
