# AI Operations Assistant

## Overview
A multi-agent AI system that plans, executes, and verifies tasks using LLM reasoning and real APIs.

## Architecture
- Planner Agent: Converts user input into a JSON execution plan
- Executor Agent: Calls external APIs based on the plan
- Verifier Agent: Validates and formats the final response

## APIs Used
- OpenAI (LLM reasoning)
- GitHub Search API
- OpenWeatherMap API

## Setup Instructions

```bash
git clone <repo>
cd ai_ops_assistant
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app
