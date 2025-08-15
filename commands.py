import click
from exts import db
from models.user import PermissionEnum, PermissionModel, RoleModel, UserModel


def create_permission():
    for permission_name in dir(PermissionEnum):
        if permission_name.startswith("__"):
            continue
        permission = PermissionModel(name=getattr(PermissionEnum, permission_name))
        db.session.add(permission)
    db.session.commit()
    click.echo("权限添加成功！")



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


def create_test_user():
    admin_role = RoleModel.query.filter_by(name="管理员").first()
    zhangsan = UserModel(username="张三", email="123465@163.com", password="0000000", is_staff=True, role=admin_role)

    operator_role = RoleModel.query.filter_by(name="运营").first()
    hanxue = UserModel(username="韩雪", email="abcdef@163.com", password="11111111", is_staff=True, role=operator_role)

    inspect_role = RoleModel.query.filter_by(name="稽查").first()
    laowang = UserModel(username="老王", email="789456123@qq.com", password="22222222", is_staff=True, role=inspect_role)

    # 添加用户到会话
    db.session.add_all([zhangsan, hanxue, laowang])

    try:
        db.session.commit()
        click.echo("测试用户添加成功")
    except Exception as e:
        db.session.rollback()
        click.echo(f"测试用户添加失败: {str(e)}")

def test():
    click.echo("test")
