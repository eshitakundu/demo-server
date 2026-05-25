from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo Server")

@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name with a friendly message.
    
    Args:
        name: The person's name to greet
        
    Returns:
        A personalized greeting message
    """
    greetings = [
        f"Hello, {name}! Great to see you!",
        f"Hi {name}! How are you doing today?",
        f"Welcome, {name}! Ready to get started?",
        f"Hey {name}! Nice to have you here!",
    ]
    return random.choice(greetings)


@mcp.tool()
def get_timestamp() -> dict:
    """Get the current timestamp and formatted date/time.
    
    Returns:
        A dictionary with current timestamp info
    """
    now = datetime.now()
    return {
        "iso_format": now.isoformat(),
        "unix_timestamp": now.timestamp(),
        "formatted": now.strftime("%Y-%m-%d %H:%M:%S"),
        "day_of_week": now.strftime("%A"),
    }

if __name__ == "__main__":
    mcp.run()