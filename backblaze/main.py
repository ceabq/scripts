import b2sdk.v2
import time
info = b2sdk.v2.InMemoryAccountInfo()
b2api = b2sdk.v2.B2Api(info)
timenow = time.strftime("%Y-%m-%d")
filepath = input("文件路径")
application_key_id = ""
application_key = ""
b2api.authorize_account("production", application_key_id, application_key)
#引号里填bucket id
bucket = b2api.get_bucket_by_id("")
filename = timenow+'.zip'
bucket.upload_local_file(filepath,filename)