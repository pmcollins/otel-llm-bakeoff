# LangChain Instrumentation Bakeoff

This repository compares four different approaches to instrumenting LangChain applications.

Each scenario runs the same LangChain application, but is instrumented in a unique way, defined and run via an
[oteltest](https://github.com/pmcollins/oteltest) script. These scripts have been run and their output committed to the
`json/` directory.

## Instrumentation Approaches

1. **[LangSmith](ott-langsmith.py)**
   - LangSmith is LangChain's included observability tooling
   - It appears to be derived from OpenLLMetry's instrumentor

2. **[OpenLit](ott-lit.py)**
   - OpenLit is an observability platform and instrumentation library for LLM applications

3. **[OpenLLMetry](ott-llmetry.py)**
   - OpenLLMetry is an OpenTelemetry instrumentation library for LLM applications

4. **[OpenLLMetry (Local Copy)](ott-llmetry-local.py)**
   - OpenLLMetry contains vendor-specific naming
   - This repo has a local copy that uses vendor-neutral names

## Operation

These examples have been run and their telemetry saved to this repo in the `json/` directory. However, if you want to
run them and see their telemetry:

1. `pip install oteltest`
2. `oteltest ott-example-name.py`
3. Check the `json/` directory for telemetry output
