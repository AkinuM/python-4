from serializers.factory import Factory


def console_utility(source_filename, output_filename, source_type, output_type):
    if source_type == output_type:
        raise ValueError(f"Source type is output type {source_type}, use different types")

    source_sd = Factory.create_serializer(source_type)
    output_sd = Factory.create_serializer(output_type)

    with open(source_filename, "r") as f:
        source = source_sd.load(f)

    with open(output_filename, "w") as f:
        output_sd.dump(source, f)
