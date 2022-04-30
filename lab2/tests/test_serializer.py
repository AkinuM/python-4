from serializers.src.serializer import *

from serializers.json.json_serializer import JsonSerializer
from serializers.yaml.yaml_serializer import YamlSerializer
from serializers.toml.toml_serializer import TomlSerializer
import tests.test_functions as test_functions


def test_ifcbsn_types():
    i = 5
    f = 5.5
    c = complex(1, 2)
    b = True
    s = "fck"
    n = None

    assert (str(deserialize_ifcbsn(serialize_ifcbsn(i))) == str(i))
    assert (str(deserialize_ifcbsn(serialize_ifcbsn(f))) == str(f))
    assert (str(deserialize_ifcbsn(serialize_ifcbsn(c))) == str(c))
    assert (str(deserialize_ifcbsn(serialize_ifcbsn(b))) == str(b))
    assert (str(deserialize_ifcbsn(serialize_ifcbsn(s))) == str(s))
    assert (str(deserialize_ifcbsn(serialize_ifcbsn(n))) == str(n))


def test_ltsb_types():
    list1 = []
    list2 = ["a", 4, -4]
    list3 = [["4q", 78], True]

    tuple1 = ()
    tuple2 = ("a", 4, -4)
    tuple3 = (("4q", 78), True)

    set1 = ()
    set2 = ("a", 4, -4)
    set3 = (("4q", 78), True)
    bytes1 = b'bytes'

    assert (str(deserialize_ltsb(serialize_ltsb(list1))) == str(list1))
    assert (str(deserialize_ltsb(serialize_ltsb(list2))) == str(list2))
    assert (str(deserialize_ltsb(serialize_ltsb(list3))) == str(list3))
    assert (str(deserialize_ltsb(serialize_ltsb(tuple1))) == str(tuple1))
    assert (str(deserialize_ltsb(serialize_ltsb(tuple2))) == str(tuple2))
    assert (str(deserialize_ltsb(serialize_ltsb(tuple3))) == str(tuple3))
    assert (str(deserialize_ltsb(serialize_ltsb(set1))) == str(set1))
    assert (str(deserialize_ltsb(serialize_ltsb(set2))) == str(set2))
    assert (str(deserialize_ltsb(serialize_ltsb(set3))) == str(set3))
    assert (str(deserialize_ltsb(serialize_ltsb(bytes1))) == str(bytes1))


def test_dict():
    dict1 = dict()
    dict2 = {4: 7, 5: 3, 2: 1}
    dict3 = {("aaa", "bbb"): ["biba"], 32: "ABOBA"}
    dict4 = {1: dict1.copy(), 2: dict2.copy(), 3: dict3.copy()}
    dict5 = {"aa": 5}

    assert (str(dict1) == str(deserialize(serialize(dict1))))
    assert (str(dict2) == str(deserialize(serialize(dict2))))
    assert (str(dict3) == str(deserialize(serialize(dict3))))
    assert (str(dict4) == str(deserialize(serialize(dict4))))
    assert (str(dict5) == str(deserialize(serialize(dict5))))


def test_foo():
    test_functions.foo_test(deserialize, serialize)
    test_functions.foo_test(JsonSerializer.loads, JsonSerializer.dumps)
    test_functions.foo_test(YamlSerializer.loads, YamlSerializer.dumps)
    test_functions.foo_test(TomlSerializer.loads, TomlSerializer.dumps)


def test_class():
    test_functions.class_test(deserialize, serialize)
    test_functions.class_test(JsonSerializer.loads, JsonSerializer.dumps)
    test_functions.class_test(YamlSerializer.loads, YamlSerializer.dumps)
    test_functions.class_test(TomlSerializer.loads, TomlSerializer.dumps)


def test_object():
    test_functions.object_test(deserialize, serialize)
    test_functions.object_test(JsonSerializer.loads, JsonSerializer.dumps)
    test_functions.object_test(YamlSerializer.loads, YamlSerializer.dumps)
    test_functions.object_test(TomlSerializer.loads, TomlSerializer.dumps)


def test_complicated():
    test_functions.complicated_test(deserialize, serialize)
    test_functions.complicated_test(JsonSerializer.loads, JsonSerializer.dumps)
    test_functions.complicated_test(YamlSerializer.loads, YamlSerializer.dumps)
    test_functions.complicated_test(TomlSerializer.loads, TomlSerializer.dumps)


def test_lambda():
    test_functions.lambda_test(deserialize, serialize)
    test_functions.lambda_test(JsonSerializer.loads, JsonSerializer.dumps)
    test_functions.lambda_test(YamlSerializer.loads, YamlSerializer.dumps)
    test_functions.lambda_test(TomlSerializer.loads, TomlSerializer.dumps)


def test_butoma():
    test_functions.butoma_test(deserialize, serialize)
    test_functions.butoma_test(JsonSerializer.loads, JsonSerializer.dumps)
    test_functions.butoma_test(YamlSerializer.loads, YamlSerializer.dumps)
    test_functions.butoma_test(TomlSerializer.loads, TomlSerializer.dumps)
