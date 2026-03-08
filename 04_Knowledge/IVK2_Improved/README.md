# IVK2 Improved v0.1

Lightweight local search index for your own files.

## What this is
IVK2 is a local file search engine for a Jarvis-style workspace.

Use it when:
- you have too many notes, clippings, or documents to browse manually
- you want to search your own corpus first
- you want a small local index without storing full raw text

Do not expect it to:
- replace web search
- understand everything automatically
- act like a full autonomous memory system

The intended flow is:
1. Search your local corpus first.
2. If local material is insufficient, use external search separately.
3. Treat external search as temporary evidence, not as automatic index content.

## Why this version
- No raw text in index (signature + tags + tiny lex sketch only)
- Incremental rebuild (mtime/size skip)
- SQLite compact storage + `vacuum`
- Small enough for local/offline-first use

## Quick start
Read `START_HERE_IVK2.md` first.

Shortest path:
```powershell
04_Knowledge\IVK2_Improved\run_ivk2.bat build <YOUR_DOCUMENT_FOLDER>
04_Knowledge\IVK2_Improved\run_ivk2.bat query "프롬프트 설계 원칙"
```

By default, the batch file stores the DB here:
- `04_Knowledge\IVK2_Improved\data\index.sqlite`

## Commands

### Build index
```powershell
04_Knowledge\IVK2_Improved\run_ivk2.bat build <YOUR_DOCUMENT_FOLDER>
```

### Query
```powershell
04_Knowledge\IVK2_Improved\run_ivk2.bat query "프롬프트 설계 원칙"
```

### Stats
```powershell
04_Knowledge\IVK2_Improved\run_ivk2.bat stats
```

### Compact DB
```powershell
04_Knowledge\IVK2_Improved\run_ivk2.bat vacuum
```

### Direct engine call (optional)
If you want a custom DB path:
```powershell
python 04_Knowledge\IVK2_Improved\ivk2_improved.py build <YOUR_DOCUMENT_FOLDER> --db <YOUR_OUTPUT_PATH>\ivk2\index.sqlite
python 04_Knowledge\IVK2_Improved\ivk2_improved.py query "프롬프트 설계 원칙" --db <YOUR_OUTPUT_PATH>\ivk2\index.sqlite -k 10
```

## Dual profile (for large vaults)
Use this only when one vault becomes large enough that one DB feels slow.

- guide: `DUAL_PROFILE.md`
- build script: `run_ivk2_dual_profile.bat`
- merged query command:
```powershell
python 04_Knowledge\IVK2_Improved\ivk2_improved.py query-dual "질문" --hot-db 04_Knowledge\IVK2_Improved\data\hot.sqlite --cold-db 04_Knowledge\IVK2_Improved\data\cold.sqlite -k 10
```

## External search note
IVK2 is local-first by design.

If you later want hybrid search:
- keep IVK2 as the local source of truth
- attach external search as a separate evidence lane
- do not merge web results directly into the local DB by default

## Notes
- Intended for internal/local corpus search.
- Good for "find where I already thought about this".
- For latest web facts, use web search separately.
- `run_ivk2.bat`는 먼저 `python`을, 없으면 `py -3`를 사용합니다.
