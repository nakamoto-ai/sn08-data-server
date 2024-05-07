import argparse
import jwt
from datetime import datetime, timedelta
import config

def generate_jwt(key: str, dur: float):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=dur),  # Token expires in 1 day
        'iat': datetime.utcnow(),  # Issued at time
    }

    # Encode the payload to create the JWT
    encoded_jwt = jwt.encode(payload, key, algorithm='HS256')
    print(encoded_jwt)

if __name__ == '__main__':    
    parser = argparse.ArgumentParser(description='Generate JWT for file download')
    parser.add_argument('--dur', type=float, default=30, help='Duration key is valid')
    args = parser.parse_args()

    generate_jwt(key=config.SECRET_KEY, dur=args.dur)
