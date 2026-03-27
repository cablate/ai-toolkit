# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- Confidence-based tiering guidelines for vector-memory skill
- Vector-memory skill and MCP server configuration
- ASCII statusline preview in README

### Changed
- Broadened thorough skill trigger description
- Merged Dispatch/Interactive agents into single Agents section in README
- Kept only Serena and memory in mcp.example.json

### Removed
- Removed mcp-image, excalidraw, chrome-devtools from README
- Removed survey-craft and transcribe skills
- Removed redundant tools-reference.md

## 2025-03-21

### Changed
- Flattened agents directory, translated all skills to English
- Rewritten agent-factory from JD to SOP style
- Standardized all skill and agent descriptions
- Consolidated dispatch agents: 7 to 5 with clear boundaries
- Refined dispatch agent positioning

### Removed
- Removed evals system
- Pruned interactive agents, kept only agent-factory

## 2025-03-20

### Added
- Agent dispatch eval system
- Dispatch agents, interactive agents, project-docs skill

### Changed
- Complete README rewrite

## 2025-03-19

### Added
- 9 skills: self-growth, code-review, brainstorming, dev patterns, TDD, MCP
- agentskill-expertise and collaboration-style skills
- Statusline: cost-aware Claude Code status bar
- Banner and branding

### Changed
- Repositioned repo from skill collection to full Claude Code setup
- Updated thorough skill with cost-aware model selection

## 2025-03-17

### Added
- Initial commit: handoff and thorough skills
- Sync script for pulling from ~/.claude/ to repo
