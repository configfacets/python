# Configfacets - https://configfacets.com

## Empower teams with configurations built for collaboration

One platform, endless possibilities: Streamline application and deployment configurations, Infrastructure as Code (IaC), agentic prompts, feature flags, and more.

## Configfacets python client library

### Usage

```
pip install configfacets==0.0.1
```

```
from configfacets.configuration import Configuration

config = Configuration(
    apiUrl="https://configfacets.com/apis/repos/configfacets/core-concepts/applications-0.0.1/resources/collections/api-configurations/exec?format=json",
    apiKey="<your_api_key>",
    postBody={"facets": ["env:prod", "cluster:aws", "region:east"]},
)
config.fetch()
resp = config.get_resp()

rabbitMQHost = config.get_value("rabbitmq.host")
rabbitMQPort = config.get_value("rabbitmq.port")

print("RabbitMQ Host:{}, Port:{}".format(rabbitMQHost, rabbitMQPort))


```
