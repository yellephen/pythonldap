import ldap3
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--target', help="target ip address")
	parser.add_argument('-d','--domain', help="Domain DN eg. 'DC=test,DC=local'")
	parser.add_argument('-u','--username', help="users username and domain. eg. anotherdomain\\\\administrator")
	parser.add_argument('-p','--password', help="users password")
	parser.add_argument('-l','--ldapfilter',default="(&(objectClass=*))",help="Default: (&(objectClass=*)). All Users: (objectClass=user). All SPNS: (serviceprincipalname=*)")
	
	args = parser.parse_args()
	
	server = ldap3.Server(args.target, get_info = ldap3.ALL, port =389, use_ssl = False)
	connection = ldap3.Connection(server,args.username,args.password, authentication=ldap3.NTLM)
	connection.bind()
	print(server.info)
	connection.search(search_base=args.domain, search_filter=args.ldapfilter, search_scope='SUBTREE', attributes='*')
	print(connection.entries)

if __name__ == "__main__":
    main()

