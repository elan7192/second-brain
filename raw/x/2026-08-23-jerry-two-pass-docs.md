# Source: Jerry Liu on two-pass document processing

- URL: https://x.com/jerryjliu0/status/2091564183922077885
- Author: jerryjliu0 (Jerry Liu)
- Date: 2026-08-23
- Captured: 2026-08-24 from the pasted URL (fxTwitter). Attached video was not transcribed.

## Tweet

The latest RAG trend for the current agent harnesses (Codex, Cowork) is to do two passes of document processing to solve a knowledge work task over a data room of documents:

1. A fast and light pass, oftentimes using a free/OSS doc parsing tool. This can be cheaply run across 10-100-1k’s of files, and enables the agent to then do retrieval (e.g. grep, semantic) to find relevant subsets of context.

2. A “just-in-time” VLM-based pass. Once the agent finds the relevant pages of context, it will screenshot the documents and call its own VLM (or write code) to dissect the pages.

The issue with only using VLM-based OCR tools over massive ad-hoc customer file dumps is that it’s slow and expensive. Doing JIT VLM OCR allows the agent to filter through the data cheaply, but still preserve accuracy for the context that’s needed for the task.

The agent harnesses do two-pass document processing by default using off the shelf-tools: pdf2text as the first pass, and using itself (Opus 5) as the second pass. See the below video where Cowork runs over a bunch of PDFs to answer a question about a benchmark graph in the Kimi k3 paper.

The main issues here with the “out of the box” doc processing these agents offer are:

- Opus 5 is not the best VLM for OCR. It is also way too expensive at scale and lacks grounding
- The OSS tools like pypdf, pdf2text, may not be versatile enough as the first pass.
- The agent will write a lot of throwaway code to rewrite things an OCR tool would’ve provided out of the box, like chart processing, bounding boxes, confidence scores, leading to increased cost and speed.

We have all the tools within @llama_index to help any agent do two-pass document processing with higher accuracy and lower cost.

1. We have liteparse for the first pass - a free/OSS parser written in Rust that’s faster/more accurate than other OSS parsers, and supports 50+ document types
2. We have LlamaParse for the second pass - an agentic document engine that uses VLMs+harnesses to achieve SOTA in accuracy and cost across various doc parsing and extraction tasks. It can be called from any agent harness as an MCP or skill. It takes in page numbers as input, so that the agent can choose to run LlamaParse over a subset of the doc instead of the full doc as a “zoom-in” pass.

Come check it out!

LiteParse: https://github.com/run-llama/liteparse
LlamaParse: https://cloud.llamaindex.ai/
All the relevant docs, including MCP, are here: https://developers.llamaindex.ai/llamaparse/for-agents/mcp/
