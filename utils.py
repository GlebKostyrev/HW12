import json
import pprint

from config import CANDIDATES_PATH, SETTING_PATH

def get_settings():
    with open(SETTING_PATH, "r", encoding="utf-8") as f:
        data_json = json.load(f)
    return data_json


def get_candidates():
    with open(CANDIDATES_PATH, "r", encoding="utf-8") as f:
        data_json = json.load(f)
    return data_json


def get_candidate_by_cid(cid):

    candidates = get_candidates()

    for candidate in candidates:
        if candidate.get("id") == cid:
            return candidate


def search_candidates_by_name(name):

    settings = get_settings()
    case_sensitive = settings("case-sensitive", False)
    candidates = get_candidates()

    candidates_match = []

    for candidate in candidates:

        if name in candidate("name"):
            candidates_match.append(candidate)
            continue

        if not case_sensitive:
            if name.lower() in candidate("name").lower():
                candidates_match.append(candidate)

    return candidates_match

def get_candidates_by_skill(skill_name):

    setting = get_settings()
    limit = setting.get("limit", 3)
    candidates = get_candidates()
    candidates_match = []

    skill_name = skill_name.lower()

    for candidate in candidates:

        skills = candidate["skills"].lower().split(", ")

        if skill_name in skills:
            candidates_match.append(candidate)

    return candidates_match[:limit]

