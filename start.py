import os
import uvicorn

public_host = "0.0.0.0"
local_host = "127.0.0.1"
port = 8000
use_host = public_host

if __name__ == "__main__":
    os.environ["LOCAL"] = "True"
    uvicorn.run("app:app", host=use_host, port=port, reload=True, log_level="info")
