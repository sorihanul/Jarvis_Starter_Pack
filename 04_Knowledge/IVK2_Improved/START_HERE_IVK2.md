# START HERE: IVK2

## What this is
IVK2 is a local search helper for your own files.

It is useful when:
- you have too many notes or documents
- you know the idea exists somewhere, but not where
- you want to search your own corpus before going to the web

## What it is not
- not a web search engine
- not an autonomous agent
- not a full memory system

Think of it as:
- "search my own archive first"

## First use

### 1. Build your local index
```powershell
<YOUR_WORKSPACE_PATH>\IVK2_Improved\run_ivk2.bat build <YOUR_DOCUMENT_FOLDER>
```

Replace `<YOUR_DOCUMENT_FOLDER>` with your own folder if needed.

### 2. Ask a question
```powershell
<YOUR_WORKSPACE_PATH>\IVK2_Improved\run_ivk2.bat query "프롬프트 설계 원칙"
```

### 3. Check DB status
```powershell
<YOUR_WORKSPACE_PATH>\IVK2_Improved\run_ivk2.bat stats
```

## Default storage
By default, this starter version stores the index here:

```text
<YOUR_WORKSPACE_PATH>\IVK2_Improved\data\index.sqlite
```

That means you can copy this package and keep the index close to the tool.

## Recommended usage
1. Search local files first.
2. If local evidence is weak, do external search separately.
3. Keep web results separate unless you deliberately promote them.

## When to use dual profile
Use `run_ivk2_dual_profile.bat` only when your vault becomes large enough that one DB feels slow.

For normal starter use, do not start with dual profile.
