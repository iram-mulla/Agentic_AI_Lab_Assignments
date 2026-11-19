stories = [
    {"id": "US-1", "artifact": "CSV export"},
    {"id": "US-2", "artifact": "PDF export"},
]
pipeline = []
for story in stories:
    design = {"story_id": story["id"], "components": [f"{story['artifact']} endpoint", "serializer"]}
    code = {"story_id": story["id"], "implementation": f"implement_{story['artifact'].replace(' ', '_').lower()}"}
    test_suite = {"story_id": story["id"], "tests": [f"{story['artifact']} output", f"{story['artifact']} filter preservation"]}
    review = {"story_id": story["id"], "status": "pending human review", "independent_tests": True}
    pipeline.append({"story": story["id"], "design": design, "code": code, "tests": test_suite, "review": review})

print({"lineage": pipeline})
