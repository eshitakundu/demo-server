# Demo MCP Server

A lightweight demo server built with FastMCP for demonstration and testing purposes. This server implements the Model Context Protocol (MCP) and can be used with Claude and other compatible clients.

## Quick Start

### Prerequisites

- Python 3.12 or higher
- pip or uv (for dependency management)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/demo-mcp-server.git
   cd demo-mcp-server
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # Or with uv:
   uv pip install -r requirements.txt
   ```

### Running the Server

```bash
mcp dev main.py
```

The server will start and be ready to accept requests via the MCP protocol.