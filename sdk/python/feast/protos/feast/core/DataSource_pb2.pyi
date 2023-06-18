"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import feast.core.DataFormat_pb2
import feast.core.Feature_pb2
import feast.types.Value_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class DataSource(google.protobuf.message.Message):
    """Defines a Data Source that can be used source Feature data
    Next available id: 28
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _SourceType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SourceTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SourceType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INVALID: DataSource.SourceType.ValueType = ...  # 0
        BATCH_FILE: DataSource.SourceType.ValueType = ...  # 1
        BATCH_SNOWFLAKE: DataSource.SourceType.ValueType = ...  # 8
        BATCH_BIGQUERY: DataSource.SourceType.ValueType = ...  # 2
        BATCH_REDSHIFT: DataSource.SourceType.ValueType = ...  # 5
        STREAM_KAFKA: DataSource.SourceType.ValueType = ...  # 3
        STREAM_KINESIS: DataSource.SourceType.ValueType = ...  # 4
        CUSTOM_SOURCE: DataSource.SourceType.ValueType = ...  # 6
        REQUEST_SOURCE: DataSource.SourceType.ValueType = ...  # 7
        PUSH_SOURCE: DataSource.SourceType.ValueType = ...  # 9
        BATCH_TRINO: DataSource.SourceType.ValueType = ...  # 10
        BATCH_SPARK: DataSource.SourceType.ValueType = ...  # 11
        BATCH_ATHENA: DataSource.SourceType.ValueType = ...  # 12
    class SourceType(_SourceType, metaclass=_SourceTypeEnumTypeWrapper):
        """Type of Data Source.
        Next available id: 12
        """
        pass

    INVALID: DataSource.SourceType.ValueType = ...  # 0
    BATCH_FILE: DataSource.SourceType.ValueType = ...  # 1
    BATCH_SNOWFLAKE: DataSource.SourceType.ValueType = ...  # 8
    BATCH_BIGQUERY: DataSource.SourceType.ValueType = ...  # 2
    BATCH_REDSHIFT: DataSource.SourceType.ValueType = ...  # 5
    STREAM_KAFKA: DataSource.SourceType.ValueType = ...  # 3
    STREAM_KINESIS: DataSource.SourceType.ValueType = ...  # 4
    CUSTOM_SOURCE: DataSource.SourceType.ValueType = ...  # 6
    REQUEST_SOURCE: DataSource.SourceType.ValueType = ...  # 7
    PUSH_SOURCE: DataSource.SourceType.ValueType = ...  # 9
    BATCH_TRINO: DataSource.SourceType.ValueType = ...  # 10
    BATCH_SPARK: DataSource.SourceType.ValueType = ...  # 11
    BATCH_ATHENA: DataSource.SourceType.ValueType = ...  # 12

    class TagsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class FieldMappingEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class SourceMeta(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        EARLIESTEVENTTIMESTAMP_FIELD_NUMBER: builtins.int
        LATESTEVENTTIMESTAMP_FIELD_NUMBER: builtins.int
        @property
        def earliestEventTimestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
        @property
        def latestEventTimestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
        def __init__(self,
            *,
            earliestEventTimestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
            latestEventTimestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["earliestEventTimestamp",b"earliestEventTimestamp","latestEventTimestamp",b"latestEventTimestamp"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["earliestEventTimestamp",b"earliestEventTimestamp","latestEventTimestamp",b"latestEventTimestamp"]) -> None: ...

    class FileOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from a file"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        FILE_FORMAT_FIELD_NUMBER: builtins.int
        URI_FIELD_NUMBER: builtins.int
        S3_ENDPOINT_OVERRIDE_FIELD_NUMBER: builtins.int
        @property
        def file_format(self) -> feast.core.DataFormat_pb2.FileFormat: ...
        uri: typing.Text = ...
        """Target URL of file to retrieve and source features from.
        s3://path/to/file for AWS S3 storage
        gs://path/to/file for GCP GCS storage
        file:///path/to/file for local storage
        """

        s3_endpoint_override: typing.Text = ...
        """override AWS S3 storage endpoint with custom S3 endpoint"""

        def __init__(self,
            *,
            file_format : typing.Optional[feast.core.DataFormat_pb2.FileFormat] = ...,
            uri : typing.Text = ...,
            s3_endpoint_override : typing.Text = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["file_format",b"file_format"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["file_format",b"file_format","s3_endpoint_override",b"s3_endpoint_override","uri",b"uri"]) -> None: ...

    class BigQueryOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from a BigQuery Query"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TABLE_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        table: typing.Text = ...
        """Full table reference in the form of [project:dataset.table]"""

        query: typing.Text = ...
        """SQL query that returns a table containing feature data. Must contain an event_timestamp column, and respective
        entity columns
        """

        def __init__(self,
            *,
            table : typing.Text = ...,
            query : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["query",b"query","table",b"table"]) -> None: ...

    class TrinoOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from a Trino Query"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TABLE_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        table: typing.Text = ...
        """Full table reference in the form of [project:dataset.table]"""

        query: typing.Text = ...
        """SQL query that returns a table containing feature data. Must contain an event_timestamp column, and respective
        entity columns
        """

        def __init__(self,
            *,
            table : typing.Text = ...,
            query : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["query",b"query","table",b"table"]) -> None: ...

    class KafkaOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from Kafka messages.
        Each message should be a Protobuf that can be decoded with the generated
        Java Protobuf class at the given class path
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KAFKA_BOOTSTRAP_SERVERS_FIELD_NUMBER: builtins.int
        TOPIC_FIELD_NUMBER: builtins.int
        MESSAGE_FORMAT_FIELD_NUMBER: builtins.int
        WATERMARK_DELAY_THRESHOLD_FIELD_NUMBER: builtins.int
        kafka_bootstrap_servers: typing.Text = ...
        """Comma separated list of Kafka bootstrap servers. Used for feature tables without a defined source host[:port]]"""

        topic: typing.Text = ...
        """Kafka topic to collect feature data from."""

        @property
        def message_format(self) -> feast.core.DataFormat_pb2.StreamFormat:
            """Defines the stream data format encoding feature/entity data in Kafka messages."""
            pass
        @property
        def watermark_delay_threshold(self) -> google.protobuf.duration_pb2.Duration:
            """Watermark delay threshold for stream data"""
            pass
        def __init__(self,
            *,
            kafka_bootstrap_servers : typing.Text = ...,
            topic : typing.Text = ...,
            message_format : typing.Optional[feast.core.DataFormat_pb2.StreamFormat] = ...,
            watermark_delay_threshold : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["message_format",b"message_format","watermark_delay_threshold",b"watermark_delay_threshold"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["kafka_bootstrap_servers",b"kafka_bootstrap_servers","message_format",b"message_format","topic",b"topic","watermark_delay_threshold",b"watermark_delay_threshold"]) -> None: ...

    class KinesisOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from Kinesis records.
        Each record should be a Protobuf that can be decoded with the generated
        Java Protobuf class at the given class path
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        REGION_FIELD_NUMBER: builtins.int
        STREAM_NAME_FIELD_NUMBER: builtins.int
        RECORD_FORMAT_FIELD_NUMBER: builtins.int
        region: typing.Text = ...
        """AWS region of the Kinesis stream"""

        stream_name: typing.Text = ...
        """Name of the Kinesis stream to obtain feature data from."""

        @property
        def record_format(self) -> feast.core.DataFormat_pb2.StreamFormat:
            """Defines the data format encoding the feature/entity data in Kinesis records.
            Kinesis Data Sources support Avro and Proto as data formats.
            """
            pass
        def __init__(self,
            *,
            region : typing.Text = ...,
            stream_name : typing.Text = ...,
            record_format : typing.Optional[feast.core.DataFormat_pb2.StreamFormat] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["record_format",b"record_format"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["record_format",b"record_format","region",b"region","stream_name",b"stream_name"]) -> None: ...

    class RedshiftOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from a Redshift Query"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TABLE_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        SCHEMA_FIELD_NUMBER: builtins.int
        DATABASE_FIELD_NUMBER: builtins.int
        table: typing.Text = ...
        """Redshift table name"""

        query: typing.Text = ...
        """SQL query that returns a table containing feature data. Must contain an event_timestamp column, and respective
        entity columns
        """

        schema: typing.Text = ...
        """Redshift schema name"""

        database: typing.Text = ...
        """Redshift database name"""

        def __init__(self,
            *,
            table : typing.Text = ...,
            query : typing.Text = ...,
            schema : typing.Text = ...,
            database : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["database",b"database","query",b"query","schema",b"schema","table",b"table"]) -> None: ...

    class AthenaOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from a Athena Query"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TABLE_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        DATABASE_FIELD_NUMBER: builtins.int
        DATA_SOURCE_FIELD_NUMBER: builtins.int
        table: typing.Text = ...
        """Athena table name"""

        query: typing.Text = ...
        """SQL query that returns a table containing feature data. Must contain an event_timestamp column, and respective
        entity columns
        """

        database: typing.Text = ...
        """Athena database name"""

        data_source: typing.Text = ...
        """Athena schema name"""

        def __init__(self,
            *,
            table : typing.Text = ...,
            query : typing.Text = ...,
            database : typing.Text = ...,
            data_source : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["data_source",b"data_source","database",b"database","query",b"query","table",b"table"]) -> None: ...

    class SnowflakeOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from a Snowflake Query"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TABLE_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        SCHEMA_FIELD_NUMBER: builtins.int
        DATABASE_FIELD_NUMBER: builtins.int
        table: typing.Text = ...
        """Snowflake table name"""

        query: typing.Text = ...
        """SQL query that returns a table containing feature data. Must contain an event_timestamp column, and respective
        entity columns
        """

        schema: typing.Text = ...
        """Snowflake schema name"""

        database: typing.Text = ...
        """Snowflake schema name"""

        def __init__(self,
            *,
            table : typing.Text = ...,
            query : typing.Text = ...,
            schema : typing.Text = ...,
            database : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["database",b"database","query",b"query","schema",b"schema","table",b"table"]) -> None: ...

    class SparkOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from a spark table/query"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TABLE_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        PATH_FIELD_NUMBER: builtins.int
        FILE_FORMAT_FIELD_NUMBER: builtins.int
        table: typing.Text = ...
        """Table name"""

        query: typing.Text = ...
        """Spark SQl query that returns the table, this is an alternative to `table`"""

        path: typing.Text = ...
        """Path from which spark can read the table, this is an alternative to `table`"""

        file_format: typing.Text = ...
        """Format of files at `path` (e.g. parquet, avro, etc)"""

        def __init__(self,
            *,
            table : typing.Text = ...,
            query : typing.Text = ...,
            path : typing.Text = ...,
            file_format : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["file_format",b"file_format","path",b"path","query",b"query","table",b"table"]) -> None: ...

    class CustomSourceOptions(google.protobuf.message.Message):
        """Defines configuration for custom third-party data sources."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        CONFIGURATION_FIELD_NUMBER: builtins.int
        configuration: builtins.bytes = ...
        """Serialized configuration information for the data source. The implementer of the custom data source is
        responsible for serializing and deserializing data from bytes
        """

        def __init__(self,
            *,
            configuration : builtins.bytes = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["configuration",b"configuration"]) -> None: ...

    class RequestDataOptions(google.protobuf.message.Message):
        """Defines options for DataSource that sources features from request data"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class DeprecatedSchemaEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: feast.types.Value_pb2.ValueType.Enum.ValueType = ...
            def __init__(self,
                *,
                key : typing.Text = ...,
                value : feast.types.Value_pb2.ValueType.Enum.ValueType = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        DEPRECATED_SCHEMA_FIELD_NUMBER: builtins.int
        SCHEMA_FIELD_NUMBER: builtins.int
        @property
        def deprecated_schema(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, feast.types.Value_pb2.ValueType.Enum.ValueType]:
            """Mapping of feature name to type"""
            pass
        @property
        def schema(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[feast.core.Feature_pb2.FeatureSpecV2]: ...
        def __init__(self,
            *,
            deprecated_schema : typing.Optional[typing.Mapping[typing.Text, feast.types.Value_pb2.ValueType.Enum.ValueType]] = ...,
            schema : typing.Optional[typing.Iterable[feast.core.Feature_pb2.FeatureSpecV2]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["deprecated_schema",b"deprecated_schema","schema",b"schema"]) -> None: ...

    class PushOptions(google.protobuf.message.Message):
        """Defines options for DataSource that supports pushing data to it. This allows data to be pushed to
        the online store on-demand, such as by stream consumers.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    FIELD_MAPPING_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_FIELD_NUMBER: builtins.int
    DATE_PARTITION_COLUMN_FIELD_NUMBER: builtins.int
    CREATED_TIMESTAMP_COLUMN_FIELD_NUMBER: builtins.int
    DATA_SOURCE_CLASS_TYPE_FIELD_NUMBER: builtins.int
    BATCH_SOURCE_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    FILE_OPTIONS_FIELD_NUMBER: builtins.int
    BIGQUERY_OPTIONS_FIELD_NUMBER: builtins.int
    KAFKA_OPTIONS_FIELD_NUMBER: builtins.int
    KINESIS_OPTIONS_FIELD_NUMBER: builtins.int
    REDSHIFT_OPTIONS_FIELD_NUMBER: builtins.int
    REQUEST_DATA_OPTIONS_FIELD_NUMBER: builtins.int
    CUSTOM_OPTIONS_FIELD_NUMBER: builtins.int
    SNOWFLAKE_OPTIONS_FIELD_NUMBER: builtins.int
    PUSH_OPTIONS_FIELD_NUMBER: builtins.int
    SPARK_OPTIONS_FIELD_NUMBER: builtins.int
    TRINO_OPTIONS_FIELD_NUMBER: builtins.int
    ATHENA_OPTIONS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Unique name of data source within the project"""

    project: typing.Text = ...
    """Name of Feast project that this data source belongs to."""

    description: typing.Text = ...
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    owner: typing.Text = ...
    type: global___DataSource.SourceType.ValueType = ...
    @property
    def field_mapping(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Defines mapping between fields in the sourced data
        and fields in parent FeatureTable.
        """
        pass
    timestamp_field: typing.Text = ...
    """Must specify event timestamp column name"""

    date_partition_column: typing.Text = ...
    """(Optional) Specify partition column
    useful for file sources
    """

    created_timestamp_column: typing.Text = ...
    """Must specify creation timestamp column name"""

    data_source_class_type: typing.Text = ...
    """This is an internal field that is represents the python class for the data source object a proto object represents.
    This should be set by feast, and not by users.
    The field is used primarily by custom data sources and is mandatory for them to set. Feast may set it for
    first party sources as well.
    """

    @property
    def batch_source(self) -> global___DataSource:
        """Optional batch source for streaming sources for historical features and materialization."""
        pass
    @property
    def meta(self) -> global___DataSource.SourceMeta: ...
    @property
    def file_options(self) -> global___DataSource.FileOptions: ...
    @property
    def bigquery_options(self) -> global___DataSource.BigQueryOptions: ...
    @property
    def kafka_options(self) -> global___DataSource.KafkaOptions: ...
    @property
    def kinesis_options(self) -> global___DataSource.KinesisOptions: ...
    @property
    def redshift_options(self) -> global___DataSource.RedshiftOptions: ...
    @property
    def request_data_options(self) -> global___DataSource.RequestDataOptions: ...
    @property
    def custom_options(self) -> global___DataSource.CustomSourceOptions: ...
    @property
    def snowflake_options(self) -> global___DataSource.SnowflakeOptions: ...
    @property
    def push_options(self) -> global___DataSource.PushOptions: ...
    @property
    def spark_options(self) -> global___DataSource.SparkOptions: ...
    @property
    def trino_options(self) -> global___DataSource.TrinoOptions: ...
    @property
    def athena_options(self) -> global___DataSource.AthenaOptions: ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        project : typing.Text = ...,
        description : typing.Text = ...,
        tags : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        owner : typing.Text = ...,
        type : global___DataSource.SourceType.ValueType = ...,
        field_mapping : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        timestamp_field : typing.Text = ...,
        date_partition_column : typing.Text = ...,
        created_timestamp_column : typing.Text = ...,
        data_source_class_type : typing.Text = ...,
        batch_source : typing.Optional[global___DataSource] = ...,
        meta : typing.Optional[global___DataSource.SourceMeta] = ...,
        file_options : typing.Optional[global___DataSource.FileOptions] = ...,
        bigquery_options : typing.Optional[global___DataSource.BigQueryOptions] = ...,
        kafka_options : typing.Optional[global___DataSource.KafkaOptions] = ...,
        kinesis_options : typing.Optional[global___DataSource.KinesisOptions] = ...,
        redshift_options : typing.Optional[global___DataSource.RedshiftOptions] = ...,
        request_data_options : typing.Optional[global___DataSource.RequestDataOptions] = ...,
        custom_options : typing.Optional[global___DataSource.CustomSourceOptions] = ...,
        snowflake_options : typing.Optional[global___DataSource.SnowflakeOptions] = ...,
        push_options : typing.Optional[global___DataSource.PushOptions] = ...,
        spark_options : typing.Optional[global___DataSource.SparkOptions] = ...,
        trino_options : typing.Optional[global___DataSource.TrinoOptions] = ...,
        athena_options : typing.Optional[global___DataSource.AthenaOptions] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["athena_options",b"athena_options","batch_source",b"batch_source","bigquery_options",b"bigquery_options","custom_options",b"custom_options","file_options",b"file_options","kafka_options",b"kafka_options","kinesis_options",b"kinesis_options","meta",b"meta","options",b"options","push_options",b"push_options","redshift_options",b"redshift_options","request_data_options",b"request_data_options","snowflake_options",b"snowflake_options","spark_options",b"spark_options","trino_options",b"trino_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["athena_options",b"athena_options","batch_source",b"batch_source","bigquery_options",b"bigquery_options","created_timestamp_column",b"created_timestamp_column","custom_options",b"custom_options","data_source_class_type",b"data_source_class_type","date_partition_column",b"date_partition_column","description",b"description","field_mapping",b"field_mapping","file_options",b"file_options","kafka_options",b"kafka_options","kinesis_options",b"kinesis_options","meta",b"meta","name",b"name","options",b"options","owner",b"owner","project",b"project","push_options",b"push_options","redshift_options",b"redshift_options","request_data_options",b"request_data_options","snowflake_options",b"snowflake_options","spark_options",b"spark_options","tags",b"tags","timestamp_field",b"timestamp_field","trino_options",b"trino_options","type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["options",b"options"]) -> typing.Optional[typing_extensions.Literal["file_options","bigquery_options","kafka_options","kinesis_options","redshift_options","request_data_options","custom_options","snowflake_options","push_options","spark_options","trino_options","athena_options"]]: ...
global___DataSource = DataSource
