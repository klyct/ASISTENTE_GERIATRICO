from bardapi import Bard
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("Zgg2QUWXYI_Wh9GMuBatHZt6bcpw_tF79eqlj1PQOfoAuQ3VXYe863FItPMWcDSb6_qapA.")
bard = Bard(token=token)
response = bard.get_answer('saludame')
print(response['content'])
