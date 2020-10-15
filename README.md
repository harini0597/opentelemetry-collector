# opentelemetry-collector

<h1> Docker image <h1>
docker run -p 55678:55678 -p 55680:55680 \
    -v /Users/hsuresh/Desktop/opentelemtry-example/Opentelemetry-collector/collector-config.yaml:/etc/otel-collector-config.yaml \
    omnition/opentelemetry-collector-contrib:latest \
    --config=/etc/otel-collector-config.yaml
    
