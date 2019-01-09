import time

from behave import Given, then, step

from src.pivotal_api_services.workspaces import WorkspaceServices
from src.utils.json_schema_validator import validate_json_schema

workspaces_services = WorkspaceServices()


@Given(u"I create a Workspace")
def create_project_step(context):
    data = {"name": "New Workspace"}
    context.workspaces_status, context.workspaces_response = workspaces_services.create_workspace(data)


@then(u'I verify project creation status is {status_code}')
def step_impl(context, status_code):
    print(context.project_status)
    assert context.workspaces_status == status_code, "Workspace creation status is %s" % status_code


@step(u'I verify project schema')
def step_impl(context):
    actual_response = workspaces_services.get_workspace(id=str(context.project_response["id"]))
    schema = workspaces_services.get_workspace_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Project Schema failed due to: {}".format(schema_failure_reason)