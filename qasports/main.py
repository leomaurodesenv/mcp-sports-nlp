# server.py
from datasets import load_dataset
from mcp.server.fastmcp import FastMCP, Context


DATASET_NAME = "leomaurodesenv/QASports2"
mcp = FastMCP("QASports2")
dataset = load_dataset(DATASET_NAME, "all", split="train[:10]")
subsets = [hf_link.split("/")[-3] for hf_link in dataset.download_checksums.keys()]


@mcp.tool()
async def get_sports() -> str:
    """Get a list of available sports."""
    global subsets
    return "Available sports: " + "\n- ".join(subsets)


@mcp.tool()
async def get_questions(sport: str, ctx: Context) -> str:
    """Get questions for a given sport.

    Args:
        sport: Name of the sport
        ctx: MCP context object
    """
    # Log a message to the client
    await ctx.info(f"Processing {sport} data...")

    # Loading dataset and generating answer
    subset_data = load_dataset(DATASET_NAME, sport, split="train[:10]")
    data = [
        f"question: {s_data['question']}, answer: {s_data['answer']} "
        for s_data in subset_data
    ]
    summary = f"Summarize: {'\n'.join(data)[:500]}"

    # Return summary text
    return summary


if __name__ == "__main__":
    mcp.run()
