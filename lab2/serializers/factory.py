from serializers.json.json_serializer import JsonSerializer
from serializers.yaml.yaml_serializer import YamlSerializer
from serializers.toml.toml_serializer import TomlSerializer


class Factory:
    @staticmethod
    def create_serializer(name):
        if name == "json":
            return JsonSerializer

        if name == "yaml":
            return YamlSerializer

        if name == "toml":
            return TomlSerializer
