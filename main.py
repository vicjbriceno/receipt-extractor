import anthropic
from dotenv import load_dotenv
from pathlib import Path
import sys

## Import documents
from extractor.schema import Receipt

prompt = Path("receipt_system_prompt.txt").read_text(encoding="utf-8")
receipt = Path("samples/receipt_01.txt").read_text(encoding="utf-8")

load_dotenv()  # lee el .env y mete las env vars
client = anthropic.Anthropic()  # toma la anthropic key


try:
    response = client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=4096,
        system=prompt,
        messages=[{"role": "user", "content": receipt}],
        output_format=Receipt,
    )
except anthropic.APIConnectionError:
    print("No pude conectar con la API. Revisa tu conexion e intenta de nuevo.")
    sys.exit(1)
except anthropic.APIStatusError as e:
    print(f"La API devolvio un error ({e.status_code}). Intenta de nuevo.")
    sys.exit(1)

    
        
receipt_output=response.parsed_output.model_dump_json(indent=2)
print(receipt_output)






