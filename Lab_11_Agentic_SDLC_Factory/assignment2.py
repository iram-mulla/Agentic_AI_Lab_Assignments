def buggy_coding_agent(rows, filters, columns):
    """Deliberate implementation bug: invert the acceptance-criterion filter."""
    filtered = [
        row
        for row in rows
        if all(row[key] != value for key, value in filters.items())
    ]
    return ",".join(columns) + "\n" + "\n".join(
        ",".join(str(row[column]) for column in columns)
        for row in filtered
    )


def testing_agent():
    """Independent test suite generated from CSV acceptance criteria."""
    def test_suite(export_function):
        rows = [
            {"region": "North", "sales": 100},
            {"region": "South", "sales": 200},
            {"region": "North", "sales": 150},
        ]
        output = export_function(rows, {"region": "North"}, ["region", "sales"])
        return {
            "produces_csv_output": bool(output),
            "header_matches": output.splitlines()[0] == "region,sales",
            "only_filtered_rows_present": all(
                "South" not in line for line in output.splitlines()[1:]
            ),
        }
    return test_suite


def buggy_export(rows, filters, columns):
    return buggy_coding_agent(rows, filters, columns)


rows = [{"region": "North", "sales": 100}, {"region": "South", "sales": 200}]
tests = testing_agent()(buggy_export)
failed_tests = [name for name, passed in tests.items() if not passed]

print({"tests": tests, "failed_tests": failed_tests})
assert "only_filtered_rows_present" in failed_tests
