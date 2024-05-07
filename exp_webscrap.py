from scrapegraphai.graphs import SmartScraperGraph
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyBz4zKLnsR1vZ6JWhtwSV68qpZ8ZOp0g0I"

# Define the configuration for the graph
graph_config = {
    "llm": {
        # "api_key": os.getenv("GOOGLE_API_KEY"),
        "model": "gemini-pro",
    },
    "embeddings": {
        "model_instance": "textembedding-gecko@003",
    },
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the articles",
    source="https://perinim.github.io/projects",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)