import secrets
import argparse

def generate_api_key(length=32):
    """Generate a secure API key"""
    return secrets.token_hex(length)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure API key")
    parser.add_argument(
        "--length",
        type=int,
        default=32,
        help="Length of the API key in bytes (default: 32, resulting in a 64 character hex string)"
    )
    args = parser.parse_args()
    
    api_key = generate_api_key(args.length)
    print(f"Generated API key: {api_key}")
    print("\nTo use this key, add it to your .env file:")
    print(f"API_KEY={api_key}") 