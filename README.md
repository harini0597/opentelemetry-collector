# opentelemetry-collector

<h3> Docker image </h3>

docker run -p 55678:55678 -p 55680:55680 \
    -v /Users/hsuresh/Desktop/opentelemtry-example/Opentelemetry-collector/collector-config.yaml:/etc/otel-collector-config.yaml \
    omnition/opentelemetry-collector-contrib:latest \
    --config=/etc/otel-collector-config.yaml
    
