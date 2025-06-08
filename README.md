# mcp-sports-nlp

This is a learning repository about the Model Context Protocol (MCP) and its application for accessing Sports Datasets.

## What is Model Context Protocol (MCP)?

"MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools." ([modelcontextprotocol](https://modelcontextprotocol.io/introduction)) Its structure is composed by:
- MCP Hosts: Programs like Claude Desktop, IDEs, or AI tools that access data through MCP.
- MCP Servers: Lightweight programs that expose specific capabilities through the standardized Model Context Protocol.
- Data Sources: Your computer’s files, databases, or external systems available over the internet (e.g., through APIs).

## Project Structure

This repository is structured as follows:

- `weather/`: Contains code related to accessing and processing weather data, based on [quickstarter server](https://modelcontextprotocol.io/quickstart/server).
