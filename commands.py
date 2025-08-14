import click
from app import app
from exts import db
from models.user import PermissionEnum, PermissionModel, RoleModel


@app.cli.command("create-permission")
def create_permission():
    for permission_name in dir(PermissionEnum):
        if permission_name.startswith("__"):
            continue
        permission = PermissionModel(name=getattr(PermissionEnum, permission_name))
        db.session.add(permission)
    db.session.commit()
    click.echo("权限添加成功！")


@app.cli.command("create-role")
def create_role():
    # 稽查
    inspect = RoleModel(name="稽查", desc="负责审核帖子和评论是否合法合规!")
    inspect.permission = PermissionModel.query.filter(PermissionModel.name.in_([
        PermissionEnum.POST, PermissionEnum.COMMENT
    ])).all()

    # 运营
    operator = RoleModel(name="运营", desc="负责网站持续正常运营!")
    operator.permission = PermissionModel.query.filter(PermissionModel.name.in_([
        PermissionEnum.POST,
        PermissionEnum.COMMENT,
        PermissionEnum.BOARD,
        PermissionEnum.FRONT_USER,
    ])).all()

    #管理员
    administrator = RoleModel(name="管理员", desc="负责整个网站所有工作!")
    administrator.permission = PermissionModel.query.all()

    db.session.add_all([inspect, operator, administrator])
    db.session.commit()
    click.echo("角色添加成功")
