# LangChain Instrumentation Bakeoff 🧁🍥🥮🍰

This repository compares four different approaches to instrumenting LangChain applications.

Each scenario runs the same LangChain application, instrumented differently and executed with
an [oteltest](https://github.com/pmcollins/oteltest) script. The output from these runs is committed to
the [output](output) directory.

## Instrumentation Scenarios

- **🧁 OpenLLMetry** ([`ott-llmetry.py`](ott-llmetry.py)): uses the OpenLLMetry instrumentation library, unmodified.
- **🍥 OpenLLMetry (Local Copy)** ([`ott-llmetry-local.py`](ott-llmetry-local.py)): uses
  a [local copy](opentelemetry-instrumentation-langchain) of just the `opentelemetry-instrumentation-langchain` package
  with vendor-specific strings removed.
- **🥮 LangSmith** ([`ott-langsmith.py`](ott-langsmith.py)): uses LangChain's included observability tooling, which
  appears to be derived from OpenLLMetry's instrumentor.
- **🍰 OpenLit** ([`ott-lit.py`](ott-lit.py)): uses the OpenLit Python package, which is a collection of instrumentation
  libraries and other capabilities for LLM observability.

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
* 🥮 LangSmith
    * Telemetry looks like OpenLLMetry's except instead of "traceloop" in attribute names, it's "langsmith".
    * No metrics, just spans (the original OpenLLMetry instrumentor emits both).
* 🍰 OpenLit
    * An observability platform, of which instrumentation is just a part.
    * OpenLit's packaging is monolithic, so if you `pip install openlit` you get several instrumentors and capabilities
      that are not relevant.
    * Emits vendor-neutral telemetry.

## Output

The following is a summary of the telemetry emitted from the four instrumentation approaches while running the LangChain
example.

### 🧁 OpenLLMetry

#### Spans

Spans emitted and their names:

- RunnablePassthrough.task
- RunnableParallel<question>
- ChatPromptTemplate
- ChatOpenAI
- StrOutputParser
- RunnableSequence

<details>
<summary>Sample span: RunnablePassthrough.task</summary>

```json
{
  "traceId": "UAEa7zQbWN3G5seMm+30vw==",
  "spanId": "s8ogRN9WGAE=",
  "parentSpanId": "TfiyaMOi9AE=",
  "name": "RunnablePassthrough.task",
  "kind": "SPAN_KIND_INTERNAL",
  "startTimeUnixNano": "1747678317904876000",
  "endTimeUnixNano": "1747678317904942000",
  "attributes": [
    {
      "key": "traceloop.workflow.name",
      "value": {
        "stringValue": "RunnableSequence"
      }
    },
    {
      "key": "traceloop.entity.path",
      "value": {
        "stringValue": "RunnableParallel<question>"
      }
    },
    {
      "key": "traceloop.span.kind",
      "value": {
        "stringValue": "task"
      }
    },
    {
      "key": "traceloop.entity.name",
      "value": {
        "stringValue": "RunnablePassthrough"
      }
    },
    {
      "key": "traceloop.entity.input",
      "value": {
        "stringValue": "{\"inputs\": \"What is the capital of France?\", \"tags\": [\"map:key:question\"], \"metadata\": {}, \"kwargs\": {\"run_type\": null, \"name\": \"RunnablePassthrough\"}}"
      }
    },
    {
      "key": "traceloop.entity.output",
      "value": {
        "stringValue": "{\"outputs\": \"What is the capital of France?\", \"kwargs\": {\"tags\": [\"map:key:question\"]}}"
      }
    }
  ],
  "status": {},
  "flags": 256
}
```

</details> 

#### Metrics

* gen_ai.client.token.usage
* gen_ai.client.operation.duration

<details>
<summary>Sample metric: gen_ai.client.token.usage</summary>

```json
{
  "name": "gen_ai.client.token.usage",
  "description": "Measures number of input and output tokens used",
  "unit": "token",
  "histogram": {
    "dataPoints": [
      {
        "startTimeUnixNano": "1747678319396497000",
        "timeUnixNano": "1747678320469829000",
        "count": "2",
        "sum": 77.0,
        "bucketCounts": [
          "0",
          "0",
          "0",
          "0",
          "2",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0"
        ],
        "explicitBounds": [
          0.0,
          5.0,
          10.0,
          25.0,
          50.0,
          75.0,
          100.0,
          250.0,
          500.0,
          750.0,
          1000.0,
          2500.0,
          5000.0,
          7500.0,
          10000.0
        ],
        "attributes": [
          {
            "key": "gen_ai.system",
            "value": {
              "stringValue": "Langchain"
            }
          },
          {
            "key": "gen_ai.token.type",
            "value": {
              "stringValue": "input"
            }
          },
          {
            "key": "gen_ai.response.model",
            "value": {
              "stringValue": "gpt-3.5-turbo-0125"
            }
          }
        ],
        "min": 38.0,
        "max": 39.0
      },
      {
        "startTimeUnixNano": "1747678319396534000",
        "timeUnixNano": "1747678320469829000",
        "count": "2",
        "sum": 100.0,
        "bucketCounts": [
          "0",
          "0",
          "1",
          "0",
          "0",
          "0",
          "1",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0"
        ],
        "explicitBounds": [
          0.0,
          5.0,
          10.0,
          25.0,
          50.0,
          75.0,
          100.0,
          250.0,
          500.0,
          750.0,
          1000.0,
          2500.0,
          5000.0,
          7500.0,
          10000.0
        ],
        "attributes": [
          {
            "key": "gen_ai.system",
            "value": {
              "stringValue": "Langchain"
            }
          },
          {
            "key": "gen_ai.token.type",
            "value": {
              "stringValue": "output"
            }
          },
          {
            "key": "gen_ai.response.model",
            "value": {
              "stringValue": "gpt-3.5-turbo-0125"
            }
          }
        ],
        "min": 7.0,
        "max": 93.0
      }
    ],
    "aggregationTemporality": "AGGREGATION_TEMPORALITY_CUMULATIVE"
  }
}
```

</details>

### 🍥 OpenLLMetry Local

#### Spans

_Number of spans and their names are identical to OpenLLMetry._

<details>
<summary>Sample span: RunnablePassthrough.task</summary>

```json
{
  "traceId": "0hFubDClFMKaFe7TefxQOw==",
  "spanId": "xP/WJYvWM6A=",
  "parentSpanId": "/N6Yu4yu1oo=",
  "name": "RunnablePassthrough.task",
  "kind": "SPAN_KIND_INTERNAL",
  "startTimeUnixNano": "1747789955167983000",
  "endTimeUnixNano": "1747789955168048000",
  "attributes": [
    {
      "key": "workflow.name",
      "value": {
        "stringValue": "RunnableSequence"
      }
    },
    {
      "key": "entity.path",
      "value": {
        "stringValue": "RunnableParallel<question>"
      }
    },
    {
      "key": "span.kind",
      "value": {
        "stringValue": "task"
      }
    },
    {
      "key": "entity.name",
      "value": {
        "stringValue": "RunnablePassthrough"
      }
    },
    {
      "key": "entity.input",
      "value": {
        "stringValue": "{\"inputs\": \"What is the capital of France?\", \"tags\": [\"map:key:question\"], \"metadata\": {}, \"kwargs\": {\"run_type\": null, \"name\": \"RunnablePassthrough\"}}"
      }
    },
    {
      "key": "entity.output",
      "value": {
        "stringValue": "{\"outputs\": \"What is the capital of France?\", \"kwargs\": {\"tags\": [\"map:key:question\"]}}"
      }
    }
  ],
  "status": {},
  "flags": 256
}
```

</details>

#### Metrics

_Metrics are identical to OpenLLMetry's._

### 🥮 LangSmith

#### Spans

_Number of spans and their names are identical to OpenLLMetry._

<details>
<summary>Sample span</summary>

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

</details>

#### Metrics

_No metrics emitted._

### 🍰 OpenLit

#### Spans

This instrumentation emits four spans for this scenario and they all have the name `chat gpt-3.6-turbo`.

<details>
<summary>Sample span</summary>

```json
{
  "traceId": "Q9YhchNPeQvhkdqwCmaxLA==",
  "spanId": "K1hO3xWK4TI=",
  "parentSpanId": "PhwkOMkjUss=",
  "name": "chat gpt-3.5-turbo",
  "kind": "SPAN_KIND_CLIENT",
  "startTimeUnixNano": "1747330242830926000",
  "endTimeUnixNano": "1747330244009197000",
  "attributes": [
    {
      "key": "telemetry.sdk.name",
      "value": {
        "stringValue": "openlit"
      }
    },
    {
      "key": "gen_ai.operation.name",
      "value": {
        "stringValue": "chat"
      }
    },
    {
      "key": "gen_ai.system",
      "value": {
        "stringValue": "openai"
      }
    },
    {
      "key": "gen_ai.request.model",
      "value": {
        "stringValue": "gpt-3.5-turbo"
      }
    },
    {
      "key": "gen_ai.request.seed",
      "value": {
        "stringValue": ""
      }
    },
    {
      "key": "server.port",
      "value": {
        "intValue": "443"
      }
    },
    {
      "key": "gen_ai.request.frequency_penalty",
      "value": {
        "doubleValue": 0.0
      }
    },
    {
      "key": "gen_ai.request.max_tokens",
      "value": {
        "intValue": "-1"
      }
    },
    {
      "key": "gen_ai.request.presence_penalty",
      "value": {
        "doubleValue": 0.0
      }
    },
    {
      "key": "gen_ai.request.stop_sequences",
      "value": {
        "arrayValue": {}
      }
    },
    {
      "key": "gen_ai.request.temperature",
      "value": {
        "doubleValue": 1.0
      }
    },
    {
      "key": "gen_ai.request.top_p",
      "value": {
        "doubleValue": 1.0
      }
    },
    {
      "key": "gen_ai.response.id",
      "value": {
        "stringValue": "chatcmpl-BXWhn3eOVSstuEh9tl4ohhMo75pX9"
      }
    },
    {
      "key": "gen_ai.response.model",
      "value": {
        "stringValue": "gpt-3.5-turbo-0125"
      }
    },
    {
      "key": "gen_ai.usage.input_tokens",
      "value": {
        "intValue": "39"
      }
    },
    {
      "key": "gen_ai.usage.output_tokens",
      "value": {
        "intValue": "7"
      }
    },
    {
      "key": "server.address",
      "value": {
        "stringValue": "api.openai.com"
      }
    },
    {
      "key": "gen_ai.request.service_tier",
      "value": {
        "stringValue": "auto"
      }
    },
    {
      "key": "gen_ai.response.service_tier",
      "value": {
        "stringValue": "default"
      }
    },
    {
      "key": "gen_ai.response.system_fingerprint",
      "value": {
        "stringValue": "None"
      }
    },
    {
      "key": "deployment.environment",
      "value": {
        "stringValue": "default"
      }
    },
    {
      "key": "service.name",
      "value": {
        "stringValue": "default"
      }
    },
    {
      "key": "gen_ai.request.user",
      "value": {
        "stringValue": ""
      }
    },
    {
      "key": "gen_ai.request.is_stream",
      "value": {
        "boolValue": false
      }
    },
    {
      "key": "gen_ai.usage.total_tokens",
      "value": {
        "intValue": "46"
      }
    },
    {
      "key": "gen_ai.usage.cost",
      "value": {
        "doubleValue": 3e-05
      }
    },
    {
      "key": "gen_ai.server.time_to_first_token",
      "value": {
        "doubleValue": 1.172328233718872
      }
    },
    {
      "key": "gen_ai.sdk.version",
      "value": {
        "stringValue": "1.78.1"
      }
    },
    {
      "key": "gen_ai.response.finish_reasons",
      "value": {
        "arrayValue": {
          "values": [
            {
              "stringValue": "stop"
            }
          ]
        }
      }
    },
    {
      "key": "gen_ai.output.type",
      "value": {
        "stringValue": "text"
      }
    }
  ],
  "events": [
    {
      "timeUnixNano": "1747330244008622000",
      "name": "gen_ai.content.prompt",
      "attributes": [
        {
          "key": "gen_ai.prompt",
          "value": {
            "stringValue": "user: \n    You are a helpful assistant that provides clear and concise answers.\n\n    Question: What is the capital of France?\n\n    Please provide a helpful answer:\n    "
          }
        }
      ]
    },
    {
      "timeUnixNano": "1747330244008661000",
      "name": "gen_ai.content.completion",
      "attributes": [
        {
          "key": "gen_ai.completion",
          "value": {
            "stringValue": "The capital of France is Paris."
          }
        }
      ]
    }
  ],
  "status": {
    "code": "STATUS_CODE_OK"
  },
  "flags": 256
}
```

</details>

#### Metrics

- gen_ai.client.token.usage
- gen_ai.client.operation.duration
- gen_ai.server.time_to_first_token
- gen_ai.total.requests
- gen_ai.usage.output_tokens
- gen_ai.usage.input_tokens
- gen_ai.usage.cost

<details>
<summary>Sample metric</summary>

```json
{
  "name": "gen_ai.client.token.usage",
  "description": "Measures number of input and output tokens used",
  "unit": "{token}",
  "histogram": {
    "dataPoints": [
      {
        "startTimeUnixNano": "1747330244008862000",
        "timeUnixNano": "1747330245229291000",
        "count": "2",
        "sum": 194.0,
        "bucketCounts": [
          "0",
          "0",
          "0",
          "1",
          "1",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0"
        ],
        "explicitBounds": [
          1.0,
          4.0,
          16.0,
          64.0,
          256.0,
          1024.0,
          4096.0,
          16384.0,
          65536.0,
          262144.0,
          1048576.0,
          4194304.0,
          16777216.0,
          67108864.0
        ],
        "exemplars": [
          {
            "timeUnixNano": "1747330244008715000",
            "spanId": "K1hO3xWK4TI=",
            "traceId": "Q9YhchNPeQvhkdqwCmaxLA==",
            "asInt": "46"
          },
          {
            "timeUnixNano": "1747330245226707000",
            "spanId": "iFtin3dRCH4=",
            "traceId": "S9tVSDK3f2pVLj+SBSsi4Q==",
            "asInt": "148"
          }
        ],
        "attributes": [
          {
            "key": "telemetry.sdk.name",
            "value": {
              "stringValue": "openlit"
            }
          },
          {
            "key": "service.name",
            "value": {
              "stringValue": "default"
            }
          },
          {
            "key": "deployment.environment",
            "value": {
              "stringValue": "default"
            }
          },
          {
            "key": "gen_ai.operation.name",
            "value": {
              "stringValue": "chat"
            }
          },
          {
            "key": "gen_ai.system",
            "value": {
              "stringValue": "openai"
            }
          },
          {
            "key": "gen_ai.request.model",
            "value": {
              "stringValue": "gpt-3.5-turbo"
            }
          },
          {
            "key": "server.address",
            "value": {
              "stringValue": "api.openai.com"
            }
          },
          {
            "key": "server.port",
            "value": {
              "intValue": "443"
            }
          },
          {
            "key": "gen_ai.response.model",
            "value": {
              "stringValue": "gpt-3.5-turbo-0125"
            }
          }
        ],
        "min": 46.0,
        "max": 148.0
      },
      {
        "startTimeUnixNano": "1747330244009848000",
        "timeUnixNano": "1747330245229291000",
        "count": "2",
        "sum": 1319.0,
        "bucketCounts": [
          "0",
          "0",
          "0",
          "0",
          "0",
          "2",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0"
        ],
        "explicitBounds": [
          1.0,
          4.0,
          16.0,
          64.0,
          256.0,
          1024.0,
          4096.0,
          16384.0,
          65536.0,
          262144.0,
          1048576.0,
          4194304.0,
          16777216.0,
          67108864.0
        ],
        "exemplars": [
          {
            "timeUnixNano": "1747330245227781000",
            "spanId": "cqDys3pW8Ns=",
            "traceId": "S9tVSDK3f2pVLj+SBSsi4Q==",
            "asInt": "796"
          }
        ],
        "attributes": [
          {
            "key": "telemetry.sdk.name",
            "value": {
              "stringValue": "openlit"
            }
          },
          {
            "key": "service.name",
            "value": {
              "stringValue": "default"
            }
          },
          {
            "key": "deployment.environment",
            "value": {
              "stringValue": "default"
            }
          },
          {
            "key": "gen_ai.operation.name",
            "value": {
              "stringValue": "chat"
            }
          },
          {
            "key": "gen_ai.system",
            "value": {
              "stringValue": "langchain"
            }
          },
          {
            "key": "gen_ai.request.model",
            "value": {
              "stringValue": "gpt-3.5-turbo"
            }
          },
          {
            "key": "server.address",
            "value": {
              "stringValue": "NOT_FOUND"
            }
          },
          {
            "key": "server.port",
            "value": {
              "stringValue": "NOT_FOUND"
            }
          },
          {
            "key": "gen_ai.response.model",
            "value": {
              "stringValue": "gpt-3.5-turbo"
            }
          }
        ],
        "min": 523.0,
        "max": 796.0
      }
    ],
    "aggregationTemporality": "AGGREGATION_TEMPORALITY_CUMULATIVE"
  }
}
```

</details>

## Conclusions

Because LangSmith and our local copy of OpenLLMetry are both repackaged OpenLLMetry, we can say that the four options
being compared here can be reduced to two options: OpenLLMetry and OpenLit.

Comparison of major features:

**🧁 OpenLLMetry**

- ✅ Modular packaging
- ❌ Vendor-specific telemetry attributes
- ✅ High fidelity traces
- ❌ Rudimentary metrics

**🍰 OpenLit**

- ❌ Monolithic packaging
- ✅ Vendor-neutral telemetry attributes
- ❌ Rudimentary traces
- ✅ High fidelity metrics

In either case, the codebase will likely have to be forked:

- OpenLLMetry to replace vendor-specific attributes with vendor-neutral ones.
- OpenLit so customers can install just the instrumentor.

Because OpenLLMetry uses fine-grained packaging, using its Langchain intrumentor code as a starting point would be
straightforward. This has already been mostly done
[here](https://github.com/zhirafovod/opentelemetry-python-contrib/pull/1/files).
Its vendor specific attributes are easily stripped, as has been done in the
[opentelemetry-instrumentation-langchain](opentelemetry-instrumentation-langchain)
directory. The only remaining item is metrics, which are relatively simple in the case of OpenLLMetry, but OpenLit's
implementation can be used as a starting point.


