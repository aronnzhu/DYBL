from ldap3 import Server, Connection


# Ldap服务配置
class LdapServer:
    def __init__(self):
        self.ldap_server = get_fsbv('ldap_server')
        self.ldap_user = get_fsbv('ldap_user')
        self.ldap_pw = md5_decryption(get_fsbv('ldap_pw'))
        self.server = Server(self.ldap_server)


#  ldap用户绑定
class LdapUserBind(LdapServer):
    def __init__(self, username, password):
        LdapServer.__init__(self)
        self.user = User.objects.get(username=username).user_extend
        self.user_dn = self.user.dn
        self.password = password
        self.user_old_ldap_pw = md5_decryption(str(self.user.ldap_pw))

    def bind(self):
        result = True
        try:
            Connection(self.server, user=self.user_dn, password=self.password, auto_bind=True)
        except:
            result = False
        if result:
            self.update_ldap_pw()  # 检查ldap登录密码是否有变化，如有变化进行更新
        return result

    def update_ldap_pw(self):
        if self.user_old_ldap_pw != self.password:
            self.user.ldap_pw = md5_encryption(self.password)
            self.user.save()

#同步Ldap数据用
class LdapUserSyn(LdapServer):
    def __init__(self):
        LdapServer.__init__(self)
        self.conn = Connection(self.server, user=self.ldap_user,password=self.ldap_pw, auto_bind=True)

    def get_all_ldap_user_info(self):
        self.conn.search('ou=***, dc=***, dc=***', '(objectclass=person)',
            attributes=['sn','mail','givenName','displayName','entryDN'])
        return self.conn.entries

    def user_syn(self):
        print('开始同步ldap数据到封神榜...')
        i = 1
        for user in self.get_all_ldap_user_info():
            # print('正在同步第' + str(i) + '位用户数据...')
            user_info = str(user).replace(' ', '').split('\n')[:-1]
            user_ldap = {u.split(":")[0]: u.split(":")[1] for u in user_info}
            user_real_name = user_ldap['sn'] + user_ldap['givenName']
            # print(user_ldap)
            email = user_ldap['mail']
            username = str(email).split('@')[0]
            user_auth_user_need = {'username': username,
                                   'first_name': user_ldap['displayName'],
                                   'last_name': user_real_name,
                                   'email': email,
                                   'password': '123456'}
            dn = str(user_ldap['entryDN']).replace('-STATUS','')
            role = get_ou_from_ldap(user_ldap['DN'])
            if username == '***' or username == '***':
                role = 'B'
            user_extend_need = {'name': user_real_name,
                                'email': user_ldap['mail'],
                                'role': role,
                                'dn': dn,
                                'ldap_pw': md5_encryption('***')}
            # print(user_auth_user_need)
            # print(user_extend_need)
            try:
                user = User.objects.create_user(**user_auth_user_need)
                user.is_staff = True
                user.save()
                user_id = user.id
                user_extend_need['user_id'] = user_id
                user_extend.objects.create(**user_extend_need)
            except:
                user_auth_user_need.pop('password') #更新不涉及密码
                user_extend_need.pop('ldap_pw') #更新不涉及密码
                User.objects.filter(username=user_auth_user_need['username']).update(**user_auth_user_need)
                user_extend.objects.filter(name=user_extend_need['name']).update(**user_extend_need)
            # print('第' + str(i) + '位用户数据同步完成')
            i = i + 1
        print("ldap用户数据同步完成")
