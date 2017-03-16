__author__ = "Alex Li"

from sqlalchemy import Table, Column, Enum,Integer,String,DATE, ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


Base = declarative_base() #生成所有sqlorm的基类

user_m2m_bindhost = Table('user_m2m_bindhost', Base.metadata, #表名user_m2m_bindhost
                        Column('userprofile_id', Integer, ForeignKey('user_profile.id')),#外键关联user_profile表的id字段
                        Column('bindhost_id', Integer, ForeignKey('bind_host.id')),#外键关联bind_host表的id字段
                        )
bindhost_m2m_hostgroup = Table('bindhost_m2m_hostgroup', Base.metadata, #表名bindhost_m2m_hostgroup
                          Column('bindhost_id', Integer, ForeignKey('bind_host.id')),#外键关联bind_host表的id字段
                          Column('hostgroup_id', Integer, ForeignKey('host_group.id')),#外键关联host_group表的id字段
                          )

user_m2m_hostgroup = Table('userprofile_m2m_hostgroup', Base.metadata,#表名userprofile_m2m_hostgroup
                               Column('userprofile_id', Integer, ForeignKey('user_profile.id')),#外键关联user_profile表的id字段
                               Column('hostgroup_id', Integer, ForeignKey('host_group.id')),#外键关联host_group表的id字段
                               )


class Host(Base):
    __tablename__ = 'host'#表名host
    id = Column(Integer,primary_key=True)#id字段，主键，自动增长
    hostname = Column(String(64),unique=True)#hostname字段，唯一
    ip = Column(String(64),unique=True)#ip字段，最大长度64，唯一
    port = Column(Integer,default=22)#port字段，整形，默认22

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = 'host_group'#表名host_group
    id = Column(Integer, primary_key=True)#id字段，主键，自动增长
    name = Column(String(64), unique=True)#name字段，唯一
    #多对多关联BindHost类（注意不是表名），中间表类（注意不是表名），反向字段为host_groups
    bind_hosts = relationship("BindHost",secondary=bindhost_m2m_hostgroup,backref="host_groups")

    def __repr__(self):
        return self.name

class RemoteUser(Base):
    __tablename__ = 'remote_user'#表名remote_user
    #auth_type，username，password组合联合唯一约束
    __table_args__ = (UniqueConstraint('auth_type', 'username','password', name='_user_passwd_uc'),)

    id = Column(Integer, primary_key=True)#id字段，主键，自动增长
    AuthTypes = [
        ('ssh-password','SSH/Password'), #ssh-password 用于导入数据库，SH/Password用于显示
        ('ssh-key','SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))#auth_type字段，只能是选项列表里规定的值
    username = Column(String(32))#username字段，最大长度32
    password = Column(String(128))#password字段，最大长度128

    def __repr__(self):
        return self.username

class BindHost(Base):
    '''
    192.168.1.11    web
    192.168.1.11    mysql

    '''
    __tablename__ = "bind_host"#表名bind_host
    #host_id和remoteuser_id组合联合唯一约束
    __table_args__ = (UniqueConstraint('host_id','remoteuser_id', name='_host_remoteuser_uc'),)

    id = Column(Integer, primary_key=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    #group_id = Column(Integer,ForeignKey('group.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))
    host = relationship("Host",backref="bind_hosts")
    #host_group = relationship("HostGroup",backref="bind_hosts")
    remote_user = relationship("RemoteUser",backref="bind_hosts")
    def __repr__(self):
        return "<%s -- %s >" %(self.host.ip,
                                   self.remote_user.username
                                  )

class UserProfile(Base):
    __tablename__ = 'user_profile'#表名user_profile
    id = Column(Integer, primary_key=True)#id字段，主键，自动增长
    username = Column(String(32),unique=True)#username字段，最大长度32，唯一
    password = Column(String(128))#password字段，最大长度128
    #多对多关联BindHost类（注意不是表名），中间表类（注意不是表名），反向字段为user_profiles
    bind_hosts = relationship("BindHost", secondary=user_m2m_bindhost,backref="user_profiles")
    # 多对多关联BindHost类（注意不是表名），中间user_m2m_hostgroup表类（注意不是表名，如果要填表名可以是"userprofile_m2m_hostgroup"），反向字段为user_profiles
    host_groups = relationship("HostGroup",secondary=user_m2m_hostgroup,backref="user_profiles")

    def __repr__(self):
        return self.username


# class AuditLog(Base):
#     pass


if __name__ == "__main__":
    engine = create_engine("mysql+pymysql://root:alex3714@192.168.16.86/oldboydb?charset=utf8",
                           )
    Base.metadata.create_all(engine)  # 创建表结构