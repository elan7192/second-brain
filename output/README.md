# Compiled graph viewer

`obsidian-graph.html` loads three.js as ES modules. Serve this folder. Do not open the file from disk.

```
cd output
python3 -m http.server 8765
```

Open http://127.0.0.1:8765/obsidian-graph.html

Drag to orbit. Scroll to zoom. Cluster headers at a distance. Node labels when closer.
