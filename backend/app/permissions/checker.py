from permissions.roles import ROLES

def has_permission(
    role,
    permission
):

    permissions = ROLES.get(
        role,
        []
    )

    return (

        "all" in permissions

        or

        permission in permissions

    )