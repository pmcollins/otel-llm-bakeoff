# LangChain Instrumentation Bakeoff 🧁🍥🥮🍰

This repository compares four different approaches to instrumenting LangChain applications.

Each scenario runs the same LangChain application, but each is instrumented uniquely, and is run via an
[oteltest](https://github.com/pmcollins/oteltest) script. These scripts have been run and their output committed to the
[output](output) directory.

## Instrumentation Approaches

- **🧁 OpenLLMetry** ([`ott-llmetry.py`](ott-llmetry.py)): an instrumentation library for LLM applications.
- **🍥 OpenLLMetry (Local Copy)** ([`ott-llmetry-local.py`](ott-llmetry-local.py)): a [local copy](openllmetry) of
  the `opentelemetry-instrumentation-langchain` package and its local dependencies with vendor-specific strings removed.
- **🥮 LangSmith** ([`ott-langsmith.py`](ott-langsmith.py)): LangChain's included observability tooling, which appears to
  be derived from OpenLLMetry's instrumentor.
- **🍰 OpenLit** ([`ott-lit.py`](ott-lit.py)): an observability platform and instrumentation library for LLM
  applications.

## Operation

To run the example scripts and see their telemetry:

1. `pip install oteltest`
2. `oteltest ott-something.py`
3. Check the `json/` directory for telemetry output

## Observations

* 🧁 OpenLLMetry
    * Repo uses modular packaging, so you can `pip install opentelemetry-instrumentation-langchain` separately.
    * Emits telemetry with attribute keys containing the word "traceloop".
    * OpenLLMetry has claimed the package names of upstream OTel.
* 🍥 Local copy of OpenLLMetry package(s)
    * Not many changes required to locally build a vendor-neutral package.
* 🥮 LangSmith:
    * Telemetry looks like OpenLLMetry's except instead of "traceloop" in attrubute names, you get "langsmith".
    * No metrics, just spans (the original OpenLLMetry instrumentor sends metrics + spans).
* 🍰 OpenLit:
    * An observability platform, of which instrumentation is just a part.
    * OpenLit's packaging is monolithic, so if you `pip install openlit` you get several instrumentors and capabilities
      that are not relevant.
    * Emits vendor-neutral telemetry.

## Output

### LangSmith

Example LangSmith span:

```json
{
    "traceId": "5xihIcWNcs40zrIOoEF0uw==",
    "spanId": "1nksWusGpbY=",
    "parentSpanId": "7gtSEbKGKfk=",
    "name": "RunnableParallel<question>",
    "kind": "SPAN_KIND_INTERNAL",
    "startTimeUnixNano": "1747684501221924096",
    "endTimeUnixNano": "1747684501222807040",
    "attributes": [
      {
        "key": "langsmith.span.id",
        "value": {
          "stringValue": "9067e67a-c5da-4fd8-8d7d-16f34edd564c"
        }
      },
      {
        "key": "langsmith.trace.id",
        "value": {
          "stringValue": "f1c6cfef-6341-4369-a3af-e720eb6579ef"
        }
      },
      {
        "key": "langsmith.span.dotted_order",
        "value": {
          "stringValue": "20250519T195501187802Zf1c6cfef-6341-4369-a3af-e720eb6579ef.20250519T195501221924Z9067e67a-c5da-4fd8-8d7d-16f34edd564c"
        }
      },
      {
        "key": "langsmith.span.parent_id",
        "value": {
          "stringValue": "f1c6cfef-6341-4369-a3af-e720eb6579ef"
        }
      },
      {
        "key": "langsmith.span.kind",
        "value": {
          "stringValue": "chain"
        }
      },
      {
        "key": "langsmith.trace.name",
        "value": {
          "stringValue": "RunnableParallel<question>"
        }
      },
      {
        "key": "langsmith.trace.session_name",
        "value": {
          "stringValue": "my-project"
        }
      },
      {
        "key": "gen_ai.operation.name",
        "value": {
          "stringValue": "chain"
        }
      },
      {
        "key": "gen_ai.system",
        "value": {
          "stringValue": "langchain"
        }
      },
      {
        "key": "langsmith.metadata.LANGSMITH_OTEL_ENABLED",
        "value": {
          "stringValue": "true"
        }
      },
      {
        "key": "langsmith.metadata.revision_id",
        "value": {
          "stringValue": "c9d0c60-dirty"
        }
      },
      {
        "key": "langsmith.span.tags",
        "value": {
          "stringValue": "seq:step:1"
        }
      },
      {
        "key": "gen_ai.prompt",
        "value": {
          "stringValue": "{\"input\":\"What is the capital of France?\"}"
        }
      },
      {
        "key": "gen_ai.completion",
        "value": {
          "stringValue": "{\"question\":\"What is the capital of France?\"}"
        }
      }
    ],
    "status": {
      "code": "STATUS_CODE_OK"
    },
    "flags": 256
  }
```
