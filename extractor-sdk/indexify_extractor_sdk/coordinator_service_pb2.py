# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coordinator_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19\x63oordinator_service.proto\x12\x14indexify_coordinator"1\n\x19GetContentMetadataRequest\x12\x14\n\x0c\x63ontent_list\x18\x01 \x03(\t"Y\n\x1aGetContentMetadataResponse\x12;\n\x0c\x63ontent_list\x18\x01 \x03(\x0b\x32%.indexify_coordinator.ContentMetadata"\xaa\x01\n\x11UpdateTaskRequest\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x32\n\x07outcome\x18\x03 \x01(\x0e\x32!.indexify_coordinator.TaskOutcome\x12;\n\x0c\x63ontent_list\x18\x04 \x03(\x0b\x32%.indexify_coordinator.ContentMetadata"\x19\n\x17ListStateChangesRequest"k\n\x0bStateChange\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tobject_id\x18\x02 \x01(\t\x12\x13\n\x0b\x63hange_type\x18\x03 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\x04\x12\x14\n\x0cprocessed_at\x18\x05 \x01(\x04"N\n\x18ListStateChangesResponse\x12\x32\n\x07\x63hanges\x18\x01 \x03(\x0b\x32!.indexify_coordinator.StateChange"@\n\x10ListTasksRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x19\n\x11\x65xtraction_policy\x18\x02 \x01(\t">\n\x11ListTasksResponse\x12)\n\x05tasks\x18\x01 \x03(\x0b\x32\x1a.indexify_coordinator.Task"\x14\n\x12UpdateTaskResponse"3\n\x1eGetExtractorCoordinatesRequest\x12\x11\n\textractor\x18\x02 \x01(\t"0\n\x1fGetExtractorCoordinatesResponse\x12\r\n\x05\x61\x64\x64rs\x18\x01 \x03(\t"\'\n\x12ListIndexesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t"C\n\x13ListIndexesResponse\x12,\n\x07indexes\x18\x01 \x03(\x0b\x32\x1b.indexify_coordinator.Index"2\n\x0fGetIndexRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t">\n\x10GetIndexResponse\x12*\n\x05index\x18\x01 \x01(\x0b\x32\x1b.indexify_coordinator.Index"@\n\x12\x43reateIndexRequest\x12*\n\x05index\x18\x02 \x01(\x0b\x32\x1b.indexify_coordinator.Index"\x15\n\x13\x43reateIndexResponse"z\n\x05Index\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12\x19\n\x11\x65xtraction_policy\x18\x05 \x01(\t\x12\x11\n\textractor\x18\x06 \x01(\t"\x1e\n\tEmbedding\x12\x11\n\tembedding\x18\x01 \x03(\x02" \n\nAttributes\x12\x12\n\nattributes\x18\x02 \x01(\t"\x81\x01\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\tembedding\x18\x02 \x01(\x0b\x32\x1f.indexify_coordinator.Embedding\x12\x34\n\nattributes\x18\x03 \x01(\x0b\x32 .indexify_coordinator.Attributes"V\n\x07\x43ontent\x12\x0c\n\x04mime\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12/\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32\x1d.indexify_coordinator.Feature"p\n\x17RegisterExecutorRequest\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12\x32\n\textractor\x18\x03 \x01(\x0b\x32\x1f.indexify_coordinator.Extractor"/\n\x18RegisterExecutorResponse\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t">\n\x10HeartbeatRequest\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t\x12\x15\n\rpending_tasks\x18\x02 \x01(\x03"S\n\x11HeartbeatResponse\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t\x12)\n\x05tasks\x18\x02 \x03(\x0b\x32\x1a.indexify_coordinator.Task"\xeb\x02\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\textractor\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12?\n\x10\x63ontent_metadata\x18\x04 \x01(\x0b\x32%.indexify_coordinator.ContentMetadata\x12\x14\n\x0cinput_params\x18\x05 \x01(\t\x12\x19\n\x11\x65xtraction_policy\x18\x06 \x01(\t\x12P\n\x14output_index_mapping\x18\x07 \x03(\x0b\x32\x32.indexify_coordinator.Task.OutputIndexMappingEntry\x12\x32\n\x07outcome\x18\x08 \x01(\x0e\x32!.indexify_coordinator.TaskOutcome\x1a\x39\n\x17OutputIndexMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x17\n\x15ListExtractorsRequest"M\n\x16ListExtractorsResponse\x12\x33\n\nextractors\x18\x01 \x03(\x0b\x32\x1f.indexify_coordinator.Extractor"\xf1\x02\n\tExtractor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x14\n\x0cinput_params\x18\x03 \x01(\t\x12P\n\x11\x65mbedding_schemas\x18\x04 \x03(\x0b\x32\x35.indexify_coordinator.Extractor.EmbeddingSchemasEntry\x12N\n\x10metadata_schemas\x18\x05 \x03(\x0b\x32\x34.indexify_coordinator.Extractor.MetadataSchemasEntry\x12\x18\n\x10input_mime_types\x18\x06 \x03(\t\x1a\x37\n\x15\x45mbeddingSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14MetadataSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"#\n\x13GetNamespaceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"J\n\x14GetNamespaceResponse\x12\x32\n\tnamespace\x18\x01 \x01(\x0b\x32\x1f.indexify_coordinator.Namespace"\xc6\x01\n\x12ListContentRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x11\n\tparent_id\x18\x03 \x01(\t\x12I\n\tlabels_eq\x18\x04 \x03(\x0b\x32\x36.indexify_coordinator.ListContentRequest.LabelsEqEntry\x1a/\n\rLabelsEqEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"R\n\x13ListContentResponse\x12;\n\x0c\x63ontent_list\x18\x01 \x03(\x0b\x32%.indexify_coordinator.ContentMetadata"2\n\x1dListExtractionPoliciesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t"Z\n\x1eListExtractionPoliciesResponse\x12\x38\n\x08policies\x18\x01 \x03(\x0b\x32&.indexify_coordinator.ExtractionPolicy"`\n\x16\x43reateNamespaceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x08policies\x18\x02 \x03(\x0b\x32&.indexify_coordinator.ExtractionPolicy";\n\x17\x43reateNamespaceResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\x03"\x16\n\x14ListNamespaceRequest"L\n\x15ListNamespaceResponse\x12\x33\n\nnamespaces\x18\x01 \x03(\x0b\x32\x1f.indexify_coordinator.Namespace"\xd7\x01\n\x10\x45xtractionPolicy\x12\x11\n\textractor\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cinput_params\x18\x04 \x01(\t\x12\x44\n\x07\x66ilters\x18\x05 \x03(\x0b\x32\x33.indexify_coordinator.ExtractionPolicy.FiltersEntry\x12\x16\n\x0e\x63ontent_source\x18\x06 \x01(\t\x1a.\n\x0c\x46iltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"x\n\x17\x45xtractionPolicyRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x36\n\x06policy\x18\x03 \x01(\x0b\x32&.indexify_coordinator.ExtractionPolicy\x12\x12\n\ncreated_at\x18\x02 \x01(\x03"\xbb\x03\n\x18\x45xtractionPolicyResponse\x12\x12\n\ncreated_at\x18\x03 \x01(\x03\x12\x32\n\textractor\x18\x02 \x01(\x0b\x32\x1f.indexify_coordinator.Extractor\x12k\n\x18index_name_table_mapping\x18\x04 \x03(\x0b\x32I.indexify_coordinator.ExtractionPolicyResponse.IndexNameTableMappingEntry\x12m\n\x19output_index_name_mapping\x18\x05 \x03(\x0b\x32J.indexify_coordinator.ExtractionPolicyResponse.OutputIndexNameMappingEntry\x1a<\n\x1aIndexNameTableMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a=\n\x1bOutputIndexNameMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xa3\x02\n\x0f\x43ontentMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x11\n\tparent_id\x18\x03 \x01(\t\x12\x0c\n\x04mime\x18\x04 \x01(\t\x12\x41\n\x06labels\x18\x05 \x03(\x0b\x32\x31.indexify_coordinator.ContentMetadata.LabelsEntry\x12\x13\n\x0bstorage_url\x18\x06 \x01(\t\x12\x12\n\ncreated_at\x18\x07 \x01(\x03\x12\x11\n\tnamespace\x18\x08 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t\x12\x12\n\nsize_bytes\x18\n \x01(\x04\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"N\n\x14\x43reateContentRequest\x12\x36\n\x07\x63ontent\x18\x02 \x01(\x0b\x32%.indexify_coordinator.ContentMetadata"#\n\x15\x43reateContentResponse\x12\n\n\x02id\x18\x01 \x01(\t"S\n\tNamespace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x08policies\x18\x02 \x03(\x0b\x32&.indexify_coordinator.ExtractionPolicy"=\n\x10GetSchemaRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x16\n\x0e\x63ontent_source\x18\x02 \x01(\t"O\n\x11GetSchemaResponse\x12:\n\x06schema\x18\x01 \x01(\x0b\x32*.indexify_coordinator.StructuredDataSchema"?\n\x14StructuredDataSchema\x12\x0f\n\x07\x63olumns\x18\x01 \x01(\t\x12\x16\n\x0e\x63ontent_source\x18\x02 \x01(\t"(\n\x13GetAllSchemaRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t"S\n\x14GetAllSchemaResponse\x12;\n\x07schemas\x18\x01 \x03(\x0b\x32*.indexify_coordinator.StructuredDataSchema*3\n\x0bTaskOutcome\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x32\x92\x11\n\x12\x43oordinatorService\x12j\n\rCreateContent\x12*.indexify_coordinator.CreateContentRequest\x1a+.indexify_coordinator.CreateContentResponse"\x00\x12y\n\x12GetContentMetadata\x12/.indexify_coordinator.GetContentMetadataRequest\x1a\x30.indexify_coordinator.GetContentMetadataResponse"\x00\x12\x64\n\x0bListContent\x12(.indexify_coordinator.ListContentRequest\x1a).indexify_coordinator.ListContentResponse"\x00\x12y\n\x16\x43reateExtractionPolicy\x12-.indexify_coordinator.ExtractionPolicyRequest\x1a..indexify_coordinator.ExtractionPolicyResponse"\x00\x12\x85\x01\n\x16ListExtractionPolicies\x12\x33.indexify_coordinator.ListExtractionPoliciesRequest\x1a\x34.indexify_coordinator.ListExtractionPoliciesResponse"\x00\x12i\n\x08\x43reateNS\x12,.indexify_coordinator.CreateNamespaceRequest\x1a-.indexify_coordinator.CreateNamespaceResponse"\x00\x12\x63\n\x06ListNS\x12*.indexify_coordinator.ListNamespaceRequest\x1a+.indexify_coordinator.ListNamespaceResponse"\x00\x12`\n\x05GetNS\x12).indexify_coordinator.GetNamespaceRequest\x1a*.indexify_coordinator.GetNamespaceResponse"\x00\x12m\n\x0eListExtractors\x12+.indexify_coordinator.ListExtractorsRequest\x1a,.indexify_coordinator.ListExtractorsResponse"\x00\x12s\n\x10RegisterExecutor\x12-.indexify_coordinator.RegisterExecutorRequest\x1a..indexify_coordinator.RegisterExecutorResponse"\x00\x12\x62\n\tHeartbeat\x12&.indexify_coordinator.HeartbeatRequest\x1a\'.indexify_coordinator.HeartbeatResponse"\x00(\x01\x30\x01\x12\x64\n\x0bListIndexes\x12(.indexify_coordinator.ListIndexesRequest\x1a).indexify_coordinator.ListIndexesResponse"\x00\x12[\n\x08GetIndex\x12%.indexify_coordinator.GetIndexRequest\x1a&.indexify_coordinator.GetIndexResponse"\x00\x12\x64\n\x0b\x43reateIndex\x12(.indexify_coordinator.CreateIndexRequest\x1a).indexify_coordinator.CreateIndexResponse"\x00\x12\x88\x01\n\x17GetExtractorCoordinates\x12\x34.indexify_coordinator.GetExtractorCoordinatesRequest\x1a\x35.indexify_coordinator.GetExtractorCoordinatesResponse"\x00\x12\x61\n\nUpdateTask\x12\'.indexify_coordinator.UpdateTaskRequest\x1a(.indexify_coordinator.UpdateTaskResponse"\x00\x12s\n\x10ListStateChanges\x12-.indexify_coordinator.ListStateChangesRequest\x1a..indexify_coordinator.ListStateChangesResponse"\x00\x12^\n\tListTasks\x12&.indexify_coordinator.ListTasksRequest\x1a\'.indexify_coordinator.ListTasksResponse"\x00\x12^\n\tGetSchema\x12&.indexify_coordinator.GetSchemaRequest\x1a\'.indexify_coordinator.GetSchemaResponse"\x00\x12\x66\n\x0bListSchemas\x12).indexify_coordinator.GetAllSchemaRequest\x1a*.indexify_coordinator.GetAllSchemaResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "coordinator_service_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_TASK_OUTPUTINDEXMAPPINGENTRY"]._options = None
    _globals["_TASK_OUTPUTINDEXMAPPINGENTRY"]._serialized_options = b"8\001"
    _globals["_EXTRACTOR_EMBEDDINGSCHEMASENTRY"]._options = None
    _globals["_EXTRACTOR_EMBEDDINGSCHEMASENTRY"]._serialized_options = b"8\001"
    _globals["_EXTRACTOR_METADATASCHEMASENTRY"]._options = None
    _globals["_EXTRACTOR_METADATASCHEMASENTRY"]._serialized_options = b"8\001"
    _globals["_LISTCONTENTREQUEST_LABELSEQENTRY"]._options = None
    _globals["_LISTCONTENTREQUEST_LABELSEQENTRY"]._serialized_options = b"8\001"
    _globals["_EXTRACTIONPOLICY_FILTERSENTRY"]._options = None
    _globals["_EXTRACTIONPOLICY_FILTERSENTRY"]._serialized_options = b"8\001"
    _globals["_EXTRACTIONPOLICYRESPONSE_INDEXNAMETABLEMAPPINGENTRY"]._options = None
    _globals[
        "_EXTRACTIONPOLICYRESPONSE_INDEXNAMETABLEMAPPINGENTRY"
    ]._serialized_options = b"8\001"
    _globals["_EXTRACTIONPOLICYRESPONSE_OUTPUTINDEXNAMEMAPPINGENTRY"]._options = None
    _globals[
        "_EXTRACTIONPOLICYRESPONSE_OUTPUTINDEXNAMEMAPPINGENTRY"
    ]._serialized_options = b"8\001"
    _globals["_CONTENTMETADATA_LABELSENTRY"]._options = None
    _globals["_CONTENTMETADATA_LABELSENTRY"]._serialized_options = b"8\001"
    _globals["_TASKOUTCOME"]._serialized_start = 5137
    _globals["_TASKOUTCOME"]._serialized_end = 5188
    _globals["_GETCONTENTMETADATAREQUEST"]._serialized_start = 51
    _globals["_GETCONTENTMETADATAREQUEST"]._serialized_end = 100
    _globals["_GETCONTENTMETADATARESPONSE"]._serialized_start = 102
    _globals["_GETCONTENTMETADATARESPONSE"]._serialized_end = 191
    _globals["_UPDATETASKREQUEST"]._serialized_start = 194
    _globals["_UPDATETASKREQUEST"]._serialized_end = 364
    _globals["_LISTSTATECHANGESREQUEST"]._serialized_start = 366
    _globals["_LISTSTATECHANGESREQUEST"]._serialized_end = 391
    _globals["_STATECHANGE"]._serialized_start = 393
    _globals["_STATECHANGE"]._serialized_end = 500
    _globals["_LISTSTATECHANGESRESPONSE"]._serialized_start = 502
    _globals["_LISTSTATECHANGESRESPONSE"]._serialized_end = 580
    _globals["_LISTTASKSREQUEST"]._serialized_start = 582
    _globals["_LISTTASKSREQUEST"]._serialized_end = 646
    _globals["_LISTTASKSRESPONSE"]._serialized_start = 648
    _globals["_LISTTASKSRESPONSE"]._serialized_end = 710
    _globals["_UPDATETASKRESPONSE"]._serialized_start = 712
    _globals["_UPDATETASKRESPONSE"]._serialized_end = 732
    _globals["_GETEXTRACTORCOORDINATESREQUEST"]._serialized_start = 734
    _globals["_GETEXTRACTORCOORDINATESREQUEST"]._serialized_end = 785
    _globals["_GETEXTRACTORCOORDINATESRESPONSE"]._serialized_start = 787
    _globals["_GETEXTRACTORCOORDINATESRESPONSE"]._serialized_end = 835
    _globals["_LISTINDEXESREQUEST"]._serialized_start = 837
    _globals["_LISTINDEXESREQUEST"]._serialized_end = 876
    _globals["_LISTINDEXESRESPONSE"]._serialized_start = 878
    _globals["_LISTINDEXESRESPONSE"]._serialized_end = 945
    _globals["_GETINDEXREQUEST"]._serialized_start = 947
    _globals["_GETINDEXREQUEST"]._serialized_end = 997
    _globals["_GETINDEXRESPONSE"]._serialized_start = 999
    _globals["_GETINDEXRESPONSE"]._serialized_end = 1061
    _globals["_CREATEINDEXREQUEST"]._serialized_start = 1063
    _globals["_CREATEINDEXREQUEST"]._serialized_end = 1127
    _globals["_CREATEINDEXRESPONSE"]._serialized_start = 1129
    _globals["_CREATEINDEXRESPONSE"]._serialized_end = 1150
    _globals["_INDEX"]._serialized_start = 1152
    _globals["_INDEX"]._serialized_end = 1274
    _globals["_EMBEDDING"]._serialized_start = 1276
    _globals["_EMBEDDING"]._serialized_end = 1306
    _globals["_ATTRIBUTES"]._serialized_start = 1308
    _globals["_ATTRIBUTES"]._serialized_end = 1340
    _globals["_FEATURE"]._serialized_start = 1343
    _globals["_FEATURE"]._serialized_end = 1472
    _globals["_CONTENT"]._serialized_start = 1474
    _globals["_CONTENT"]._serialized_end = 1560
    _globals["_REGISTEREXECUTORREQUEST"]._serialized_start = 1562
    _globals["_REGISTEREXECUTORREQUEST"]._serialized_end = 1674
    _globals["_REGISTEREXECUTORRESPONSE"]._serialized_start = 1676
    _globals["_REGISTEREXECUTORRESPONSE"]._serialized_end = 1723
    _globals["_HEARTBEATREQUEST"]._serialized_start = 1725
    _globals["_HEARTBEATREQUEST"]._serialized_end = 1787
    _globals["_HEARTBEATRESPONSE"]._serialized_start = 1789
    _globals["_HEARTBEATRESPONSE"]._serialized_end = 1872
    _globals["_TASK"]._serialized_start = 1875
    _globals["_TASK"]._serialized_end = 2238
    _globals["_TASK_OUTPUTINDEXMAPPINGENTRY"]._serialized_start = 2181
    _globals["_TASK_OUTPUTINDEXMAPPINGENTRY"]._serialized_end = 2238
    _globals["_LISTEXTRACTORSREQUEST"]._serialized_start = 2240
    _globals["_LISTEXTRACTORSREQUEST"]._serialized_end = 2263
    _globals["_LISTEXTRACTORSRESPONSE"]._serialized_start = 2265
    _globals["_LISTEXTRACTORSRESPONSE"]._serialized_end = 2342
    _globals["_EXTRACTOR"]._serialized_start = 2345
    _globals["_EXTRACTOR"]._serialized_end = 2714
    _globals["_EXTRACTOR_EMBEDDINGSCHEMASENTRY"]._serialized_start = 2603
    _globals["_EXTRACTOR_EMBEDDINGSCHEMASENTRY"]._serialized_end = 2658
    _globals["_EXTRACTOR_METADATASCHEMASENTRY"]._serialized_start = 2660
    _globals["_EXTRACTOR_METADATASCHEMASENTRY"]._serialized_end = 2714
    _globals["_GETNAMESPACEREQUEST"]._serialized_start = 2716
    _globals["_GETNAMESPACEREQUEST"]._serialized_end = 2751
    _globals["_GETNAMESPACERESPONSE"]._serialized_start = 2753
    _globals["_GETNAMESPACERESPONSE"]._serialized_end = 2827
    _globals["_LISTCONTENTREQUEST"]._serialized_start = 2830
    _globals["_LISTCONTENTREQUEST"]._serialized_end = 3028
    _globals["_LISTCONTENTREQUEST_LABELSEQENTRY"]._serialized_start = 2981
    _globals["_LISTCONTENTREQUEST_LABELSEQENTRY"]._serialized_end = 3028
    _globals["_LISTCONTENTRESPONSE"]._serialized_start = 3030
    _globals["_LISTCONTENTRESPONSE"]._serialized_end = 3112
    _globals["_LISTEXTRACTIONPOLICIESREQUEST"]._serialized_start = 3114
    _globals["_LISTEXTRACTIONPOLICIESREQUEST"]._serialized_end = 3164
    _globals["_LISTEXTRACTIONPOLICIESRESPONSE"]._serialized_start = 3166
    _globals["_LISTEXTRACTIONPOLICIESRESPONSE"]._serialized_end = 3256
    _globals["_CREATENAMESPACEREQUEST"]._serialized_start = 3258
    _globals["_CREATENAMESPACEREQUEST"]._serialized_end = 3354
    _globals["_CREATENAMESPACERESPONSE"]._serialized_start = 3356
    _globals["_CREATENAMESPACERESPONSE"]._serialized_end = 3415
    _globals["_LISTNAMESPACEREQUEST"]._serialized_start = 3417
    _globals["_LISTNAMESPACEREQUEST"]._serialized_end = 3439
    _globals["_LISTNAMESPACERESPONSE"]._serialized_start = 3441
    _globals["_LISTNAMESPACERESPONSE"]._serialized_end = 3517
    _globals["_EXTRACTIONPOLICY"]._serialized_start = 3520
    _globals["_EXTRACTIONPOLICY"]._serialized_end = 3735
    _globals["_EXTRACTIONPOLICY_FILTERSENTRY"]._serialized_start = 3689
    _globals["_EXTRACTIONPOLICY_FILTERSENTRY"]._serialized_end = 3735
    _globals["_EXTRACTIONPOLICYREQUEST"]._serialized_start = 3737
    _globals["_EXTRACTIONPOLICYREQUEST"]._serialized_end = 3857
    _globals["_EXTRACTIONPOLICYRESPONSE"]._serialized_start = 3860
    _globals["_EXTRACTIONPOLICYRESPONSE"]._serialized_end = 4303
    _globals[
        "_EXTRACTIONPOLICYRESPONSE_INDEXNAMETABLEMAPPINGENTRY"
    ]._serialized_start = 4180
    _globals[
        "_EXTRACTIONPOLICYRESPONSE_INDEXNAMETABLEMAPPINGENTRY"
    ]._serialized_end = 4240
    _globals[
        "_EXTRACTIONPOLICYRESPONSE_OUTPUTINDEXNAMEMAPPINGENTRY"
    ]._serialized_start = 4242
    _globals[
        "_EXTRACTIONPOLICYRESPONSE_OUTPUTINDEXNAMEMAPPINGENTRY"
    ]._serialized_end = 4303
    _globals["_CONTENTMETADATA"]._serialized_start = 4306
    _globals["_CONTENTMETADATA"]._serialized_end = 4597
    _globals["_CONTENTMETADATA_LABELSENTRY"]._serialized_start = 4552
    _globals["_CONTENTMETADATA_LABELSENTRY"]._serialized_end = 4597
    _globals["_CREATECONTENTREQUEST"]._serialized_start = 4599
    _globals["_CREATECONTENTREQUEST"]._serialized_end = 4677
    _globals["_CREATECONTENTRESPONSE"]._serialized_start = 4679
    _globals["_CREATECONTENTRESPONSE"]._serialized_end = 4714
    _globals["_NAMESPACE"]._serialized_start = 4716
    _globals["_NAMESPACE"]._serialized_end = 4799
    _globals["_GETSCHEMAREQUEST"]._serialized_start = 4801
    _globals["_GETSCHEMAREQUEST"]._serialized_end = 4862
    _globals["_GETSCHEMARESPONSE"]._serialized_start = 4864
    _globals["_GETSCHEMARESPONSE"]._serialized_end = 4943
    _globals["_STRUCTUREDDATASCHEMA"]._serialized_start = 4945
    _globals["_STRUCTUREDDATASCHEMA"]._serialized_end = 5008
    _globals["_GETALLSCHEMAREQUEST"]._serialized_start = 5010
    _globals["_GETALLSCHEMAREQUEST"]._serialized_end = 5050
    _globals["_GETALLSCHEMARESPONSE"]._serialized_start = 5052
    _globals["_GETALLSCHEMARESPONSE"]._serialized_end = 5135
    _globals["_COORDINATORSERVICE"]._serialized_start = 5191
    _globals["_COORDINATORSERVICE"]._serialized_end = 7385
# @@protoc_insertion_point(module_scope)
