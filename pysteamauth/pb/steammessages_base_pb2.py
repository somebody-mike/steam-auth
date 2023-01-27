# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18steammessages_base.proto\x1a google/protobuf/descriptor.proto\"1\n\rCMsgIPAddress\x12\x0c\n\x02v4\x18\x01 \x01(\x07H\x00\x12\x0c\n\x02v6\x18\x02 \x01(\x0cH\x00\x42\x04\n\x02ip\"R\n\x13\x43MsgIPAddressBucket\x12+\n\x13original_ip_address\x18\x01 \x01(\x0b\x32\x0e.CMsgIPAddress\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\x06\"O\n\x1b\x43MsgGCRoutingProtoBufHeader\x12\x16\n\x0e\x64st_gcid_queue\x18\x01 \x01(\x04\x12\x18\n\x10\x64st_gc_dir_index\x18\x02 \x01(\r\"\xa4\x06\n\x12\x43MsgProtoBufHeader\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x18\n\x10\x63lient_sessionid\x18\x02 \x01(\x05\x12\x15\n\rrouting_appid\x18\x03 \x01(\r\x12*\n\x0cjobid_source\x18\n \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12*\n\x0cjobid_target\x18\x0b \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12\x17\n\x0ftarget_job_name\x18\x0c \x01(\t\x12\x0f\n\x07seq_num\x18\x18 \x01(\x05\x12\x12\n\x07\x65result\x18\r \x01(\x05:\x01\x32\x12\x15\n\rerror_message\x18\x0e \x01(\t\x12\x1a\n\x12\x61uth_account_flags\x18\x10 \x01(\r\x12\x14\n\x0ctoken_source\x18\x16 \x01(\r\x12\x1b\n\x13\x61\x64min_spoofing_user\x18\x17 \x01(\x08\x12\x1a\n\x0ftransport_error\x18\x11 \x01(\x05:\x01\x31\x12\'\n\tmessageid\x18\x12 \x01(\x04:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12\x1a\n\x12publisher_group_id\x18\x13 \x01(\r\x12\r\n\x05sysid\x18\x14 \x01(\r\x12\x11\n\ttrace_tag\x18\x15 \x01(\x04\x12\x15\n\rwebapi_key_id\x18\x19 \x01(\r\x12\x1f\n\x17is_from_external_source\x18\x1a \x01(\x08\x12\x18\n\x10\x66orward_to_sysid\x18\x1b \x03(\r\x12\x10\n\x08\x63m_sysid\x18\x1c \x01(\r\x12\x18\n\rlauncher_type\x18\x1f \x01(\r:\x01\x30\x12\x10\n\x05realm\x18  \x01(\r:\x01\x30\x12\x16\n\ntimeout_ms\x18! \x01(\x05:\x02-1\x12\x14\n\x0c\x64\x65\x62ug_source\x18\" \x01(\t\x12!\n\x19\x64\x65\x62ug_source_string_index\x18# \x01(\r\x12\x10\n\x08token_id\x18$ \x01(\x04\x12\x30\n\nrouting_gc\x18% \x01(\x0b\x32\x1c.CMsgGCRoutingProtoBufHeader\x12\x0c\n\x02ip\x18\x0f \x01(\rH\x00\x12\x0f\n\x05ip_v6\x18\x1d \x01(\x0cH\x00\x42\t\n\x07ip_addr\"8\n\tCMsgMulti\x12\x15\n\rsize_unzipped\x18\x01 \x01(\r\x12\x14\n\x0cmessage_body\x18\x02 \x01(\x0c\"+\n\x13\x43MsgProtobufWrapped\x12\x14\n\x0cmessage_body\x18\x01 \x01(\x0c\"\xa6\x01\n\x0e\x43MsgAuthTicket\x12\x0e\n\x06\x65state\x18\x01 \x01(\r\x12\x12\n\x07\x65result\x18\x02 \x01(\r:\x01\x32\x12\x0f\n\x07steamid\x18\x03 \x01(\x06\x12\x0e\n\x06gameid\x18\x04 \x01(\x06\x12\x14\n\x0ch_steam_pipe\x18\x05 \x01(\r\x12\x12\n\nticket_crc\x18\x06 \x01(\r\x12\x0e\n\x06ticket\x18\x07 \x01(\x0c\x12\x15\n\rserver_secret\x18\x08 \x01(\x0c\"\xeb\x02\n\x14\x43\x43\x44\x44\x42\x41ppDetailCommon\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x0c\n\x04tool\x18\x06 \x01(\x08\x12\x0c\n\x04\x64\x65mo\x18\x07 \x01(\x08\x12\r\n\x05media\x18\x08 \x01(\x08\x12\x1f\n\x17\x63ommunity_visible_stats\x18\t \x01(\x08\x12\x15\n\rfriendly_name\x18\n \x01(\t\x12\x13\n\x0bpropagation\x18\x0b \x01(\t\x12\x19\n\x11has_adult_content\x18\x0c \x01(\x08\x12!\n\x19is_visible_in_steam_china\x18\r \x01(\x08\x12\x10\n\x08\x61pp_type\x18\x0e \x01(\r\x12\x1d\n\x15has_adult_content_sex\x18\x0f \x01(\x08\x12\"\n\x1ahas_adult_content_violence\x18\x10 \x01(\x08\x12\x1d\n\x15\x63ontent_descriptorids\x18\x11 \x03(\r\"\xb3\x03\n\rCMsgAppRights\x12\x11\n\tedit_info\x18\x01 \x01(\x08\x12\x0f\n\x07publish\x18\x02 \x01(\x08\x12\x17\n\x0fview_error_data\x18\x03 \x01(\x08\x12\x10\n\x08\x64ownload\x18\x04 \x01(\x08\x12\x15\n\rupload_cdkeys\x18\x05 \x01(\x08\x12\x17\n\x0fgenerate_cdkeys\x18\x06 \x01(\x08\x12\x17\n\x0fview_financials\x18\x07 \x01(\x08\x12\x12\n\nmanage_ceg\x18\x08 \x01(\x08\x12\x16\n\x0emanage_signing\x18\t \x01(\x08\x12\x15\n\rmanage_cdkeys\x18\n \x01(\x08\x12\x16\n\x0e\x65\x64it_marketing\x18\x0b \x01(\x08\x12\x17\n\x0f\x65\x63onomy_support\x18\x0c \x01(\x08\x12\"\n\x1a\x65\x63onomy_support_supervisor\x18\r \x01(\x08\x12\x16\n\x0emanage_pricing\x18\x0e \x01(\x08\x12\x16\n\x0e\x62roadcast_live\x18\x0f \x01(\x08\x12\x1e\n\x16view_marketing_traffic\x18\x10 \x01(\x08\x12\"\n\x1a\x65\x64it_store_display_content\x18\x11 \x01(\x08\"\xf1\x02\n\x13\x43\x43uratorPreferences\x12\x1b\n\x13supported_languages\x18\x01 \x01(\r\x12\x18\n\x10platform_windows\x18\x02 \x01(\x08\x12\x14\n\x0cplatform_mac\x18\x03 \x01(\x08\x12\x16\n\x0eplatform_linux\x18\x04 \x01(\x08\x12\x12\n\nvr_content\x18\x05 \x01(\x08\x12\x1e\n\x16\x61\x64ult_content_violence\x18\x06 \x01(\x08\x12\x19\n\x11\x61\x64ult_content_sex\x18\x07 \x01(\x08\x12\x19\n\x11timestamp_updated\x18\x08 \x01(\r\x12\x16\n\x0etagids_curated\x18\t \x03(\r\x12\x17\n\x0ftagids_filtered\x18\n \x03(\r\x12\x15\n\rwebsite_title\x18\x0b \x01(\t\x12\x13\n\x0bwebsite_url\x18\x0c \x01(\t\x12\x16\n\x0e\x64iscussion_url\x18\r \x01(\t\x12\x16\n\x0eshow_broadcast\x18\x0e \x01(\x08\"@\n\x12\x43LocalizationToken\x12\x10\n\x08language\x18\x01 \x01(\r\x12\x18\n\x10localized_string\x18\x02 \x01(\t\"\xec\x01\n\x17\x43\x43lanEventUserNewsTuple\x12\x0e\n\x06\x63lanid\x18\x01 \x01(\r\x12\x11\n\tevent_gid\x18\x02 \x01(\x06\x12\x18\n\x10\x61nnouncement_gid\x18\x03 \x01(\x06\x12\x13\n\x0brtime_start\x18\x04 \x01(\r\x12\x11\n\trtime_end\x18\x05 \x01(\r\x12\x16\n\x0epriority_score\x18\x06 \x01(\r\x12\x0c\n\x04type\x18\x07 \x01(\r\x12\x18\n\x10\x63lamp_range_slot\x18\x08 \x01(\r\x12\r\n\x05\x61ppid\x18\t \x01(\r\x12\x1d\n\x15rtime32_last_modified\x18\n \x01(\r\"\x80\x01\n\x16\x43\x43lanMatchEventByRange\x12\x14\n\x0crtime_before\x18\x01 \x01(\r\x12\x13\n\x0brtime_after\x18\x02 \x01(\r\x12\x11\n\tqualified\x18\x03 \x01(\r\x12(\n\x06\x65vents\x18\x04 \x03(\x0b\x32\x18.CClanEventUserNewsTuple\"\x9b\x03\n\x1f\x43\x43ommunity_ClanAnnouncementInfo\x12\x0b\n\x03gid\x18\x01 \x01(\x04\x12\x0e\n\x06\x63lanid\x18\x02 \x01(\x04\x12\x10\n\x08posterid\x18\x03 \x01(\x04\x12\x10\n\x08headline\x18\x04 \x01(\t\x12\x10\n\x08posttime\x18\x05 \x01(\r\x12\x12\n\nupdatetime\x18\x06 \x01(\r\x12\x0c\n\x04\x62ody\x18\x07 \x01(\t\x12\x14\n\x0c\x63ommentcount\x18\x08 \x01(\x05\x12\x0c\n\x04tags\x18\t \x03(\t\x12\x10\n\x08language\x18\n \x01(\x05\x12\x0e\n\x06hidden\x18\x0b \x01(\x08\x12\x16\n\x0e\x66orum_topic_id\x18\x0c \x01(\x06\x12\x11\n\tevent_gid\x18\r \x01(\x06\x12\x13\n\x0bvoteupcount\x18\x0e \x01(\x05\x12\x15\n\rvotedowncount\x18\x0f \x01(\x05\x12V\n\x10\x62\x61n_check_result\x18\x10 \x01(\x0e\x32\x17.EBanContentCheckResult:#k_EBanContentCheckResult_NotScanned\x12\x0e\n\x06\x62\x61nned\x18\x11 \x01(\x08\"\xa6\x06\n\x0e\x43\x43lanEventData\x12\x0b\n\x03gid\x18\x01 \x01(\x06\x12\x14\n\x0c\x63lan_steamid\x18\x02 \x01(\x06\x12\x12\n\nevent_name\x18\x03 \x01(\t\x12;\n\nevent_type\x18\x04 \x01(\x0e\x32\x14.EProtoClanEventType:\x11k_EClanOtherEvent\x12\r\n\x05\x61ppid\x18\x05 \x01(\r\x12\x16\n\x0eserver_address\x18\x06 \x01(\t\x12\x17\n\x0fserver_password\x18\x07 \x01(\t\x12\x1a\n\x12rtime32_start_time\x18\x08 \x01(\r\x12\x18\n\x10rtime32_end_time\x18\t \x01(\r\x12\x15\n\rcomment_count\x18\n \x01(\x05\x12\x17\n\x0f\x63reator_steamid\x18\x0b \x01(\x06\x12\x1b\n\x13last_update_steamid\x18\x0c \x01(\x06\x12\x13\n\x0b\x65vent_notes\x18\r \x01(\t\x12\x10\n\x08jsondata\x18\x0e \x01(\t\x12;\n\x11\x61nnouncement_body\x18\x0f \x01(\x0b\x32 .CCommunity_ClanAnnouncementInfo\x12\x11\n\tpublished\x18\x10 \x01(\x08\x12\x0e\n\x06hidden\x18\x11 \x01(\x08\x12 \n\x18rtime32_visibility_start\x18\x12 \x01(\r\x12\x1e\n\x16rtime32_visibility_end\x18\x13 \x01(\r\x12\x1d\n\x15\x62roadcaster_accountid\x18\x14 \x01(\r\x12\x16\n\x0e\x66ollower_count\x18\x15 \x01(\r\x12\x14\n\x0cignore_count\x18\x16 \x01(\r\x12\x16\n\x0e\x66orum_topic_id\x18\x17 \x01(\x06\x12\x1d\n\x15rtime32_last_modified\x18\x18 \x01(\r\x12\x15\n\rnews_post_gid\x18\x19 \x01(\x06\x12\x1a\n\x12rtime_mod_reviewed\x18\x1a \x01(\r\x12\x1a\n\x12\x66\x65\x61tured_app_tagid\x18\x1b \x01(\r\x12\x19\n\x11referenced_appids\x18\x1c \x03(\r\x12\x10\n\x08\x62uild_id\x18\x1d \x01(\r\x12\x14\n\x0c\x62uild_branch\x18\x1e \x01(\t\"\xc7\x01\n\x10\x43\x42illing_Address\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x10\n\x08\x61\x64\x64ress1\x18\x03 \x01(\t\x12\x10\n\x08\x61\x64\x64ress2\x18\x04 \x01(\t\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\x10\n\x08us_state\x18\x06 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x07 \x01(\t\x12\x10\n\x08postcode\x18\x08 \x01(\t\x12\x11\n\tzip_plus4\x18\t \x01(\x05\x12\r\n\x05phone\x18\n \x01(\t\"\xdb\x01\n\x19\x43PackageReservationStatus\x12\x11\n\tpackageid\x18\x01 \x01(\r\x12\x19\n\x11reservation_state\x18\x02 \x01(\x05\x12\x16\n\x0equeue_position\x18\x03 \x01(\x05\x12\x18\n\x10total_queue_size\x18\x04 \x01(\x05\x12 \n\x18reservation_country_code\x18\x05 \x01(\t\x12\x0f\n\x07\x65xpired\x18\x06 \x01(\x08\x12\x14\n\x0ctime_expires\x18\x07 \x01(\r\x12\x15\n\rtime_reserved\x18\x08 \x01(\r\"/\n\x10\x43MsgKeyValuePair\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"3\n\x0f\x43MsgKeyValueSet\x12 \n\x05pairs\x18\x01 \x03(\x0b\x32\x11.CMsgKeyValuePair*\xd8\x02\n\x16\x45\x42\x61nContentCheckResult\x12\'\n#k_EBanContentCheckResult_NotScanned\x10\x00\x12\"\n\x1ek_EBanContentCheckResult_Reset\x10\x01\x12*\n&k_EBanContentCheckResult_NeedsChecking\x10\x02\x12)\n%k_EBanContentCheckResult_VeryUnlikely\x10\x05\x12%\n!k_EBanContentCheckResult_Unlikely\x10\x1e\x12%\n!k_EBanContentCheckResult_Possible\x10\x32\x12#\n\x1fk_EBanContentCheckResult_Likely\x10K\x12\'\n#k_EBanContentCheckResult_VeryLikely\x10\x64*\xeb\x07\n\x13\x45ProtoClanEventType\x12\x15\n\x11k_EClanOtherEvent\x10\x01\x12\x14\n\x10k_EClanGameEvent\x10\x02\x12\x15\n\x11k_EClanPartyEvent\x10\x03\x12\x17\n\x13k_EClanMeetingEvent\x10\x04\x12\x1c\n\x18k_EClanSpecialCauseEvent\x10\x05\x12\x1c\n\x18k_EClanMusicAndArtsEvent\x10\x06\x12\x16\n\x12k_EClanSportsEvent\x10\x07\x12\x14\n\x10k_EClanTripEvent\x10\x08\x12\x14\n\x10k_EClanChatEvent\x10\t\x12\x1b\n\x17k_EClanGameReleaseEvent\x10\n\x12\x19\n\x15k_EClanBroadcastEvent\x10\x0b\x12\x1b\n\x17k_EClanSmallUpdateEvent\x10\x0c\x12&\n\"k_EClanPreAnnounceMajorUpdateEvent\x10\r\x12\x1b\n\x17k_EClanMajorUpdateEvent\x10\x0e\x12\x1a\n\x16k_EClanDLCReleaseEvent\x10\x0f\x12\x1d\n\x19k_EClanFutureReleaseEvent\x10\x10\x12&\n\"k_EClanESportTournamentStreamEvent\x10\x11\x12\x19\n\x15k_EClanDevStreamEvent\x10\x12\x12\x1c\n\x18k_EClanFamousStreamEvent\x10\x13\x12\x19\n\x15k_EClanGameSalesEvent\x10\x14\x12\x1d\n\x19k_EClanGameItemSalesEvent\x10\x15\x12\x1d\n\x19k_EClanInGameBonusXPEvent\x10\x16\x12\x1a\n\x16k_EClanInGameLootEvent\x10\x17\x12\x1b\n\x17k_EClanInGamePerksEvent\x10\x18\x12\x1f\n\x1bk_EClanInGameChallengeEvent\x10\x19\x12\x1d\n\x19k_EClanInGameContestEvent\x10\x1a\x12\x13\n\x0fk_EClanIRLEvent\x10\x1b\x12\x14\n\x10k_EClanNewsEvent\x10\x1c\x12\x1b\n\x17k_EClanBetaReleaseEvent\x10\x1d\x12$\n k_EClanInGameContentReleaseEvent\x10\x1e\x12\x14\n\x10k_EClanFreeTrial\x10\x1f\x12\x18\n\x14k_EClanSeasonRelease\x10 \x12\x17\n\x13k_EClanSeasonUpdate\x10!\x12\x19\n\x15k_EClanCrosspostEvent\x10\"\x12\x1d\n\x19k_EClanInGameEventGeneral\x10#*\x81\x01\n\x1cPartnerEventNotificationType\x12\x11\n\rk_EEventStart\x10\x00\x12\x1a\n\x16k_EEventBroadcastStart\x10\x01\x12\x16\n\x12k_EEventMatchStart\x10\x02\x12\x1a\n\x16k_EEventPartnerMaxType\x10\x03:A\n\x12msgpool_soft_limit\x12\x1f.google.protobuf.MessageOptions\x18\xd0\x86\x03 \x01(\x05:\x02\x33\x32:B\n\x12msgpool_hard_limit\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x01(\x05:\x03\x33\x38\x34:C\n\x14\x66orce_php_generation\x12\x1c.google.protobuf.FileOptions\x18\xd0\x86\x03 \x01(\x08:\x05\x66\x61lse:H\n\x18php_output_always_number\x12\x1d.google.protobuf.FieldOptions\x18\xe4\x86\x03 \x01(\x08:\x05\x66\x61lse:J\n\x1a\x61llow_field_named_steam_id\x12\x1d.google.protobuf.FieldOptions\x18\xe8\x86\x03 \x01(\x08:\x05\x66\x61lseB\tH\x01\x80\x01\x01\x80\xb5\x18\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_base_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(msgpool_soft_limit)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(msgpool_hard_limit)
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(force_php_generation)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(php_output_always_number)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(allow_field_named_steam_id)

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'H\001\200\001\001\200\265\030\001'
    _EBANCONTENTCHECKRESULT._serialized_start = 4719
    _EBANCONTENTCHECKRESULT._serialized_end = 5063
    _EPROTOCLANEVENTTYPE._serialized_start = 5066
    _EPROTOCLANEVENTTYPE._serialized_end = 6069
    _PARTNEREVENTNOTIFICATIONTYPE._serialized_start = 6072
    _PARTNEREVENTNOTIFICATIONTYPE._serialized_end = 6201
    _CMSGIPADDRESS._serialized_start = 62
    _CMSGIPADDRESS._serialized_end = 111
    _CMSGIPADDRESSBUCKET._serialized_start = 113
    _CMSGIPADDRESSBUCKET._serialized_end = 195
    _CMSGGCROUTINGPROTOBUFHEADER._serialized_start = 197
    _CMSGGCROUTINGPROTOBUFHEADER._serialized_end = 276
    _CMSGPROTOBUFHEADER._serialized_start = 279
    _CMSGPROTOBUFHEADER._serialized_end = 1083
    _CMSGMULTI._serialized_start = 1085
    _CMSGMULTI._serialized_end = 1141
    _CMSGPROTOBUFWRAPPED._serialized_start = 1143
    _CMSGPROTOBUFWRAPPED._serialized_end = 1186
    _CMSGAUTHTICKET._serialized_start = 1189
    _CMSGAUTHTICKET._serialized_end = 1355
    _CCDDBAPPDETAILCOMMON._serialized_start = 1358
    _CCDDBAPPDETAILCOMMON._serialized_end = 1721
    _CMSGAPPRIGHTS._serialized_start = 1724
    _CMSGAPPRIGHTS._serialized_end = 2159
    _CCURATORPREFERENCES._serialized_start = 2162
    _CCURATORPREFERENCES._serialized_end = 2531
    _CLOCALIZATIONTOKEN._serialized_start = 2533
    _CLOCALIZATIONTOKEN._serialized_end = 2597
    _CCLANEVENTUSERNEWSTUPLE._serialized_start = 2600
    _CCLANEVENTUSERNEWSTUPLE._serialized_end = 2836
    _CCLANMATCHEVENTBYRANGE._serialized_start = 2839
    _CCLANMATCHEVENTBYRANGE._serialized_end = 2967
    _CCOMMUNITY_CLANANNOUNCEMENTINFO._serialized_start = 2970
    _CCOMMUNITY_CLANANNOUNCEMENTINFO._serialized_end = 3381
    _CCLANEVENTDATA._serialized_start = 3384
    _CCLANEVENTDATA._serialized_end = 4190
    _CBILLING_ADDRESS._serialized_start = 4193
    _CBILLING_ADDRESS._serialized_end = 4392
    _CPACKAGERESERVATIONSTATUS._serialized_start = 4395
    _CPACKAGERESERVATIONSTATUS._serialized_end = 4614
    _CMSGKEYVALUEPAIR._serialized_start = 4616
    _CMSGKEYVALUEPAIR._serialized_end = 4663
    _CMSGKEYVALUESET._serialized_start = 4665
    _CMSGKEYVALUESET._serialized_end = 4716
# @@protoc_insertion_point(module_scope)