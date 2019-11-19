from influxdb import InfluxDBClient
from . import config

influxdb = InfluxDBClient(
    host=config.INFLUXDB_HOST,
    port=config.INFLUXDB_PORT,
    username=config.INFLUXDB_USERNAME,
    password=config.INFLUXDB_PASSWORD,
)


def _init_database(name: str, duration: str, shard_duration: str):
    if {'name': name} in influxdb.get_list_database():
        return
    influxdb.create_database(name)
    influxdb.create_retention_policy(
        name,
        duration,
        '1',
        database=name,
        default=False,
        shard_duration=shard_duration,
    )


_init_database('stock_price_daily', 'INF', '13w')
