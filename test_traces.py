from flask import Flask
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry import trace
from opentelemetry.sdk.trace.export import (
    BatchExportSpanProcessor
)
from opentelemetry.ext.wsgi import OpenTelemetryMiddleware
from opentelemetry.exporter.opencensus.trace_exporter import (
    OpenCensusSpanExporter,
)
from opentelemetry.exporter.otlp.trace_exporter import OTLPSpanExporter


# span_exporter = OTLPSpanExporter(
#     # optional
#     # service_name="basic-service",
#     endpoint="localhost:55680",
# )
span_exporter = OpenCensusSpanExporter(
    # optional
    service_name="basic-service",
    endpoint="localhost:55678",
)

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchExportSpanProcessor(span_exporter)
)

app = Flask(__name__)
app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)


@app.route("/")
def app3():
    return "Hello from app3!"


if __name__ == "__main__":
    app.run(port=4000)