from flask import Flask
from opentelemetry.ext.wsgi import OpenTelemetryMiddleware

from opentelemetry import metrics
from opentelemetry.sdk.metrics import Counter, MeterProvider
from opentelemetry.sdk.metrics.export.controller import PushController
from opentelemetry.sdk.metrics.export import ConsoleMetricsExporter
from opentelemetry.exporter.otlp.metrics_exporter import OTLPMetricsExporter



# metric_exporter = ConsoleMetricsExporter()
metric_exporter = OTLPMetricsExporter(
        endpoint="localhost:55680",

    )

metrics.set_meter_provider(MeterProvider())
meter = metrics.get_meter(__name__, True)
controller = PushController(meter, metric_exporter, 5)
staging_labels = {"environment": "staging"}
requests_counter = meter.create_metric(
    name="requests",
    description="number of requests",
    unit="1",
    value_type=int,
    metric_type=Counter,
)


app = Flask(__name__)
app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)

staging_labels = {"environment": "staging"}


@app.route("/")
def app1():
    requests_counter.add(1, staging_labels)
    return "test"


if __name__ == "__main__":
    app.run(port=5000)
