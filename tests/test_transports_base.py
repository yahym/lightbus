import pytest

from lightbus import RedisRpcTransport, RedisResultTransport, RedisEventTransport, RedisSchemaTransport
from lightbus.config import Config
from lightbus.exceptions import TransportNotFound
from lightbus.transports.base import TransportRegistry

pytestmark = pytest.mark.unit


@pytest.fixture()
def redis_default_config():
    return Config.load_dict({
        'apis': {
            'default': {
                'rpc_transport': {'redis': {}},
                'result_transport': {'redis': {}},
                'event_transport': {'redis': {}},
                'schema_transport': {'redis': {}},
            }
        }
    })


@pytest.fixture()
def redis_other_config():
    return Config.load_dict({
        'apis': {
            'other': {
                'rpc_transport': {'redis': {}},
                'result_transport': {'redis': {}},
                'event_transport': {'redis': {}},
                'schema_transport': {'redis': {}},
            }
        }
    })


def test_transport_registry_get_does_not_exist_default():
    registry = TransportRegistry()
    with pytest.raises(TransportNotFound):
        assert not registry.get_rpc_transport('default')
    with pytest.raises(TransportNotFound):
        assert not registry.get_result_transport('default')
    with pytest.raises(TransportNotFound):
        assert not registry.get_event_transport('default')
    with pytest.raises(TransportNotFound):
        assert not registry.get_schema_transport('default')


def test_transport_registry_get_does_not_exist_default_default_value():
    registry = TransportRegistry()
    assert registry.get_rpc_transport('default', default=None) is None
    assert registry.get_result_transport('default', default=None) is None
    assert registry.get_event_transport('default', default=None) is None
    assert registry.get_schema_transport('default', default=None) is None


def test_transport_registry_get_does_not_exist_other():
    registry = TransportRegistry()
    with pytest.raises(TransportNotFound):
        assert not registry.get_rpc_transport('other')
    with pytest.raises(TransportNotFound):
        assert not registry.get_result_transport('other')
    with pytest.raises(TransportNotFound):
        assert not registry.get_event_transport('other')
    with pytest.raises(TransportNotFound):
        assert not registry.get_schema_transport('other')


def test_transport_registry_get_fallback(redis_default_config):
    registry = TransportRegistry().load_config(redis_default_config)
    assert registry.get_rpc_transport('default').__class__ == RedisRpcTransport
    assert registry.get_result_transport('default').__class__ == RedisResultTransport
    assert registry.get_event_transport('default').__class__ == RedisEventTransport
    assert registry.get_schema_transport('default').__class__ == RedisSchemaTransport


def test_transport_registry_get_specific_api(redis_other_config):
    registry = TransportRegistry().load_config(redis_other_config)
    assert registry.get_rpc_transport('other').__class__ == RedisRpcTransport
    assert registry.get_result_transport('other').__class__ == RedisResultTransport
    assert registry.get_event_transport('other').__class__ == RedisEventTransport
    assert registry.get_schema_transport('other').__class__ == RedisSchemaTransport


def test_transport_registry_load_config(redis_default_config):
    registry = TransportRegistry().load_config(redis_default_config)
    assert registry.get_rpc_transport('default').__class__ == RedisRpcTransport
    assert registry.get_result_transport('default').__class__ == RedisResultTransport
    assert registry.get_event_transport('default').__class__ == RedisEventTransport
    assert registry.get_schema_transport('default').__class__ == RedisSchemaTransport
