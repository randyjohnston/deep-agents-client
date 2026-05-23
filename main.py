import asyncio
import os

from dotenv import load_dotenv
from langgraph_sdk import get_client

load_dotenv()

client = get_client(
    url="https://langsmith.randyjohnston.info/lgp/deepagents-retest-20260520-22a65f4e761e51a584209604d3c69f85",
    api_key=os.environ["LANGSMITH_API_KEY"],
)


async def chat():
    thread = await client.threads.create()
    thread_id = thread["thread_id"]
    print(f"Thread: {thread_id}")
    print("Type 'exit' or 'quit' to end.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() in ("exit", "quit"):
            break

        print("Assistant: ", end="", flush=True)
        printed = ""
        async for chunk in client.runs.stream(
            thread_id,
            "agent",
            input={"messages": [{"role": "user", "content": user_input}]},
            stream_mode="messages",
        ):
            if chunk.event == "messages/partial":
                for msg in chunk.data:
                    if msg.get("type") == "ai":
                        full_text = "".join(
                            block["text"]
                            for block in msg.get("content", [])
                            if isinstance(block, dict) and block.get("type") == "text"
                        )
                        delta = full_text[len(printed):]
                        if delta:
                            print(delta, end="", flush=True)
                            printed = full_text
        print("\n")


if __name__ == "__main__":
    asyncio.run(chat())
