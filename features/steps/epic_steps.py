from behave import given,then, step

from src.pivotal_api_services.epic import EpicServices
from src.utils.json_schema_validator import validate_json_schema

epic_services = EpicServices()


@step("I create a new epic")
def create_epic_step(context):
    data = {}
    for row in context.table:
        data = {"name": str(row['label'])}
    context.epic_status, context.epic_response = epic_services.create_epic(
        id_project=str(context.project_response["id"]), data=data)


@step("I update the epic")
def update_epic_step(context):
    data = {}
    for row in context.table:
        data = {"name": str(row['label'])}
    context.epic_status, context.epic_response = epic_services.update_epic(
        id_project=str(context.project_response["id"]), id_epic=str(context.epic_response["id"]), data=data)


@step("I delete the epic")
def update_project_step(context):
    context.epic_status = epic_services.delete_epic(id_project=str(context.project_response["id"]),
                                                    id_epic=str(context.epic_response["id"]))


@then('I verify epic updated status is {status_code}')
def step_impl(context, status_code):
    print(context.epic_status)
    assert context.epic_status == int(status_code), "Epic updated status is %s" % status_code


@then('I verify epic created status is {status_code}')
def step_impl(context, status_code):
    print(context.epic_status)
    assert context.epic_status == int(status_code), "Epic creation status is %s" % status_code


@then('I verify epic deleted status is {status_code}')
def step_impl(context, status_code):
    print(context.epic_status)
    assert context.epic_status == int(status_code), "epic deleted status is %s" % status_code


@step('I verify epic schema')
def step_impl(context):
    actual_response = epic_services.get_epic(id_project=str(context.project_response["id"]),
                                             id_epic=str(context.epic_response["id"]))
    schema = epic_services.get_epic_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Project Schema failed due to: {}".format(schema_failure_reason)