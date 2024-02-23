import os
import subprocess
import hmac
import binascii
import hashlib
from cryptography.hazmat.primitives import constant_time
from flask import Flask, request, abort

from dotenv import load_dotenv
# Load các biến từ tệp .env
load_dotenv()

# Sử dụng biến
SECRET_KEY = os.getenv('SECRET_KEY')
print(1)
print(SECRET_KEY)
app_name = os.getenv('APP_NAME')
path = os.getenv('APP_PATH')
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.get_data(as_text=True)
        if is_valid_signature(request):
            default_path = "/home/ubuntu"
            cmd = f'{default_path}/auto_deploy.sh'
            print(cmd)
            print("Received valid signature")
            result = subprocess.run([cmd,app_name,path], check=False)
            
            # with open('deploy_log.txt', 'w') as log_file:
            #     result = subprocess.run([f'./auto_deploy.sh',app_name], check=False, stdout=log_file, stderr=subprocess.PIPE)
            return 'Webhook received successfully!', 200
        else:
            print("Received invalid signature")
            abort(403)
    else:
        abort(400)

def is_valid_signature(request):
    return True
    signature = request.headers.get('X-Hub-Signature-256')
    if not signature:
        print("not signature")
        return False

    # Extract the hash method and actual signature
    method, sig = signature.split('=', 1)

    # Calculate the expected hash
    expected_hash = hmac.new(SECRET_KEY, msg=request.data, digestmod=hashlib.sha256).digest()

    # Use constant_time.compare to mitigate timing attacks
    return constant_time.bytes_eq(binascii.unhexlify(sig), expected_hash)

if __name__ == '__main__':
    app.run(port=5000)
