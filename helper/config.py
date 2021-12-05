

class Config:
    CAPS = dict(
        platformName='Android',
        platformVersion='25',
        automationName='UiAutomator2',
        udid='emulator-5554')
    WHATSAPP_APP_NAME = "com.whatsapp"
    WHATSAPP_APP_HOME_ACTIVITY= ".HomeActivity"
    WHATSAPP_APP_FILE_URL = "http://www.eniyiuygulama.com/whatsapp.apk"
    WHATSAPP_APP_FILE_URL_32_64 = "http://www.eniyiuygulama.com/whatsapp_32_64.apk"
    def __init__(self):
        pass

    def only(self, data=dict(), keys=[]):
        return dict((k, data[k]) for k in keys if k in data)

    '''
        Call only except for the keys you specified for the directory.
    '''

    def unonly(self, data=dict(), keys=[]):
        return {k: data[k] for k in set(list(data.keys())) - set(keys)}

    MESSAGES_ROW_REGEX =  b"(?P<_id>\d+)\|(?P<key_remote_jid>.*?)\|(?P<key_from_me>\d+)\|(?P<key_id>.*?)\|(?P<status>\d+)\|(?P<data>[\s\S]+?)\|(?P<timestamp>\d+)"
    MESSAGES_ROW_NEWS_REGEX = b"(?P<_id>\d+)\|(?P<hidden>\d+)\|(?P<key_remote_jid>.*?)\|(?P<last_message_row_id>\d+)\|(?P<last__readmessage_row_id>\d+)\|(?P<data>[\s\S]+?)\|(?P<amv_id>\d+)"


    MESSAGES_MEDIA_REGEX = b"(?P<_id>\d+)\|(?P<key_remote_jid>.*?)\|(?P<media_url>[\s\S]+?)\|(?P<media_wa_type>\d+)\|(?P<media_mime_type>[\s\S]+?)\|(?P<media_name>[\s\S]+?)\|(?P<media_enc_hash>[\s\S]+?)\|(?P<thumb_image>[\s\S]+?)\|\n"
    K_CONSTANT = "-1150867590"
    DATABASE_PATH = "/data/data/com.whatsapp/databases/msgstore.db"
    MESSAGES_TABLE_NAME = "messages"
    CHAT_LIST_TABLE_NAME = "chat_list"
    INSERT_INTO_MESSAGES_QUERY = "INSERT INTO {messages_table_name} " \
                                 "(key_remote_jid, key_from_me, key_id, status, needs_push, data, timestamp, media_url, media_mime_type, media_wa_type, media_size, media_name, media_caption, media_hash, media_duration, origin, latitude, longitude, thumb_image, remote_resource, received_timestamp, send_timestamp, receipt_server_timestamp, receipt_device_timestamp, read_device_timestamp, played_device_timestamp, raw_data, recipient_count, participant_hash, starred, quoted_row_id, mentioned_jids, multicast_id, edit_version, media_enc_hash, payment_transaction_id, forwarded, preview_type, send_count, lookup_tables) " \
                                 "VALUES ('{remote_jid}', '1', '{key_id_to}-{k_constant}', 0, 0, '{message}', (SELECT strftime('%s', 'now')*1000), NULL, NULL, 0, 0, NULL, NULL, NULL, '0', '0', '0.0', '0.0', NULL, NULL, (SELECT strftime('%s', 'now')/1000), '-1', NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, '0', NULL, NULL, '0', NULL, NULL, '0', 0, 0, '0');"
    INSERT_INTO_MESSAGES_QUERY_MEDIA = "INSERT INTO {messages_table_name} " \
                                       "(key_remote_jid, key_from_me, key_id, status, needs_push, data, timestamp, media_url, media_mime_type, media_wa_type, media_size, media_name, media_caption, media_hash, media_duration, origin, latitude, longitude, thumb_image, remote_resource, received_timestamp, send_timestamp, receipt_server_timestamp, receipt_device_timestamp, read_device_timestamp, played_device_timestamp, raw_data, recipient_count, participant_hash, starred, quoted_row_id, mentioned_jids, multicast_id, edit_version, media_enc_hash, payment_transaction_id, forwarded, preview_type, send_count, lookup_tables) " \
                                       "VALUES ('{remote_jid}', '1', '{key_id_to}-{k_constant}', 0, 0, NULL, (SELECT strftime('%s', 'now')*1000), '{media_url}', NULL, {media_wa_type}, {media_size}, '{media_name}', '{message}', '{media_hash}', '0',0, '0.0', '0.0', (SELECT thumb_image  FROM messages where _id={row_id}), NULL, (SELECT strftime('%s', 'now')*1000), '-1', NULL, NULL, NULL, NULL, NULL, '0', NULL, NULL, '0', NULL, NULL, '0', '{media_enc_hash}', NULL, '0', 0, 0, '0');"

    INSERT_INTO_MESSAGES_QUERY_MEDIA_NEXT = "INSERT INTO message_media (message_row_id, chat_row_id, autotransfer_retry_enabled, multicast_id, media_job_uuid, transferred, transcoded, file_path, file_size, suspicious_content, trim_from, trim_to, face_x, face_y, media_key, media_key_timestamp, width, height, has_streaming_sidecar, gif_attribution, thumbnail_height_width_ratio, direct_path, first_scan_sidecar, first_scan_length, message_url, mime_type, file_length, media_name, file_hash, media_duration, page_count, enc_file_hash, partial_media_hash, partial_media_enc_hash, is_animated_sticker, original_file_hash, mute_video) select  (SELECT MAX(_id) FROM {messages_table_name}),chat_row_id, 1, multicast_id, media_job_uuid, 0, transcoded, file_path, file_size, suspicious_content, trim_from, trim_to, face_x, face_y, media_key, media_key_timestamp, width, height, has_streaming_sidecar, gif_attribution, thumbnail_height_width_ratio, direct_path, first_scan_sidecar, first_scan_length, message_url, mime_type, file_length, media_name, file_hash, media_duration, page_count, enc_file_hash, partial_media_hash, partial_media_enc_hash, is_animated_sticker, original_file_hash, mute_video from message_media where message_row_id = {row_id};"
    INSERT_INTO_CHATLIST_QUERY = "INSERT INTO {chatlist_table_name} (key_remote_jid) " \
                                 "SELECT '{remote_jid}' WHERE not exists (SELECT 1 from chat_list where key_remote_jid='{remote_jid}');"
    INSERT_CHAT_OKEY = "insert into chat (jid_row_id,hidden) select (SELECT _id from jid where raw_string='{remote_jid}'),0 WHERE EXISTS (SELECT _id from jid where raw_string='{remote_jid}')"
    INSERT_JID = "insert into jid (user,server,agent,device,type,raw_string)  select '{clean_phone}','s.whatsapp.net',0,0,0,'{no_clean_phone}'  WHERE not EXISTS (SELECT _id from jid where raw_string='{no_clean_phone}')"
    UPDATE_CHATLIST_QUERY = "UPDATE {chatlist_table_name} SET message_table_id = " \
                            "(SELECT max(messages._id) FROM messages),last_read_receipt_sent_message_table_id= (SELECT max(messages._id) FROM messages) - 1, last_read_message_table_id = (SELECT max(messages._id) FROM messages) - 1, archived=0, last_message_table_id = (SELECT max(messages._id) FROM messages), sort_timestamp=(SELECT strftime('%s', 'now')*1000),mod_tag=0,gen=0.0,plaintext_disabled=1,unseen_message_count=1,unseen_row_count=1,vcard_ui_dismissed=0,change_number_notified_message_id=1,ephemeral_setting_timestamp=0,show_group_description=0,last_important_message_table_id=1    WHERE chat_list.key_remote_jid='{remote_jid}';"
    GET_MESSAGES = "SELECT _id, key_remote_jid, key_from_me, key_id, status, data, timestamp FROM "+str(MESSAGES_TABLE_NAME)+""
    GET_MESSAGES_YENI = "SELECT cv._id, cv.hidden, cv.raw_string_jid, cv.last_message_row_id, cv.last_read_message_row_id, amv.data,amv._id AS bizim_id FROM chat_view cv INNER JOIN available_message_view amv ON cv._id = amv.chat_row_id where amv.from_me = 0 and cv.last_message_row_id != cv.last_read_message_row_id and amv._id > cv.last_read_message_row_id and amv.lookup_tables != 100"
    GET_MEDIA = "select message_url,mime_type,hex(media_key) from message_media where message_row_id = {id}"
    FILTER_FROM_JID = " key_remote_jid = '{key_remote_jid}' "
    FILTER_FROM_DATE = " timestamp>={filter_from_date_epoch} "
    FILTER_TO_DATE = " timestamp<={filter_to_date_epoch} "
