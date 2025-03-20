from configfacets.configuration import Configuration

config = Configuration(
    source="https://configfacets.com/apis/repos/configfacets/core-concepts/appconfigs/resources/collections/api-configurations/exec?format=json",
    source_type="url",
    apiKey="<your_api_key>",
    postBody={"facets": ["env:prod", "cluster:aws", "region:west"]},
)
config.fetch()
resp = config.get_resp()

rabbitMQHost = config.get_value("rabbitmq.host")
rabbitMQPort = config.get_value("rabbitmq.port")

print("RabbitMQ Host:{}, Port:{}".format(rabbitMQHost, rabbitMQPort))
