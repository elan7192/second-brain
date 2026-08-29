# Source: Four-pillar retrieval second brain

- Date: 2026-08-23
- Form: pasted architecture note, no URL

## Four pillars as pasted

To make an agent able to read and recall, go beyond vector search:

1. Hybrid Search + Rerank. Combine BM25 (exact keywords) with Vector (semantics). Reorder with a Cross-Encoder Reranker. Claim: this greatly raises retrieval accuracy. No method or numbers given.

2. Knowledge graph / GraphRAG. Record relations between entities and notes. Agent follows a path such as project A depends on technique B owned by person C.

3. Layered memory.
   - Working memory: current conversation prompt context.
   - Episodic memory: logs and experience from past tasks.
   - Semantic / declarative memory: the second-brain knowledge base (Obsidian / Notion notes, documents).

4. Agentic routing. Tool calling. Split the user question. Launch precise queries. Reflect whether the retrieved result is enough. Query again if not.

## Landing advice as pasted

1. Use ready tools: MemGPT / Letta, LangChain / LlamaIndex agent frameworks, or GraphRAG that supports Markdown / wikilinks.

2. Structure notes. Put standard YAML frontmatter at the top of each note (tags, summary, date). Let the agent filter metadata first, then search the body.
