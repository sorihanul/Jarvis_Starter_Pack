# 자비스 시스템 내비게이션 (DIRECTORY MAP)

이 파일은 레시피 규격과 현재 폴더(00_Core~05_Scripts)가 통합된 시스템 전체의 구조 지도입니다.
에이전트(자비스)는 파일 생성, 참조, 삭제 시 반드시 이 지도를 기반으로 경로를 설정해야 합니다.

## 🗂 STRUCTURE (전체 구조)

```text
Jarvis_Workspace/
│
├── [IDENTITY & NAVIGATION LAYER] (불변, 읽기 전용)
│   ├── START_HERE.md (진입 안내)
│   ├── MAP.md (현재 파일, 시스템 구조)
│   ├── POLICY.md (시스템 운영 핵심 정책)
│   ├── AGENT_INDEX.md (사용가능 에이전트 목록)
│   └── SKILL_INDEX.md (사용가능 스킬 목록)
│
├── 00_Core/ (두뇌/자아 핵심)
│   ├── AILO Full‑Stack v0.9E++ ... (AILO 영문 공식 스펙)
│   ├── 한글 AILO-H Full-Stack ... (AILO-H 한국어 공식 스펙/최초 정체성)
│   └── JARVIS_FOLDER_RECIPE_v1.0.md (폴더 설계 원칙, 본 파일의 기원이 되는 레시피)
│
├── 01_Modules/ (확장 기능 및 도구 모음)
│   ├── Coding_Sequential_Agent_Starter/ (순차적 코딩 & 리뷰 에이전트 파이프라인 모음)
│   ├── Learning_Loop_Lite_Starter/ (세션 종료 캡슐과 승격 후보를 남기는 경량 학습 루프)
│   ├── Madang_Pan_Lite_Starter/ (전면 대화 라우팅 및 짧은 브리핑 모듈)
│   ├── Persona_Agent_Starter/ (맞춤형 문체/성격 기반 에이전트 생성 프레임워크)
│   ├── Project_Workspace_Lite_Starter/ (프로젝트 작업장을 4문서로 시작하는 경량 모듈)
│   └── AILO_Coding_Engine_Module_PUBLIC_v1.1.md (기본 코딩 엔진 체계)
│
├── 02_Protocols/ (업무 처리 통제 루틴)
│   ├── PIPELINE_CONTRACT_v1.3.md (대화/실행 분리 및 승인 파이프라인)
│   ├── AGENDA_Flow_Protocol_PUBLIC_v1.0.md (업무 안건 처리 플로우)
│   └── Memory_Garbage_Collector_Protocol_PUBLIC.md (메모리 정리 주기 통제)
│
├── 03_Memory/ (기억 관리 로직 구현체)
│   └── Jarvis_Memory.py (기억 압축/저장 스크립트)
│
├── 04_Knowledge/ (참조 지식 및 검색 로직)
│   ├── IVK 2.md (벡터 기반 지식 검색 개요)
│   └── IVK2_Improved/ (최적화된 검색 파이프라인 폴더)
│
├── 05_Scripts/ (유틸리티 및 템플릿 파일)
│   └── AGENDA_Flow_Template.ps1 (아젠다 템플릿 생성 스크립트)
│
├── [TASK & EXECUTION LAYER] (가변, 임시 및 기록 데이터)
│   ├── AGENTS/ (에이전트 개별 정의서 모음)
│   ├── SKILLS/ (폴더 공용 도구 모음)
│   ├── TASKS/ (현재 수행중인 작업 목록, 프로젝트 작업장, 운영 방법론 문서)
│   ├── CAPSULES/ (완료된 Task의 최종 세션 요약 데이터, 캡슐 템플릿, Agenda 캡슐)
│   └── LOGS/ (실행 로그, 에러 내역, Agenda 로그)
│
└── README.md (스타터 팩 최초 사용 설명서)
```

## 📖 CORE FILES (핵심 파일 안내)
- `START_HERE.md`: 에이전트 초기화 진입점
- `MAP.md`: 컴포넌트 간 이동 및 역할 이해 목적 지도 
- `02_Protocols/PIPELINE_CONTRACT_v1.3.md`: 대화/실행 분리 및 오케스트레이터 운영 규칙
- `00_Core/한글 AILO-H...md`: 최상위 불변 자비스(가라사니 시스템) 규칙 (`MAIN_IDENTITY`를 겸함)
- `POLICY.md`: AI가 지켜야 하는 작업 수행 태도 및 출력 형식

## 🗺 READ ORDER (부팅 시 권장 읽기 순서)
1) `START_HERE.md`
2) `MAP.md`
3) `00_Core/한글 AILO-H Full-Stack v0.91 — Unified Core Specification.md`
4) `POLICY.md`

## 🚫 RESTRICTED (금지 사항)
- **Identity Layer 오염 금지**: 작업(Task)에 관련된 내용은 오로지 `TASKS/`, `CAPSULES/`, `LOGS/`에만 쓴다.
- **경로 이탈 지양**: 정의된 구조 외에 가급적 불필요한 루트 폴더나 파일을 새로 생성하지 않도록 주의해 주세요.
