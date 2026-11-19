"""Mini agentic SDLC pipeline."""
FEATURE_REQUEST = "Add CSV export to the reports page, preserving applied filters."

def requirement_agent():
    return [{
        "id": "US-1",
        "text": "As a user, export the filtered report view as CSV.",
        "acceptance_criteria": [
            "clicking Export produces a .csv file",
            "the CSV contains only filtered rows",
            "the header matches visible columns",
        ],
    }]

def human_confirms_stories(stories):
    print("[HUMAN CHECKPOINT] stories confirmed")
    return True

def design_agent(stories):
    return {"story_id": stories[0]["id"], "components": ["export_endpoint", "csv_serializer", "export_button"]}

def coding_agent(design, stories):
    def export_endpoint(rows, applied_filters, columns):
        filtered = [row for row in rows if all(row.get(key) == value for key, value in applied_filters.items())]
        lines = [",".join(columns)]
        lines.extend(",".join(str(row.get(column, "")) for column in columns) for row in filtered)
        return "\n".join(lines)
    return {"design_ref": design["components"], "export_endpoint": export_endpoint}

def testing_agent(stories):
    """Tests are generated from acceptance criteria, independently of code."""
    def test_suite(export_function):
        rows = [{"region": "North", "sales": 100}, {"region": "South", "sales": 200}, {"region": "North", "sales": 150}]
        output = export_function(rows, {"region": "North"}, ["region", "sales"])
        return [
            ("produces output", bool(output)),
            ("header matches", output.splitlines()[0] == "region,sales"),
            ("only filtered rows", all("South" not in line for line in output.splitlines()[1:])),
        ]
    return test_suite

def review_agent(test_results):
    clean = all(passed for _, passed in test_results)
    return {"issues": [] if clean else ["test failure"], "clean": clean}

if __name__ == "__main__":
    stories = requirement_agent()
    human_confirms_stories(stories)
    design = design_agent(stories)
    code = coding_agent(design, stories)
    test_results = testing_agent(stories)(code["export_endpoint"])
    review = review_agent(test_results)
    print({"stories": stories, "design": design, "tests": test_results, "review": review})
