import ldap3
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--target', help="target ip address")
	parser.add_argument('-d','--domain', help="Domain DN eg. 'DC=test,DC=local'")
	parser.add_argument('-u','--username', help="users username and domain. eg. anotherdomain\\\\administrator")
	parser.add_argument('-p','--password', help="users password")
	parser.add_argument('-o','--objectclass',help="The objectclass to list sams of. eg. group|user|computer ")

	args = parser.parse_args()
	
	server = ldap3.Server(args.target, get_info = ldap3.ALL, port =389, use_ssl = False)
	connection = ldap3.Connection(server,args.username,args.password, authentication=ldap3.NTLM)
	connection.bind()
	connection.search(search_base=args.domain, search_filter="(objectclass="+args.objectclass+")", search_scope='SUBTREE', attributes='samaccountname')
	for entry in connection.entries:
		print(entry['sAMAccountNAme'])

if __name__ == "__main__":
    main()

